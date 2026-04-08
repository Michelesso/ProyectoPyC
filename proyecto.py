import sqlite3

conexion = sqlite3.connect ("Atletismo.db")
cursor = conexion.cursor()

#INSERTAR REGISTRO

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (1, 'Salvador Jurado Maqueda', 'F', '17/11/2008'),)
import sqlite3

conexion = sqlite3.connect("Atletismo.db")
cursor = conexion.cursor()

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (1, 'Salvador Jurado Maqueda', 'F', '17/11/2008'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (2, 'Michel Esso Reina', 'M', '19/10/2008'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (3, 'Paco Rodriguez Arroyo', 'M', '29/12/2008'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (4, 'Alejandro Frika', 'M', '10/01/1804'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (5, 'Juan Antonio Carracedo Pulido', 'M', '03/04/1965'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (6, 'David Torres Martin', 'M', '02/05/2006'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (7, 'Lucia Jurado Maqueda', 'F', '17/08/2010'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (8, 'Mercedes Jurado Maqueda', 'F', '17/08/2010'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (9, 'Lola Jurado Maqueda', 'F', '17/08/2010'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (10, 'Antonio Mateos Garcia', 'M', '10/01/2008'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (11, 'Jesus Cruz Gallego', 'M', '29/02/2007'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (12, 'Pastora Caro', 'F', '09/11/2007'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (13, 'Aitana Savedra', 'F', '17/03/2007'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (14, 'Luis Manzanedo Manzanedo', 'M', '02/09/1966'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (15, 'Pablo Miranda Franco', 'F', '16/09/2006'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (16, 'Daniela Moriano Sanchez', 'F', '07/07/2006'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (17, 'Daniela Ponce Castañeda', 'F', '18/10/2008'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (18, 'Ana Ortega y Gassette', 'F', '12/03/2004'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (19, 'Ana Maria Castañeda Zafra', 'F', '01/01/1986'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (20, 'Lola Maqueda Torres', 'F', '05/06/1922'),)

cursor.execute('''INSERT INTO atletas (id_atleta, nombre_completo, genero, fecha_nacimiento) VALUES (?,?,?, ?)
''', (21, 'Jose Manuel Ponce Piña', 'M', '01/01/1986'),)

conexion.commit() # Confirma la transacción

print("Atleta insertado con éxito.")

conexion.close()





