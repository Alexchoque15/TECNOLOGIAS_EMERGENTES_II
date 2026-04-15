from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contactos = []
id_counter = 1

@app.route("/")
def index():
    return render_template("contactos.html", contactos=contactos)

@app.route("/agregar", methods=["POST"])
def agregar():
    global id_counter

    contacto = {
        "id": id_counter,
        "nombre": request.form.get("nombre"),
        "correo": request.form.get("correo"),
        "celular": request.form.get("celular")
    }

    contactos.append(contacto)
    id_counter += 1

    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    global contactos
    contactos = [c for c in contactos if c["id"] != id]
    return redirect(url_for("index"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    contacto = next((c for c in contactos if c["id"] == id), None)

    if request.method == "POST":
        contacto["nombre"] = request.form.get("nombre")
        contacto["correo"] = request.form.get("correo")
        contacto["celular"] = request.form.get("celular")
        return redirect(url_for("index"))

    return render_template("editar.html", contacto=contacto)

if __name__ == "__main__":
    app.run(debug=True)