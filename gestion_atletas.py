import sqlite3

def conectar():
    conexion = sqlite3.connect("Atletismo.db")
    # ACTIVAR CLAVES FORÁNEAS: Vital para el punto 4 del proyecto
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

# --- OPERACIONES DE LECTURA (READ) ---
def listar_records_con_nombres():
    """Ejemplo de relación entre tablas usando JOIN"""
    conn = conectar()
    cursor = conn.cursor()
    query = '''
        SELECT r.prueba, a.nombre_completo, r.marca_record 
        FROM records_trotasierra r
        JOIN Atletas a ON r.id_atleta = a.id_atleta
    '''
    cursor.execute(query)
    for r in cursor.fetchall():
        print(f"Prueba: {r[0]} | Atleta: {r[1]} | Récord: {r[2]}")
    conn.close()

# --- OPERACIONES DE ACTUALIZACIÓN (UPDATE) ---
def actualizar_marca_atleta():
    """Punto 3: Modificar registros existentes"""
    id_m = input("ID de la marca a modificar: ")
    nuevo_tiempo = input("Nuevo tiempo/marca (ej: 10.50s): ")
    
    conn = conectar()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE marcas_campeonato SET marca_tiempo = ? WHERE id_marca = ?", 
                       (nuevo_tiempo, id_m))
        conn.commit() # Control de transacción
        print("Marca actualizada correctamente.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

# --- OPERACIONES DE ELIMINACIÓN (DELETE) ---
def eliminar_atleta():
    """Punto 3: Eliminar registros"""
    id_a = input("ID del atleta a eliminar: ")
    conn = conectar()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Atletas WHERE id_atleta = ?", (id_a,))
        conn.commit()
        print("Atleta (y sus marcas relacionadas) eliminado.")
    except Exception as e:
        conn.rollback()
        print(f"Error al eliminar: {e}")
    finally:
        conn.close()

# --- MENÚ INTERACTIVO (Punto 5) ---
def menu_principal():
    while True:
        print("\n--- SISTEMA DE GESTIÓN TROTASIERRA ---")
        print("1. Ver Récords del Club (READ con JOIN)")
        print("2. Actualizar una marca (UPDATE)")
        print("3. Eliminar un atleta (DELETE)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            listar_records_con_nombres()
        elif opcion == "2":
            actualizar_marca_atleta()
        elif opcion == "3":
            eliminar_atleta()
        elif opcion == "4":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    menu_principal()