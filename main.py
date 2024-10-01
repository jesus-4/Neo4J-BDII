from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona

driver = None
def crear_nodos_ejemplo():
    with driver.session() as session:
        # Crear Zonas
        session.execute_write(crear_zona, "Z1", "Centro", "Urbana", "50 km²", "Agua, Electricidad, Transporte")
        session.execute_write(crear_zona, "Z2", "Nuevo centro", "Urbana", "100 km²", "Agua, Electricidad")

        # Crear Terrenos
        session.execute_write(crear_terreno, "T1", "Chilecito", 50000, 1500, "En Venta", "Residencial", "2024-09-01", "Terreno con vista al parque")
        session.execute_write(crear_terreno, "T2", "Cordoba", 75000, 2000, "En Venta", "Comercial", "2024-09-10", "Terreno ideal para negocios")

        # Crear Propietarios
        session.execute_write(crear_propietario, "P1", "Claramonte Jesus", "jClaramonte@example.com", "123456789")
        session.execute_write(crear_propietario, "P2", "María García", "maria@example.com", "987654321")

        # Crear Empleados
        session.execute_write(crear_empleado, "E1", "Javier Cordoba", "Z1", "Jcordoba@example.com", "555123456")
        session.execute_write(crear_empleado, "E2", "Luis Martínez", "Z2", "luis@example.com", "555654321")

        # Crear Clientes
        session.execute_write(crear_cliente, "C1", "Juan Pérez", "juan@example.com", "666123456", "Z1", 60000)
        session.execute_write(crear_cliente, "C2", "Laura Sánchez", "laura@example.com", "666654321", "Z2", 80000)

def crear_relaciones_ejemplo():
    with driver.session() as session:
        # Asociar Terrenos a Zonas
        session.execute_write(asociar_terreno_zona, "T1", "Z1")
        session.execute_write(asociar_terreno_zona, "T2", "Z2")

        # Asignar Empleados a Zonas
        session.execute_write(asignar_empleado_zona, "E1", "Z1")
        session.execute_write(asignar_empleado_zona, "E2", "Z2")

        # Vincular Terrenos a Propietarios
        session.execute_write(vincular_terreno_propietario, "T1", "P1")
        session.execute_write(vincular_terreno_propietario, "T2", "P2")

        # Clientes interesados en Terrenos
        session.execute_write(cliente_interesado_en_terreno, "C1", "T1")
        session.execute_write(cliente_interesado_en_terreno, "C2", "T2")
        session.execute_write(cliente_interesado_en_terreno, "C2", "T1")

        # Clientes interactúan con Empleados
        session.execute_write(cliente_interactua_empleado, "C1", "E1")
        session.execute_write(cliente_interactua_empleado, "C2", "E2")

def cerrar_conexion():
    if driver:
        driver.close()
        print("Conexión cerrada.")

def main():
    global driver

    # Datos de conexión
    uri = "neo4j+s://6844ddef.databases.neo4j.io"  # Asegúrate de que esta línea es correcta
    usuario = "neo4j"
    password = "rcXRNRxLuK8jIMoc3PzNBUaWyS3THXe8v9ybZdIoA88"  # Asegúrate de que esta línea tenga la contraseña correcta

    # Crear el driver
    try:
        driver = GraphDatabase.driver(uri, auth=(usuario, password))

        print("Conexión exitosa a Neo4j.")

        crear_nodos_ejemplo()
        crear_relaciones_ejemplo()

        print("Nodos y relaciones creadas exitosamente.")
    except Neo4jError as error:
        print(f"Ocurrió un error al conectarse a Neo4j: {error}")
    finally:
        cerrar_conexion()

if __name__ == "__main__":
    main()