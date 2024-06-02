import csv
from configuracion import crear_base

def insertar_partidos_desde_csv(nombre_archivo_csv):
    db = crear_base()
    coleccion = db['partidos']
    
    # Leer archivo cssv
    with open(nombre_archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            partido = {
                "Tournament": fila["Tournament"],
                "Date": fila["Date"],
                "Series": fila["Series"],
                "Court": fila["Court"],
                "Surface": fila["Surface"],
                "Round": fila["Round"],
                "Best of": int(fila["Best of"]),
                "Player_1": fila["Player_1"],
                "Player_2": fila["Player_2"],
                "Winner": fila["Winner"],
                "Rank_1": int(fila["Rank_1"]),
                "Rank_2": int(fila["Rank_2"]),
                "Pts_1": int(fila["Pts_1"]),
                "Pts_2": int(fila["Pts_2"]),
                "Odd_1": float(fila["Odd_1"]),
                "Odd_2": float(fila["Odd_2"]),
                "score": fila["score"]
            }
            coleccion.insert_one(partido)
        print("Datos ingresados con exito!")
if __name__ == "__main__":
    nombre_archivo_csv = 'atp_tennis.csv'
    insertar_partidos_desde_csv(nombre_archivo_csv)
