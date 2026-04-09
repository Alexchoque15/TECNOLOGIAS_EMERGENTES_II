#RUTAS CON TIPOS DE DATOS

from flask import Flask

app = Flask(__name__)

@app.route("/cadena/<string:nombre>")
def demo_cadena(nombre):
    return f"Cadena; {nombre} => tipo de dato: {type(nombre).__name__}"

@app.route("/entero/<int:numero>")
def demo_entero(numero):
    return f"Entero: {numero} => Tipo de dato: {type(numero).__name__}"

@app.route('/decimal/<float:decimal>')
def demo_float(decimal):
    return f"Float. {decimal} => Tipo de dato: {type(decimal).__name__}"

@app.route("/ruta/<path:ruta>")
def demo_ruta(ruta):
    return f"Ruta: {ruta}"

if __name__ == "__main__":
    app.run(debug=True) 