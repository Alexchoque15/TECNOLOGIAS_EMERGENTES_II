from flask import Flask, session, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "carrito_secret_key"

@app.route("/")
def index():
    carrito = session.get("carrito", [])
    return render_template("carrito.html", carrito=carrito)

@app.route("/agregar", methods=["POST"])
def agregar():
    producto = request.form.get("producto")

    if "carrito" not in session:
        session["carrito"] = []

    session["carrito"].append(producto)
    session.modified = True

    return redirect(url_for("index"))

@app.route("/limpiar")
def limpiar():
    session.pop("carrito", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)