from flask import Flask, render_template, request, redirect, url_for, flash
from config import *
from models import db, Contacto
from datetime import datetime
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = "empresa_secret_key"

# Configuración BD
app.config.from_object("config")
db.init_app(app)

# Crear tablas
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":

        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        if not nombre or not email or not mensaje:
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for("contacto"))

        nuevo = Contacto(
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )

        db.session.add(nuevo)
        db.session.commit()

        flash("Mensaje enviado correctamente", "success")
        return redirect(url_for("contacto"))

    return render_template("contacto.html")

@app.route("/contactos")
def ver_contactos():
    contactos = Contacto.query.all()
    return render_template("ver_contactos.html", contactos=contactos)


@app.route("/dashboard")
def dashboard():
    total_contactos = Contacto.query.count()

    hoy = datetime.utcnow().date()

    contactos_hoy = Contacto.query.filter(
        func.date(Contacto.fecha) == hoy
    ).count()

    return render_template(
        "dashboard.html",
        total_contactos=total_contactos,
        contactos_hoy=contactos_hoy
    )


if __name__ == "__main__":
    app.run(debug=True)