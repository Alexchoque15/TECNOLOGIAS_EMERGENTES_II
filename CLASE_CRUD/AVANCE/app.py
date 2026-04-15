from flask import Flask,session,request,render_template,make_response,url_for,flash

app = Flask(__name__)
app.secret_key = '8350e5a3e24c153df2275c9f80692773'

@app.route("/")
def index():
    return render_template('index.html',mensaje="Pagina principal")

#Rutas para gestionar gestiones
@app.route("/set_data")
def set_data():
    # Almacenar datos o variables en la sesion
    session['nombre'] = 'Elsa'
    session['tema'] = 'Oscuro'
    return render_template('index.html',mensaje='Datos de sesion guardados')

@app.route('/get_data')
def get_data():
    if 'nombre' not in session or 'tema' not in session:
        return render_template('index.html',mensaje='No hay datos en la session')
    
    #Recuperar datos de session
    nombre = session['nombre']
    tema = session['tema']
    return render_template('index.html',mensaje=f"Nombre: {nombre} Tema: {tema}")

@app.route("/clear_session")
def clear_session():
    session.clear()
    return render_template('index.html',mensaje="Datos de session eliminados")

#Rutas para gestionar cookies
@app.route("/set_cookie")
def set_cookie():
    respuesta = make_response(render_template('index.html',mensaje="cookie guardados"))
    respuesta.set_cookie("cookie_usuario","Alan")
    respuesta.set_cookie("cookie_color","Rojo")
    return respuesta

@app.route("/get_cookie")
def get_cookie():
    usuario = request.cookies.get('cookie_usuario')
    color = request.cookies.get('cookie_color')
    return render_template('index.html',mensaje=f'Cookie usuario: {usuario} Cookie color:{color}')

@app.route("/borrar_cookies")
def eliminar_cookies():
    response = make_response(render_template('index.html',mensaje="cookies eliminadas"))
    response.set_cookie('cookie_usuario','',expires=0)
    response.set_cookie('cookie_color','',expires=0)
    return response

if __name__ == "__main__":
    app.run(debug=True)