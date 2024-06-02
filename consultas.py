from configuracion import crear_base

def torneos():
    db = crear_base()
    coleccion = db['partidos']

    # Utilizar la función de agregación para obtener los torneos únicos
    pipeline = [
        {"$group": {"_id": "$Tournament"}}
    ]
    resultados = coleccion.aggregate(pipeline)

    # Mostrar los resultados por consola
    for resultado in resultados:
        print(resultado['_id'])

def torneos_ganador():
    db = crear_base()
    coleccion = db['partidos']

    # Utilizar la función de agregación para obtener los torneos únicos en los que Murray A. haya ganado
    pipeline = [
        {"$match": {"Winner": "Ito T."}},  # Filtrar documentos donde X jugador gano un partidos
        {"$group": {"_id": "$Tournament"}}  # Agrupar por torneo para obtener torneos únicos
    ]
    resultados = coleccion.aggregate(pipeline)

    # Mostrar los resultados por consola
    for resultado in resultados:
        print(resultado['_id'])


if __name__ == "__main__":
    # torneos()
    torneos_ganador()
