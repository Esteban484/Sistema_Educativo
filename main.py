#IMPORTAR LIBRERIA PARA USAR FRAMEWORK FLASK
from flask import Flask, request, session, redirect, url_for
from flask import render_template
import os
from flask import request
import backend
import pymysql
##llamado a flask
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'img')
app.secret_key = 'my_secret_key'
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

# Establecer la conexión a la base de datos
connection = pymysql.connect(host='db4free.net',
                             user='admin12345',
                             password='admin12345',
                             db='sisedu12345')


##servicio web
@app.route('/', methods=["GET", "POST"])
def home():
  fondoP = os.path.join(app.config['UPLOAD_FOLDER'], 'cat-4.jpg')
  return render_template('index.html', fondo=fondoP)


@app.route('/cursos', methods=["GET", "POST"])
def cursos():
  progra = os.path.join(app.config['UPLOAD_FOLDER'], 'progra.jpeg')
  ml = os.path.join(app.config['UPLOAD_FOLDER'], 'ml.png')
  va = os.path.join(app.config['UPLOAD_FOLDER'], 'va.jpg')
  ig = os.path.join(app.config['UPLOAD_FOLDER'], 'ig.png')
  return render_template('cursos.html', progra=progra, ml=ml, va=va, ig=ig)


@app.route('/login', methods=["GET", "POST"])
def login():
  # Si el usuario envía el formulario
  if request.method == 'POST':
    # Obtener los datos del formulario
    username = request.form['username']
    password = request.form['password']
    # Crear un cursor
    cursor = connection.cursor()

    # Verificar si el nombre de usuario y la contraseña son válidos
    query = 'SELECT nombre, apellido FROM estudiante WHERE cedula_est = %s AND contrasenia = %s'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    # Crear un cursor
    cursor2 = connection.cursor()

    # Verificar si el nombre de usuario y la contraseña son válidos
    query2 = 'SELECT nombre, apellido FROM profesor WHERE cedula_profesor = %s AND contrasenia = %s'
    cursor2.execute(query2, (username, password))
    result2 = cursor2.fetchone()

    # Cerrar la conexión
    connection.close()

    # Si se encuentra un usuario válido, iniciar sesión
    if result:
      session['username'] = username
      return render_template('alumno1.html', resultado=result)
    elif result2:
      session['username'] = username
      return render_template('maestro.html', resultado=result2)
    else:
      # Si no se encuentra un usuario válido, mostrar un mensaje de error
      error = 'Cédula o contraseña invalidas'
  else:
    error = None

  # Mostrar el formulario de inicio de sesión
  return render_template('login.html', error=error)


@app.route('/inscribir_estudiante', methods=['POST'])
def inscribir_estudiante():
  # obtener los datos del formulario
  nombre = request.form['nombre']
  apellido = request.form['apellido']
  cedula = request.form['cedula']
  contraseña = request.form['contrasenia']
  machine = request.form.get('machine')
  vision = request.form.get('vision')
  progra = request.form.get('programacion')
  ingenieria = request.form.get('ingenieria')
  # conectarse a la base de datos
  cur = connection.cursor()

  # ejecutar la consulta INSERT con parámetros de sustitución
  cur.execute(
    '''INSERT INTO estudiante (cedula_est, contrasenia, nombre, apellido, curso) VALUES (%s, %s, %s,%s,%s)''',
    (cedula, contraseña, nombre, apellido, machine))

  # confirmar la transacción
  connection.commit()
  cur.close()
  connection.close()

  return 'Usuario agregado exitosamente'


@app.route('/docentes', methods=["GET", "POST"])
def docentes():
  return render_template('docentes.html')


@app.route('/inscripciones', methods=["GET", "POST"])
def inscripciones():
  return render_template('insc.html')


@app.route('/alumno1', methods=["GET", "POST"])
def alumno1():
  # Verificar si el usuario ha iniciado sesión
  if 'username' in session:
    # Mostrar la página de "home"
    return render_template('alumno1.html')
  else:
    # Redirigir al usuario al formulario de inicio de sesión
    return redirect(url_for('login'))


@app.route('/about', methods=["GET", "POST"])
def about():
  joel = os.path.join(app.config['UPLOAD_FOLDER'], 'joel.jpeg')
  robbi = os.path.join(app.config['UPLOAD_FOLDER'], 'robbi.jpg')
  fer = os.path.join(app.config['UPLOAD_FOLDER'], 'fer.jpg')
  nando = os.path.join(app.config['UPLOAD_FOLDER'], 'nando.jpg')
  esteban = os.path.join(app.config['UPLOAD_FOLDER'], 'esteban.jpg')
  return render_template('about.html',
                         joel=joel,
                         robbi=robbi,
                         fer=fer,
                         nando=nando,
                         esteban=esteban)


@app.route('/info', methods=["GET", "POST"])
def info():
  return render_template('info.html')


@app.route('/calificaciones', methods=["GET", "POST"])
def calificaciones():
  return render_template('calificaciones.html')


@app.route('/maestro', methods=["GET", "POST"])
def maestro():
  return render_template('maestro.html')


@app.route('/calificar', methods=["GET", "POST"])
def calificar():
  return render_template('calificar_estudiantes.html')


##ejecutar el servicio web
if __name__ == '__main__':
  #OJO QUITAR EL DEBUG EN PRODUCCION
  app.run(host='0.0.0.0', port=5000, debug=True)
