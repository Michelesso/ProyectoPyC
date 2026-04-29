import sqlite3

def conectar():
    conexion = sqlite3.connect("Atletismo.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_tablas_y_datos():
    conexion = conectar()
    cursor = conexion.cursor()
    # Solo creamos las tablas si no existen, NO insertamos nada aquí.
    # Las marcas reales vienen de tu archivo marcas.py
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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records_trotasierra (
            id_record INTEGER PRIMARY KEY AUTOINCREMENT,
            id_atleta INTEGER,
            prueba TEXT,
            marca_record TEXT,
            FOREIGN KEY (id_atleta) REFERENCES Atletas(id_atleta)
        )
    ''')
    conexion.commit()
    conexion.close()

# --- OPERACIONES DE LECTURA (Aquí está el JOIN para el nombre) ---

def buscar_temporada_atleta():
    id_a = input("\nIntroduce el ID del atleta para ver su temporada: ")
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Esta consulta une las dos tablas para darte el NOMBRE y las MARCAS REALES
    cursor.execute('''
        SELECT a.nombre_completo, t.competicion, t.prueba, t.marca 
        FROM Atletas a
        JOIN temporada_actual t ON a.id_atleta = t.id_atleta
        WHERE a.id_atleta = ?
    ''', (id_a,))
    
    resultados = cursor.fetchall()
    
    if resultados:
        nombre = resultados[0][0]
        print(f"\n>>> INSPECCIONANDO A: {nombre} (ID: {id_a})")
        print("-" * 65)
        for r in resultados:
            # r[1]: Competición, r[2]: Prueba, r[3]: Marca (las de marcas.py)
            print(f"Evento: {r[1]:<20} | Prueba: {r[2]:<15} | Marca: {r[3]}")
        print("-" * 65)
    else:
        print(f">>> No hay datos. Asegúrate de haber ejecutado 'marcas.py' primero.")
    conexion.close()

def listar_marcas_campeonato():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT m.id_marca, a.nombre_completo, m.prueba, m.marca_tiempo 
        FROM marcas_campeonato m
        JOIN Atletas a ON m.id_atleta = a.id_atleta
    ''')
    resultados = cursor.fetchall()
    print("\n--- MARCAS CAMPEONATO DE ESPAÑA 2025 ---")
    for m in resultados:
        print(f"ID: {m[0]} | Atleta: {m[1]} | Prueba: {m[2]} | Marca: {m[3]}")
    conexion.close()

def listar_records_club():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT r.prueba, a.nombre_completo, r.marca_record 
        FROM records_trotasierra r
        JOIN Atletas a ON r.id_atleta = a.id_atleta
    ''')
    resultados = cursor.fetchall()
    print("\n--- RÉCORDS HISTÓRICOS TROTASIERRA ---")
    for r in resultados:
        print(f"Prueba: {r[0]:<18} | Atleta: {r[1]:<25} | Récord: {r[2]}")
    conexion.close()

# --- OPERACIONES CRUD ---

def actualizar_marca_campeonato():
    id_m = input("\nID de la marca de Campeonato a modificar: ")
    nuevo_t = input("Nueva marca (ej: 10.45s): ")
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE marcas_campeonato SET marca_tiempo = ? WHERE id_marca = ?", (nuevo_t, id_m))
        conexion.commit()
        print(">>> Registro actualizado.")
    except Exception as e:
        conexion.rollback()
        print(f"Error: {e}")
    finally:
        conexion.close()

def eliminar_atleta():
    id_a = input("\nID del atleta a eliminar: ")
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Atletas WHERE id_atleta = ?", (id_a,))
        conexion.commit()
        print(">>> Atleta eliminado.")
    except Exception as e:
        conexion.rollback()
        print(f"Error: {e}")
    finally:
        conexion.close()

# --- MENÚ ---

def menu_principal():
    inicializar_tablas_y_datos()
    while True:
        print("\n========================================")
        print("   SISTEMA DE GESTIÓN TROTASIERRA")
        print("========================================")
        print("1. Ver Récords Club")
        print("2. Ver Marcas Campeonato España 2025")
        print("3. Inspeccionar Temporada de un atleta")
        print("4. Actualizar marca de campeonato (UPDATE)")
        print("5. Eliminar atleta (DELETE)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": listar_records_club()
        elif opcion == "2": listar_marcas_campeonato()
        elif opcion == "3": buscar_temporada_atleta()
        elif opcion == "4": actualizar_marca_campeonato()
        elif opcion == "5": eliminar_atleta()
        elif opcion == "6": break

if __name__ == "__main__":
    menu_principal()