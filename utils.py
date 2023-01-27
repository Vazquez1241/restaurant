import models
import database

def crear_usuario():
    user = models.User('w','0')
    database.db.session.add(user)
    database.db.session.commit()
    print("Se ha creado el usuario correctamente")

