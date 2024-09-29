
from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona

driver = None
def crear_nodos_ejemplo():
    with driver.session() as session:
        # Crear Zonas
        session.write_transaction(crear_zona, "Z1", "Centro", "Urbana", "50 km²", "Agua, Electricidad, Transporte")
        session.write_transaction(crear_zona, "Z2", "Norte", "Rural", "100 km²", "Agua, Electricidad")

        # Crear Terrenos
        session.write_transaction(crear_terreno, "T1", "Ciudad XYZ", 50000, 1500, "Disponible", "Residencial", "2024-09-01", "Terreno con vista al parque")
        session.write_transaction(crear_terreno, "T2", "Ciudad ABC", 75000, 2000, "En Venta", "Comercial", "2024-09-10", "Terreno ideal para negocios")

        # Crear Propietarios
        session.write_transaction(crear_propietario, "P1", "Carlos López", {"email": "carlos@example.com", "tel": "123456789"})
        session.write_transaction(crear_propietario, "P2", "María García", {"email": "maria@example.com", "tel": "987654321"})

        # Crear Empleados
        session.write_transaction(crear_empleado, "E1", "Ana Torres", "Z1", {"email": "ana@example.com", "tel": "555123456"})
        session.write_transaction(crear_empleado, "E2", "Luis Martínez", "Z2", {"email": "luis@example.com", "tel": "555654321"})

        # Crear Clientes
        session.write_transaction(crear_cliente, "C1", "Juan Pérez", {"email": "juan@example.com", "tel": "666123456"}, {"zonas": ["Z1"], "presupuesto": 60000}, 60000)
        session.write_transaction(crear_cliente, "C2", "Laura Sánchez", {"email": "laura@example.com", "tel": "666654321"}, {"zonas": ["Z2"], "presupuesto": 80000}, 80000)

def crear_relaciones_ejemplo():
    with driver.session() as session:
        # Asociar Terrenos a Zonas
        session.write_transaction(asociar_terreno_zona, "T1", "Z1")
        session.write_transaction(asociar_terreno_zona, "T2", "Z2")

        # Asignar Empleados a Zonas
        session.write_transaction(asignar_empleado_zona, "E1", "Z1")
        session.write_transaction(asignar_empleado_zona, "E2", "Z2")

        # Vincular Terrenos a Propietarios
        session.write_transaction(vincular_terreno_propietario, "T1", "P1")
        session.write_transaction(vincular_terreno_propietario, "T2", "P2")

        # Clientes interesados en Terrenos
        session.write_transaction(cliente_interesado_en_terreno, "C1", "T1")
        session.write_transaction(cliente_interesado_en_terreno, "C2", "T2")

        # Clientes interactúan con Empleados
        session.write_transaction(cliente_interactua_empleado, "C1", "E1")
        session.write_transaction(cliente_interactua_empleado, "C2", "E2")

def cerrar_conexion():
    driver.close()
    try:
        crear_nodos_ejemplo()
        crear_relaciones_ejemplo()
        print("Nodos y relaciones creados exitosamente.")
    except Neo4jError as error:
        print(f"Ocurrió un error al interactuar con Neo4j: {error}")
    finally:
        cerrar_conexion()

def main():
    global driver

    # Datos de conexión
    uri = "neo4j+s://6844ddef.databases.neo4j.io:7687"  # Asegúrate de que esta línea es correcta
    usuario = "neo4j"
    password = "rcXRNRxLuK8jIMoc3PzNBUaWyS3THXe8v9ybZdIoA88"  # Asegúrate de que esta línea tenga la contraseña correcta

    # Crear el driver
    try:
        driver = GraphDatabase.driver(uri, auth=(usuario, password))

        # Aquí llamarías a tus funciones de creación de nodos y relaciones
        print("Conexión exitosa a Neo4j.")

    except Neo4jError as error:
        print(f"Ocurrió un error al conectarse a Neo4j: {error}")
    finally:
        cerrar_conexion()

if __name__ == "__main__":
    main()