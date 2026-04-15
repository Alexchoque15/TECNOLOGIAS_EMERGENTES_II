from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect('../zoo.db')


# LISTAR
@app.route('/')
def index():
    conn = get_db()
    animales = conn.execute("SELECT * FROM animales").fetchall()
    conn.close()
    return render_template("animales.html", animales=animales)


# CREAR
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especie = request.form['especie']
        fecha = request.form['fecha']

        conn = get_db()
        conn.execute(
            "INSERT INTO animales (nombre, especie, fecha_nacimiento) VALUES (?, ?, ?)",
            (nombre, especie, fecha)
        )
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template("crear.html")


# ELIMINAR
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute("DELETE FROM animales WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')


# EDITAR
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db()

    if request.method == 'POST':
        nombre = request.form['nombre']
        especie = request.form['especie']
        fecha = request.form['fecha']

        conn.execute(
            "UPDATE animales SET nombre=?, especie=?, fecha_nacimiento=? WHERE id=?",
            (nombre, especie, fecha, id)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    animal = conn.execute("SELECT * FROM animales WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("editar.html", animal=animal)


if __name__ == '__main__':
    app.run(debug=True)