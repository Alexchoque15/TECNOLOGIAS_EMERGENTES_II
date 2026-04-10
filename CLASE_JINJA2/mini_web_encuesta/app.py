from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# SIULAMOS UNA BASE DE DATOS 
respuestas = []

@app.route('/')
def inicio():
    return redirect(url_for('encuesta'))

@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form['nombre']
    lenguaje = request.form['lenguaje']
    experiencia = request.form['experiencia']

    data = {
        'nombre': nombre,
        'lenguaje': lenguaje,
        'experiencia': experiencia
    }

    respuestas.append(data)

    return render_template('resultado.html', data=data)

@app.route('/dashboard')
def dashboard():
    total = len(respuestas)

    conteo = {}
    for r in respuestas:
        lang = r['lenguaje']
        conteo[lang] = conteo.get(lang, 0) + 1

    # 👇 CALCULAR PORCENTAJES
    porcentajes = {}
    for lang, cantidad in conteo.items():
        if total > 0:
            porcentajes[lang] = (cantidad / total) * 100
        else:
            porcentajes[lang] = 0

    return render_template('dashboard.html',
                            total=total,
                            conteo=conteo,
                            porcentajes=porcentajes,
                            respuestas=respuestas)

if __name__ == '__main__':
    app.run(debug=True)