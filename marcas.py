import sqlite3

def conectar():
    conexion = sqlite3.connect("Atletismo.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_tablas_y_datos():
    conexion = conectar()
    cursor = conexion.cursor()
    
    # 1. Crear tabla de Temporada 25/26
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temporada_actual (
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            id_atleta INTEGER,
            competicion TEXT,
            prueba TEXT,
            marca TEXT,
            FOREIGN KEY (id_atleta) REFERENCES Atletas(id_atleta)
        )
    ''')

    # 2. Insertar registros 1 a 1 (3 por cada uno de los 21 atletas)
    cursor.execute("SELECT count(*) FROM temporada_actual")
    if cursor.fetchone()[0] == 0:
        
        # --- ATLETAS DE 100m LISOS (ID 1 al 7) ---
        # Atleta 1
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (1, 'Control 1', '100m lisos', '11.20s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (1, 'Control 2', '100m lisos', '11.05s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (1, 'Campeonato de España', '100m lisos', '10.85s')")
        # Atleta 2
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (2, 'Control 1', '100m lisos', '11.40s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (2, 'Control 2', '100m lisos', '11.25s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (2, 'Campeonato de España', '100m lisos', '11.02s')")
        # Atleta 3
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (3, 'Control 1', '100m lisos', '11.30s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (3, 'Control 2', '100m lisos', '11.15s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (3, 'Campeonato de España', '100m lisos', '10.95s')")
        # Atleta 4
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (4, 'Control 1', '100m lisos', '11.50s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (4, 'Control 2', '100m lisos', '11.35s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (4, 'Campeonato de España', '100m lisos', '11.15s')")
        # Atleta 5
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (5, 'Control 1', '100m lisos', '11.00s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (5, 'Control 2', '100m lisos', '10.90s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (5, 'Campeonato de España', '100m lisos', '10.70s')")
        # Atleta 6
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (6, 'Control 1', '100m lisos', '11.60s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (6, 'Control 2', '100m lisos', '11.50s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (6, 'Campeonato de España', '100m lisos', '11.30s')")
        # Atleta 7
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (7, 'Control 1', '100m lisos', '12.40s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (7, 'Control 2', '100m lisos', '12.25s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (7, 'Campeonato de España', '100m lisos', '12.10s')")

        # --- ATLETAS DE 400m LISOS (ID 8 al 14) ---
        # Atleta 8
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (8, 'Control 1', '400m lisos', '49.50s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (8, 'Control 2', '400m lisos', '49.10s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (8, 'Campeonato de España', '400m lisos', '48.20s')")
        # Atleta 9
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (9, 'Control 1', '400m lisos', '50.30s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (9, 'Control 2', '400m lisos', '50.00s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (9, 'Campeonato de España', '400m lisos', '49.15s')")
        # Atleta 10
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (10, 'Control 1', '400m lisos', '49.00s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (10, 'Control 2', '400m lisos', '48.50s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (10, 'Campeonato de España', '400m lisos', '47.90s')")
        # Atleta 11
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (11, 'Control 1', '400m lisos', '51.20s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (11, 'Control 2', '400m lisos', '50.80s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (11, 'Campeonato de España', '400m lisos', '50.10s')")
        # Atleta 12
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (12, 'Control 1', '400m lisos', '53.50s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (12, 'Control 2', '400m lisos', '53.00s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (12, 'Campeonato de España', '400m lisos', '52.30s')")
        # Atleta 13
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (13, 'Control 1', '400m lisos', '52.10s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (13, 'Control 2', '400m lisos', '51.80s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (13, 'Campeonato de España', '400m lisos', '51.05s')")
        # Atleta 14
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (14, 'Control 1', '400m lisos', '49.80s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (14, 'Control 2', '400m lisos', '49.20s')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (14, 'Campeonato de España', '400m lisos', '48.55s')")

        # --- ATLETAS DE SALTO DE LONGITUD (ID 15 al 21) ---
        # Atleta 15
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (15, 'Control 1', 'Salto longitud', '6.90m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (15, 'Control 2', 'Salto longitud', '7.02m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (15, 'Campeonato de España', 'Salto longitud', '7.15m')")
        # Atleta 16
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (16, 'Control 1', 'Salto longitud', '6.70m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (16, 'Control 2', 'Salto longitud', '6.82m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (16, 'Campeonato de España', 'Salto longitud', '6.90m')")
        # Atleta 17
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (17, 'Control 1', 'Salto longitud', '6.30m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (17, 'Control 2', 'Salto longitud', '6.45m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (17, 'Campeonato de España', 'Salto longitud', '6.55m')")
        # Atleta 18
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (18, 'Control 1', 'Salto longitud', '7.10m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (18, 'Control 2', 'Salto longitud', '7.22m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (18, 'Campeonato de España', 'Salto longitud', '7.30m')")
        # Atleta 19
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (19, 'Control 1', 'Salto longitud', '6.50m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (19, 'Control 2', 'Salto longitud', '6.65m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (19, 'Campeonato de España', 'Salto longitud', '6.75m')")
        # Atleta 20
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (20, 'Control 1', 'Salto longitud', '5.50m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (20, 'Control 2', 'Salto longitud', '5.65m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (20, 'Campeonato de España', 'Salto longitud', '5.80m')")
        # Atleta 21
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (21, 'Control 1', 'Salto longitud', '6.80m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (21, 'Control 2', 'Salto longitud', '6.95m')")
        cursor.execute("INSERT INTO temporada_actual (id_atleta, competicion, prueba, marca) VALUES (21, 'Campeonato de España', 'Salto longitud', '7.05m')")

        conexion.commit()
        print("Datos de temporada 25/26 insertados 1 a 1 correctamente.")
    
    conexion.close()

if __name__ == "__main__":
    inicializar_tablas_y_datos()