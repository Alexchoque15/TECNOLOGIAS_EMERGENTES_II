from flask import Flask, session, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "carrito_avanzado"

@app.route("/")
def index():
    carrito = session.get("carrito", [])
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    return render_template("carrito_v2.html", carrito=carrito, total=total)

@app.route("/agregar", methods=["POST"])
def agregar():
    producto = request.form.get("producto", "").strip()
    precio_str = request.form.get("precio", "").strip()
    cantidad_str = request.form.get("cantidad", "").strip()

    if not producto or not precio_str or not cantidad_str:
        flash("Debes llenar todos los campos", "warning")
        return redirect(url_for("index"))

    try:
        precio = float(precio_str)
        cantidad = int(cantidad_str)
    except ValueError:
        flash("Precio o cantidad inválidos", "danger")
        return redirect(url_for("index"))

    if "carrito" not in session:
        session["carrito"] = []

    session["carrito"].append({
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad
    })

    session.modified = True

    flash("Producto agregado correctamente", "success")

    return redirect(url_for("index"))

@app.route("/limpiar")
def limpiar():
    session.pop("carrito", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)