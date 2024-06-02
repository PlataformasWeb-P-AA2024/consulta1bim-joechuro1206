from pymongo import MongoClient

def crear_base():
    # Dirección del servidor, nos conectamos a través
    # del protocolo mongodb a nuestro servidor
    MONGO_URI = "mongodb://localhost:27017/"

    client = MongoClient(MONGO_URI)
    return client['tennisDB']

# Esto se agrega para que muchos archivos pueden reutilizar la función crear_base()
if __name__ == "__main__":   
    # Obtener la base de datos
    db = crear_base()
    print("Base de datos 'tennisDB' creada.")
