#importacion del framework
from flask import Flask
from flask_mysqldb import MySQL


#inicializacion del APP
app= Flask(__name__)


#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql= MySQL(app)


#declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    return "Hola Mundo FLASK"

@app.route('/guardar')
def guardar():
    return "se guardo en la base  de datos"

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la base de datos"


#ejecucion del servidor en el puerto 5000
if __name__ == "_main_":
    app.run(port=5000,debug=True)