import sqlite3

def conectar():
    # Conexión simple, como en el PDF
    conexion = sqlite3.connect("Atletismo.db")
    return conexion

def inicializar_tablas_y_datos():
    conexion = conectar()
    cursor = conexion.cursor()
    # Crear tablas si no existen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temporada_actual (
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            id_atleta INTEGER,
            competicion TEXT,
            prueba TEXT,
            marca TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records_trotasierra (
            id_record INTEGER PRIMARY KEY AUTOINCREMENT,
            prueba TEXT,
            id_atleta INTEGER,
            marca_record TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

# --- CONSULTAS (READ) ---

def buscar_temporada_atleta():
    id_a = input("\nID del atleta: ")
    conexion = conectar()
    cursor = conexion.cursor()
    # JOIN para sacar el nombre del atleta
    cursor.execute('''
        SELECT a.nombre_completo, t.competicion, t.prueba, t.marca 
        FROM Atletas a
        JOIN temporada_actual t ON a.id_atleta = t.id_atleta
        WHERE a.id_atleta = ?
    ''', (id_a,))
    resultados = cursor.fetchall()
    if resultados:
        print(f"\n>>> TEMPORADA DE: {resultados[0][0]}")
        for r in resultados:
            print(f"Evento: {r[1]:<20} | {r[2]}: {r[3]}")
    else:
        print("No hay datos.")
    conexion.close()

def listar_marcas_campeonato():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT m.id_marca, a.nombre_completo, m.prueba, m.marca_tiempo 
        FROM marcas_campeonato m
        JOIN Atletas a ON m.id_atleta = a.id_atleta
    ''')
    for m in cursor.fetchall():
        print(f"ID: {m[0]} | Atleta: {m[1]:<25} | {m[2]}: {m[3]}")
    conexion.close()

def listar_records_club():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT r.prueba, a.nombre_completo, r.marca_record 
        FROM records_trotasierra r
        JOIN Atletas a ON r.id_atleta = a.id_atleta
    ''')
    print("\n--- RÉCORDS DEL CLUB ---")
    for r in cursor.fetchall():
        print(f"{r[0]:<18} | {r[1]:<25} | Récord: {r[2]}")
    conexion.close()

# --- ACTUALIZAR (UPDATE) + LÓGICA DE RÉCORD ---

def actualizar_marca_campeonato():
    id_m = input("\nID de la marca a modificar: ")
    nueva_m = input("Nueva marca (ej: 10.40s): ")
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        
        # 1. Ver qué prueba es y quién es el atleta
        cursor.execute("SELECT id_atleta, prueba FROM marcas_campeonato WHERE id_marca = ?", (id_m,))
        res = cursor.fetchone()
        if not res: return
        id_atleta, prueba = res

        # 2. Actualizar la marca personal
        cursor.execute("UPDATE marcas_campeonato SET marca_tiempo = ? WHERE id_marca = ?", (nueva_m, id_m))

        # 3. Lógica de Récord: comparar números
        cursor.execute("SELECT marca_record FROM records_trotasierra WHERE prueba = ?", (prueba,))
        rec = cursor.fetchone()
        if rec:
            v_nueva = float(nueva_m.replace('s','').replace('m',''))
            v_vieja = float(rec[0].replace('s','').replace('m',''))
            
            es_mejor = False
            if 's' in nueva_m and v_nueva < v_vieja: es_mejor = True
            elif 'm' in nueva_m and v_nueva > v_vieja: es_mejor = True

            if es_mejor:
                cursor.execute("UPDATE records_trotasierra SET marca_record = ?, id_atleta = ? WHERE prueba = ?", 
                               (nueva_m, id_atleta, prueba))
                print("¡SE HA BATIDO UN RÉCORD DEL CLUB!")

        conexion.commit()
        print("Datos actualizados.")
    except:
        conexion.rollback()
    finally:
        conexion.close()

# --- ELIMINAR (DELETE) ---

def eliminar_atleta():
    id_a = input("\nID del atleta a eliminar: ")
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        # Borramos sus datos de todas las tablas una por una (Borrado manual)
        cursor.execute("DELETE FROM temporada_actual WHERE id_atleta = ?", (id_a,))
        cursor.execute("DELETE FROM marcas_campeonato WHERE id_atleta = ?", (id_a,))
        cursor.execute("DELETE FROM records_trotasierra WHERE id_atleta = ?", (id_a,))
        cursor.execute("DELETE FROM Atletas WHERE id_atleta = ?", (id_a,))
        
        conexion.commit()
        print(f"Atleta {id_a} y todas sus marcas eliminados.")
    except:
        conexion.rollback()
    finally:
        conexion.close()

# --- MENÚ ---

def menu_principal():
    inicializar_tablas_y_datos()
    while True:
        print("\n" + "="*40)
        print("   GESTIÓN CLUB TROTASIERRA")
        print("="*40)
        print("1. Ver Récords Club")
        print("2. Ver Marcas Campeonato")
        print("3. Ver Temporada de Atleta")
        print("4. Actualizar marca")
        print("5. Eliminar atleta")
        print("6. Salir")
        
        op = input("\nOpción: ")
        if op == "1": listar_records_club()
        elif op == "2": listar_marcas_campeonato()
        elif op == "3": buscar_temporada_atleta()
        elif op == "4": actualizar_marca_campeonato()
        elif op == "5": eliminar_atleta()
        elif op == "6": break

if __name__ == "__main__":
    menu_principal()