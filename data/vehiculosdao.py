from data.modelo.vehiculos import Vehiculo

class Vehiculosdao:
    def __init__(self,db) -> None:
        self.db = db

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM vehiculos')
        data = cursor.fetchall()
        vehiculos = []

        for vehiculo in data :
            vehiculos.append(Vehiculo(vehiculo[0],vehiculo[1],vehiculo[2],vehiculo[3],vehiculo[4],vehiculo[5]))

        return vehiculos
    def addVehiculo(self,vehiculo):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO vehiculos (id,matricula,color,modelo,año,marca) VALUES  ( %s, %s, %s, %s, %s, %s)',(vehiculo.id,vehiculo.matricula,vehiculo.color,vehiculo.modelo,vehiculo.año,vehiculo.marca))
        self.db.commit()

        
    def deleteVehiculo(self,matricula):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM vehiculos WHERE matricula = %s',(matricula,))
        self.db.commit()