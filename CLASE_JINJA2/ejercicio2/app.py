from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def encuesta():
    return render_template('encuesta.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form['nombre']
    lenguaje = request.form['lenguaje']
    experiencia = request.form['experiencia']

    return render_template(
        'resultado_encuesta.html',
        nombre=nombre,
        lenguaje=lenguaje,
        experiencia=experiencia
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))