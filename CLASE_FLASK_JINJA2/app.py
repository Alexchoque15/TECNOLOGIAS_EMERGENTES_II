from flask import Flask, render_template, request, redirect, url_for, flash
import os
from config import *
from models import db, Contacto
from datetime import datetime
from sqlalchemy import func
import re

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev_key_seguro")

app.config.from_object("config")
db.init_app(app)

with app.app_context():
    db.create_all()

def email_valido(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

@app.route("/")
def index():
    return render_template("index.html")

# CREATE
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        if not nombre or not email or not mensaje:
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for("contacto"))

        if not email_valido(email):
            flash("Email inválido", "danger")
            return redirect(url_for("contacto"))

        try:
            nuevo = Contacto(nombre=nombre, email=email, mensaje=mensaje)
            db.session.add(nuevo)
            db.session.commit()
            flash("Mensaje enviado correctamente", "success")
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("Error al guardar", "danger")

        return redirect(url_for("contacto"))

    return render_template("contacto.html")

# READ
@app.route("/contactos")
def ver_contactos():
    contactos = Contacto.query.order_by(Contacto.id.desc()).all()
    return render_template("ver_contactos.html", contactos=contactos)

# UPDATE
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    contacto = Contacto.query.get_or_404(id)

    if request.method == "POST":
        contacto.nombre = request.form.get("nombre").strip()
        contacto.email = request.form.get("email").strip()
        contacto.mensaje = request.form.get("mensaje").strip()

        if not email_valido(contacto.email):
            flash("Email inválido", "danger")
            return redirect(url_for("editar", id=id))

        try:
            db.session.commit()
            flash("Contacto actualizado", "success")
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("Error al actualizar", "danger")

        return redirect(url_for("ver_contactos"))

    return render_template("editar.html", contacto=contacto)

# DELETE
@app.route("/eliminar/<int:id>")
def eliminar(id):
    contacto = Contacto.query.get_or_404(id)

    try:
        db.session.delete(contacto)
        db.session.commit()
        flash("Contacto eliminado", "success")
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("Error al eliminar", "danger")

    return redirect(url_for("ver_contactos"))

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

