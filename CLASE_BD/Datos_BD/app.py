from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# CONEXION
def get_db_connection():
    conn = sqlite3.connect('../zoo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    animales = conn.execute("SELECT * FROM animales").fetchall()
    conn.close()
    return render_template("datos.html", animales=animales)

# INSERTAR DATOS
@app.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form['nombre']
    especie = request.form['especie']
    fecha = request.form['fecha']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO animales (nombre, especie, fecha_nacimiento) VALUES (?, ?, ?)",
        (nombre, especie, fecha)
    )
    conn.commit()
    conn.close()

    return redirect('/')

#VER DATOS
@app.route('/ver_tablas')
def ver_tablas():
    conn = sqlite3.connect('../zoo.db')
    conn.row_factory = sqlite3.Row

    animales = conn.execute("SELECT * FROM animales").fetchall()
    habitats = conn.execute("SELECT * FROM habitats").fetchall()
    cuidadores = conn.execute("SELECT * FROM cuidadores").fetchall()
    asignaciones = conn.execute("SELECT * FROM asignaciones").fetchall()

    conn.close()

    return render_template(
        "ver_tablas.html",
        animales=animales,
        habitats=habitats,
        cuidadores=cuidadores,
        asignaciones=asignaciones
    )

if __name__ == '__main__':
    app.run(debug=True)