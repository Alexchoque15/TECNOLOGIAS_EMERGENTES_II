import os
import psycopg2.extras
import datetime

from flask import Flask, render_template, request, redirect, session
from db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from functools import wraps
from reportlab.lib.utils import ImageReader


app = Flask(__name__)
app.secret_key = "1234"

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return wrapper


@app.route('/')
def index():
    q = request.args.get('q')

    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if q:
        cur.execute("""
            SELECT * FROM cursos
            WHERE titulo ILIKE %s OR descripcion ILIKE %s
        """, ('%' + q + '%', '%' + q + '%'))
    else:
        cur.execute("SELECT * FROM cursos")

    cursos = cur.fetchall()
    conn.close()

    return render_template('index.html', cursos=cursos)


@app.route('/curso/<int:id>')
def curso(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT * FROM cursos WHERE id=%s", (id,))
    curso = cur.fetchone()

    conn.close()

    return render_template('curso.html', curso=curso)


@app.route('/inscribirse/<int:curso_id>', methods=['POST'])
@login_required
def inscribirse(curso_id):

    user_id = session['user_id']
    metodo = request.form.get('metodo_pago')

    if not metodo:
        return "Selecciona método de pago"

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO inscripciones (usuario_id, curso_id)
        VALUES (%s,%s)
        ON CONFLICT DO NOTHING
    """, (user_id, curso_id))

    cur.execute("""
        INSERT INTO pagos (usuario_id, curso_id, monto, estado)
        VALUES (%s,%s,%s,%s)
    """, (user_id, curso_id, 100, metodo))

    conn.commit()
    conn.close()

    return redirect('/mis_cursos')


@app.route('/favorito/<int:curso_id>')
@login_required
def favorito(curso_id):

    conn = get_connection()
    cur = conn.cursor()

    # Ver si ya existe
    cur.execute("""
        SELECT * FROM favoritos
        WHERE usuario_id=%s AND curso_id=%s
    """, (session['user_id'], curso_id))

    existe = cur.fetchone()

    if existe:
        # quitar favorito
        cur.execute("""
            DELETE FROM favoritos
            WHERE usuario_id=%s AND curso_id=%s
        """, (session['user_id'], curso_id))
    else:
        # agregar favorito
        cur.execute("""
            INSERT INTO favoritos (usuario_id, curso_id)
            VALUES (%s,%s)
        """, (session['user_id'], curso_id))

    conn.commit()
    conn.close()

    return redirect(request.referrer)

@app.route('/favoritos')
@login_required
def favoritos():

    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("""
        SELECT cursos.id, cursos.titulo, cursos.precio, cursos.imagen
        FROM favoritos
        JOIN cursos ON cursos.id = favoritos.curso_id
        WHERE favoritos.usuario_id=%s
    """, (session['user_id'],))

    cursos = cur.fetchall()
    conn.close()

    return render_template('favoritos.html', cursos=cursos)


@app.route('/mis_cursos')
@login_required
def mis_cursos():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT cursos.id,
               cursos.titulo,
               cursos.precio,
               inscripciones.progreso,
               inscripciones.completado
        FROM inscripciones
        JOIN cursos ON cursos.id = inscripciones.curso_id
        WHERE usuario_id=%s
    """, (session['user_id'],))

    cursos = cur.fetchall()
    conn.close()

    return render_template('mis_cursos.html', cursos=cursos)


@app.route('/dashboard')
@login_required
def dashboard():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM inscripciones WHERE usuario_id=%s", (session['user_id'],))
    inscritos = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM favoritos WHERE usuario_id=%s", (session['user_id'],))
    favoritos = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM pagos WHERE usuario_id=%s", (session['user_id'],))
    pagos = cur.fetchone()[0]

    conn.close()

    return render_template('dashboard.html',
                           inscritos=inscritos,
                           favoritos=favoritos,
                           pagos=pagos)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
        user = cur.fetchone()

        if user and check_password_hash(user['password'], password):

            # ---------------------------
            # SESIÓN PRINCIPAL
            # ---------------------------
            session['user_id'] = user['id']
            session['nombre'] = user['nombre']
            session['rol'] = user['rol']

            # ---------------------------
            # FAVORITOS EN SESIÓN (PRO)
            # ---------------------------
            cur.execute("""
                SELECT curso_id FROM favoritos
                WHERE usuario_id=%s
            """, (user['id'],))

            favoritos = cur.fetchall()
            session['favoritos_ids'] = [f['curso_id'] for f in favoritos]

            conn.close()

            return redirect('/')

        conn.close()
        return "Credenciales incorrectas"

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/admin')
@login_required
def admin():

    if session.get('rol') != 'admin':
        return "Acceso denegado"

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM cursos")
    cursos = cur.fetchall()

    conn.close()

    return render_template('admin.html', cursos=cursos)


@app.route('/crear_curso', methods=['GET', 'POST'])
@login_required
def crear_curso():

    if session.get('rol') != 'admin':
        return "Acceso denegado"

    if request.method == 'POST':

        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        precio = request.form['precio']

        imagen = request.files.get('imagen')

        if imagen and imagen.filename:
            filename = secure_filename(imagen.filename)
            ruta = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagen.save(ruta)
            ruta_bd = f"/static/uploads/{filename}"
        else:
            ruta_bd = None

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO cursos (titulo, descripcion, precio, imagen)
            VALUES (%s,%s,%s,%s)
        """, (titulo, descripcion, precio, ruta_bd))

        conn.commit()
        conn.close()

        return redirect('/admin')

    return render_template('crear_curso.html')


@app.route('/certificado/<int:curso_id>')
@login_required
def certificado(curso_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT titulo FROM cursos WHERE id=%s", (curso_id,))
    curso = cur.fetchone()

    if not curso:
        return "Curso no encontrado"

    nombre = session['nombre']

    fecha_actual = datetime.date.today()

    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]

    fecha = f"{fecha_actual.day} de {meses[fecha_actual.month - 1]} del {fecha_actual.year}"
    registro = f"DEV-{curso_id}-{session['user_id']}-{int(datetime.datetime.now().timestamp())}"

    plantilla_path = "static/crt.png"
    plantilla = ImageReader(plantilla_path)

    img_width, img_height = plantilla.getSize()

    os.makedirs("static/certificados", exist_ok=True)

    filename = f"certificado_{curso_id}_{session['user_id']}.pdf"
    filepath = os.path.join("static/certificados", filename)

    c = canvas.Canvas(filepath, pagesize=(img_width, img_height))

    c.drawImage(plantilla, 0, 0, width=img_width, height=img_height)

    c.setFont("Times-Italic", 28)
    c.drawCentredString(img_width/2, img_height * 0.465, nombre)

    c.setFont("Times-Italic", 18)
    c.drawCentredString(img_width/2, img_height * 0.345, curso[0])

    c.setFont("Times-Italic", 15)
    c.drawString(img_width * 0.38, img_height * 0.171, fecha)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(img_width * 0.415, img_height * 0.115, registro)

    c.save()

    return redirect(f"/static/certificados/{filename}")

@app.route('/admin_estadisticas')
@login_required
def admin_estadisticas():

    if session.get('rol') != 'admin':
        return "Acceso denegado"

    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT COUNT(*) FROM usuarios")
    usuarios = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM cursos")
    cursos = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM inscripciones")
    inscripciones = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM pagos")
    pagos = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM favoritos")
    favoritos = cur.fetchone()[0]

    cur.execute("""
        SELECT u.nombre, c.titulo, i.fecha_inscripcion, i.progreso
        FROM inscripciones i
        JOIN usuarios u ON u.id = i.usuario_id
        JOIN cursos c ON c.id = i.curso_id
        ORDER BY i.fecha_inscripcion DESC
        LIMIT 20
    """)
    actividad = cur.fetchall()

    conn.close()

    return render_template(
        'admin_estadisticas.html',
        usuarios=usuarios,
        cursos=cursos,
        inscripciones=inscripciones,
        pagos=pagos,
        favoritos=favoritos,
        actividad=actividad
    )

@app.route('/editar_curso/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_curso(id):

    if session.get('rol') != 'admin':
        return "Acceso denegado"

    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':

        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        precio = request.form['precio']

        imagen = request.files.get('imagen')

        if imagen and imagen.filename:

            filename = secure_filename(imagen.filename)
            ruta = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagen.save(ruta)
            ruta_bd = f"/static/uploads/{filename}"

            cur.execute("""
                UPDATE cursos
                SET titulo=%s,
                    descripcion=%s,
                    precio=%s,
                    imagen=%s
                WHERE id=%s
            """, (titulo, descripcion, precio, ruta_bd, id))

        else:

            cur.execute("""
                UPDATE cursos
                SET titulo=%s,
                    descripcion=%s,
                    precio=%s
                WHERE id=%s
            """, (titulo, descripcion, precio, id))

        conn.commit()
        conn.close()

        return redirect('/admin')

    cur.execute("SELECT * FROM cursos WHERE id=%s", (id,))
    curso = cur.fetchone()

    conn.close()

    return render_template('editar_curso.html', curso=curso)

@app.route('/eliminar_curso/<int:id>')
@login_required
def eliminar_curso(id):

    if session.get('rol') != 'admin':
        return "Acceso denegado"

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM cursos WHERE id=%s", (id,))

    conn.commit()
    conn.close()

    return redirect('/admin')

@app.route('/progreso/<int:curso_id>', methods=['POST'])
@login_required
def progreso(curso_id):

    progreso = request.form['progreso']

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE inscripciones
        SET progreso=%s
        WHERE usuario_id=%s AND curso_id=%s
    """, (progreso, session['user_id'], curso_id))

    conn.commit()
    conn.close()

    return redirect('/mis_cursos')

@app.route('/completar/<int:curso_id>')
@login_required
def completar(curso_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE inscripciones
        SET completado = TRUE,
            progreso = 100
        WHERE usuario_id=%s AND curso_id=%s
    """, (session['user_id'], curso_id))

    conn.commit()
    conn.close()

    return redirect('/mis_cursos')

@app.route('/registro', methods=['GET', 'POST'])
def registro():

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO usuarios (nombre, email, password)
            VALUES (%s,%s,%s)
        """, (nombre, email, password))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/admin_limpiar_datos', methods=['POST'])
@login_required
def admin_limpiar_datos():

    if session.get('rol') != 'admin':
        return "Acceso denegado"

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM inscripciones")
    cur.execute("DELETE FROM pagos")
    cur.execute("DELETE FROM favoritos")

    conn.commit()
    conn.close()

    return redirect('/admin_estadisticas')

if __name__ == '__main__':
    app.run(debug=True)