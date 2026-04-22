import sqlite3

conexion = sqlite3.connect("Atletismo.db")
cursor = conexion.cursor()

# 1. Crear la tabla de Categorías
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL,
    edad_min INTEGER,
    edad_max INTEGER
)
''')


cursor.executemany('''
    INSERT INTO categorias (nombre_categoria, edad_min, edad_max) 
    VALUES (?, ?, ?)
''', [
    ('Sub-20', 18, 19),
    ('Sub-23', 20, 22),
    ('Absoluto', 23, 34),
    ('Master', 35, 100)
])

conexion.commit()
print("Tabla 'categorias' creada e insertada con éxito.")

conexion.close()