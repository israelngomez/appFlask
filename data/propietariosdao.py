from data.modelo.propietario import Propietario


class Propietariosdao:
    def __init__(self,db) -> None:
        self.db = db

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM propietarios')
        data = cursor.fetchall()
        propietarios = []

        for propietario in data :
            propietarios.append(Propietario(propietario[0],propietario[1],propietario[2],propietario[3],propietario[4]))
        return propietarios
    def addPropietario(self,propietario):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO propietarios (id,nombre,apellidos,dnie,id_vehiculo) VALUES  ( %s, %s, %s, %s, %s)',(propietario.id,propietario.nombre,propietario.apellidos,propietario.dnie,propietario.id_vehiculo))
        self.db.commit()
    
    def deletePropietario(self,id):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM propietarios WHERE id = %s',(id,))
        self.db.commit()