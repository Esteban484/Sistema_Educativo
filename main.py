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


@app.route('/inscribir_estudiante', methods = ["GET","POST"])
def inscribir_estudiante():
    # obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form['cedula']
    contraseña = request.form['contrasenia']
    curso = request.form.get('inlineRadioOptions')
    # conectarse a la base de datos
    cur = connection.cursor()

    # ejecutar la consulta INSERT con parámetros de sustitución
    cur.execute('''INSERT INTO estudiante (id_est, contrasenia, nombre, apellido, curso) VALUES (%s, %s, %s,%s,%s)''', (cedula, contraseña, nombre,apellido,curso))
    connection.ping()
    # confirmar la transacción
    connection.commit()
    connection.ping()
    cur.close()
    connection.close()

    return render_template('insc.html',result = 'Usuario agregado exitosamente. Inicie Sesión')

@app.route('/inscripcion_estudiante_admin', methods = ["GET","POST"])
def inscripcion_estudiante_admin():
    # obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form['cedula']
    contraseña = request.form['contrasenia']
    curso = request.form.get('inlineRadioOptions')
    # conectarse a la base de datos
    cur = connection.cursor()

    # ejecutar la consulta INSERT con parámetros de sustitución
    cur.execute('''INSERT INTO estudiante (id_est, contrasenia, nombre, apellido, curso) VALUES (%s, %s, %s,%s,%s)''', (cedula, contraseña, nombre,apellido,curso))
    connection.ping()
    # confirmar la transacción
    connection.commit()
    connection.ping()
    cur.close()
    connection.ping()
    connection.close()

    return render_template('inscribir_estudiante.html',result = 'Usuario agregado exitosamente. Inicie Sesión')

@app.route('/inscripcion_docente_admin', methods = ["GET","POST"])
def inscripcion_docente_admin():
    # obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form['cedula']
    contraseña = request.form['contrasenia']
    curso = request.form.get('inlineRadioOptions')
    # conectarse a la base de datos
    cur = connection.cursor()

    # ejecutar la consulta INSERT con parámetros de sustitución
    cur.execute('''INSERT INTO profesor (id_profesor, contrasenia, nombre, apellido, curso_dirigido) VALUES (%s, %s, %s,%s,%s)''', (cedula, contraseña, nombre,apellido,curso))
    connection.ping()
    # confirmar la transacción
    connection.commit()
    connection.ping()
    cur.close()
    connection.ping()
    connection.close()

    return render_template('inscribir_docente.html',result = 'Usuario agregado exitosamente. Inicie Sesión')



@app.route('/inscripciones', methods = ["GET","POST"])
def inscripciones():
    return render_template('insc.html')

@app.route('/alumno1', methods = ["GET","POST"])
def alumno1():
    # Verificar si el usuario ha iniciado sesión
    if 'username' in session:
        # Mostrar la página de "home"
        return render_template('alumno1.html')
    else:
        # Redirigir al usuario al formulario de inicio de sesión
        return redirect(url_for('login'))
    

@app.route('/about', methods = ["GET","POST"])
def about():
    cami = os.path.join(app.config['UPLOAD_FOLDER'], 'cami.jpeg')
    joss = os.path.join(app.config['UPLOAD_FOLDER'], 'joss.jpeg')
    gus = os.path.join(app.config['UPLOAD_FOLDER'], 'gus.jpg')
    jona = os.path.join(app.config['UPLOAD_FOLDER'], 'jona.jpg')
    alexis = os.path.join(app.config['UPLOAD_FOLDER'], 'alexis.jpeg')
    return render_template('about.html',cami=cami, joss=joss , gus=gus, jona=jona,alexis=alexis)

@app.route('/docentes', methods = ["GET","POST"])
def docentes():
    profe1 = os.path.join(app.config['UPLOAD_FOLDER'], 'profe1.jpg')
    profe2 = os.path.join(app.config['UPLOAD_FOLDER'], 'profe2.jpg')
    profe3 = os.path.join(app.config['UPLOAD_FOLDER'], 'profe3.jpg')
    profe4 = os.path.join(app.config['UPLOAD_FOLDER'], 'profe4.jpg')
    
    return render_template('docentes.html',profe1=profe1, profe2=profe2 , profe3=profe3, profe4=profe4)

@app.route('/info', methods = ["GET","POST"])
def info():
    return render_template('info.html')

@app.route('/calificaciones', methods = ["GET","POST"])
def calificaciones():
    # Crear un cursor
    cursor = connection.cursor()
    # Verificar si el nombre de usuario y la contraseña son válidos
    query = 'select e.nombre, e.apellido from estudiante AS e where e.curso = (SELECT p.curso_dirigido from profesor AS p where p.id_profesor = %s);'
    connection.ping()
    cursor.execute(query, (valor_id))
    result = cursor.fetchall()
    return render_template('calificaciones.html', resultado = result)
   

@app.route('/maestro', methods = ["GET","POST"])
def maestro():
    return render_template('maestro.html')

@app.route('/calificar', methods = ["GET","POST"])
def calificar():
    return render_template('calificar_estudiantes.html')

@app.route('/administrador', methods = ["GET","POST"])
def administrador():
    return render_template('administrador.html')

@app.route('/inscribirEstudiante', methods = ["GET","POST"])
def inscribirEst():
    connection.ping()
    return render_template('inscribir_estudiante.html')

@app.route('/inscribirDocente', methods = ["GET","POST"])
def inscribirDoce():
    connection.ping()
    return render_template('inscribir_docente.html')


##ejecutar el servicio web
if __name__ == '__main__':
  #OJO QUITAR EL DEBUG EN PRODUCCION
  app.run(host='0.0.0.0', port=5000, debug=True)
