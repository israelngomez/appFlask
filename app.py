from flask import Flask, render_template, request, redirect, url_for
from data.vehiculosdao import Vehiculosdao
from data.propietariosdao import Propietariosdao
from data.modelo.vehiculos import Vehiculo
from data.modelo.propietario import Propietario




import mysql.connector




app = Flask(__name__)


db= mysql.connector.connect(
    host="informatica.iesquevedo.es",
    port=3333,
    user="root",
    password="1asir",
    database="israel"
    
)





@app.route('/')
def home():
    
    return render_template('index.html',)

@app.route('/vehiculo.html')
def vehiculos():
  
   vehiculosdao : Vehiculosdao = Vehiculosdao(db)
   return render_template('vehiculo.html', vehiculos=vehiculosdao.get_all())
   
    
@app.route('/propietario.html')
def propietario():
    propietariosdao : Propietariosdao = Propietariosdao(db)
    return render_template('propietario.html', propietarios = propietariosdao.get_all())   

@app.route('/addpropietarios', methods=['POST'])
def addpropietarios():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        dnie = request.form['dnie']
        id_vehiculo = request.form['id_vehiculo']
       
        propietario = Propietario(id,nombre,apellidos,dnie,id_vehiculo)
        propietariosdao : Propietariosdao = Propietariosdao(db)
        propietariosdao.addPropietario(propietario)
        return redirect(url_for('propietario'))
@app.route('/addvehiculos', methods=['POST'])
def addvehiculos():
    if request.method == 'POST':
        matricula = request.form['matricula']
        color = request.form['color']
        modelo = request.form['modelo']
        año = request.form['año']
        marca = request.form['marca']
        id = request.form['id']
        vehiculo = Vehiculo(matricula,color,modelo,año,marca,id)
        vehiculosdao : Vehiculosdao = Vehiculosdao(db)
        vehiculosdao.addVehiculo(vehiculo)
        return redirect(url_for('vehiculos'))

@app.route('/deletepropietarios/<string:id>')
def deletepropietarios(id):
    propietariosdao : Propietariosdao = Propietariosdao(db)
    propietariosdao.deletePropietario(id)
    return redirect(url_for('propietario'))

@app.route('/deletevehiculos/<string:matricula>')
def deletevehiculos(matricula):
    vehiculosdao : Vehiculosdao = Vehiculosdao(db)
    vehiculosdao.deleteVehiculo(matricula)
    return redirect(url_for('vehiculos'))

if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')

