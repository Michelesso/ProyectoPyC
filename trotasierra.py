import sqlite3

# 1. Conexión
conexion = sqlite3.connect("Atletismo.db")
cursor = conexion.cursor()

# Activar claves foráneas para mantener la relación entre tablas
cursor.execute("PRAGMA foreign_keys = ON")

# 2. Crear la tabla de Records del Club
cursor.execute('''
CREATE TABLE IF NOT EXISTS records_trotasierra (
    id_record INTEGER PRIMARY KEY AUTOINCREMENT,
    prueba TEXT NOT NULL,
    id_atleta INTEGER,
    marca_record TEXT NOT NULL,
    FOREIGN KEY (id_atleta) REFERENCES Atletas(id_atleta)
)
''')

try:
    # 3. Lógica para obtener los mejores (Records) basándonos en tu tabla de campeonatos
    # Buscamos la marca mínima (mejor tiempo) para carreras y máxima para saltos.
    
    # Definimos los mejores registros según los datos que insertamos antes:
    # 100m lisos: El mejor es el Atleta 5 (10.70s)
    # 400m lisos: El mejor es el Atleta 10 (47.90s)
    # Salto de longitud: El mejor es el Atleta 18 (7.30m)
    
    datos_records = [
        ('100m lisos', 5, '10.70s'),
        ('400m lisos', 10, '47.90s'),
        ('Salto de longitud', 18, '7.30m')
    ]

    # 4. Inserción de los records (Operación CREATE)
    cursor.executemany('''
        INSERT INTO records_trotasierra (prueba, id_atleta, marca_record) 
        VALUES (?, ?, ?)
    ''', datos_records)

    # 5. Confirmar la transacción
    conexion.commit()
    print("Tabla 'records_trotasierra' creada. Se han asignado los mejores atletas del club.")

except Exception as e:
    # 6. Rollback si hay error
    conexion.rollback()
    print(f"Error al procesar los records: {e}")

finally:
    # 7. Cerrar conexión
    conexion.close()