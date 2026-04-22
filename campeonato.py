import sqlite3

# 1. Conexión a la base de datos
conexion = sqlite3.connect("Atletismo.db")
cursor = conexion.cursor()

# ACTIVAR CLAVES FORÁNEAS (Importante para que la relación funcione)
cursor.execute("PRAGMA foreign_keys = ON")

# 2. Crear la tabla marcas_campeonato si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS marcas_campeonato (
    id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
    id_atleta INTEGER,
    prueba TEXT NOT NULL,
    marca_tiempo TEXT NOT NULL,
    lugar TEXT,
    fecha TEXT,
    FOREIGN KEY (id_atleta) REFERENCES Atletas(id_atleta)
)
''')

# 3. Lista con todos mis datos (Atletas del 1 al 21)

datos_marcas = [
    # 100m lisos
    (1, '100m lisos', '10.85s', 'Madrid', '2025-06-12'),
    (2, '100m lisos', '11.02s', 'Sevilla', '2025-06-12'),
    (3, '100m lisos', '10.95s', 'Barcelona', '2025-06-12'),
    (4, '100m lisos', '11.15s', 'Valencia', '2025-06-12'),
    (5, '100m lisos', '10.70s', 'Madrid', '2025-06-12'),
    (6, '100m lisos', '11.30s', 'Malaga', '2025-06-12'),
    (7, '100m lisos', '12.10s', 'Sevilla', '2025-06-12'),
    # 400m lisos
    (8, '400m lisos', '48.20s', 'Antequera', '2025-07-05'),
    (9, '400m lisos', '49.15s', 'Madrid', '2025-07-05'),
    (10, '400m lisos', '47.90s', 'Barcelona', '2025-07-05'),
    (11, '400m lisos', '50.10s', 'Valencia', '2025-07-05'),
    (12, '400m lisos', '52.30s', 'Sevilla', '2025-07-05'),
    (13, '400m lisos', '51.05s', 'Madrid', '2025-07-05'),
    (14, '400m lisos', '48.55s', 'Malaga', '2025-07-05'),
    # Salto de longitud
    (15, 'Salto de longitud', '7.15m', 'Valencia', '2025-05-20'),
    (16, 'Salto de longitud', '6.90m', 'Barcelona', '2025-05-20'),
    (17, 'Salto de longitud', '6.55m', 'Madrid', '2025-05-20'),
    (18, 'Salto de longitud', '7.30m', 'Antequera', '2025-05-20'),
    (19, 'Salto de longitud', '6.75m', 'Sevilla', '2025-05-20'),
    (20, 'Salto de longitud', '5.80m', 'Malaga', '2025-05-20'),
    (21, 'Salto de longitud', '7.05m', 'Madrid', '2025-05-20')
]

try:
    # 4. Inserción masiva corregida (executemany con 2 argumentos)
    cursor.executemany('''
        INSERT INTO marcas_campeonato (id_atleta, prueba, marca_tiempo, lugar, fecha) 
        VALUES (?, ?, ?, ?, ?)
    ''', datos_marcas)

    # 5. Confirmar transacción (COMMIT)
    conexion.commit()
    print(f"Éxito: Se han insertado {len(datos_marcas)} marcas correctamente.")

except Exception as e:
    # 6. Revertir en caso de error (ROLLBACK)
    conexion.rollback()
    print(f"Error al insertar datos: {e}")

finally:
    # 7. Cerrar conexión
    conexion.close()