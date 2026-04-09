from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form['nombre']
    return render_template('resultado.html', nombre=nombre)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 