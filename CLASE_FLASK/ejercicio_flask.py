from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 3500, "categoria": "tecnologia"},
    {"id": 2, "nombre": "Mouse", "precio": 50, "categoria": "tecnologia"},
    {"id": 3, "nombre": "Cuaderno", "precio": 20, "categoria": "papeleria"}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/api/productos")
def obtener_productos():
    return jsonify(productos)

@app.route("/agregar", methods=["POST"])
def agregar():
    data = request.json
    nuevo = {
        "id": len(productos) + 1,
        "nombre": data["nombre"],
        "precio": float(data["precio"]),
        "categoria": data["categoria"]
    }
    productos.append(nuevo)
    return jsonify(nuevo)

@app.route("/eliminar/<int:id>", methods=["DELETE"])
def eliminar(id):
    global productos
    productos = [p for p in productos if p["id"] != id]
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)