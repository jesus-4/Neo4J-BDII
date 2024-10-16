from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona

class DAO:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        if self.driver:
            self.driver.close()
            print("Conexión cerrada.")

    def execute_write(self, func, *args):
        with self.driver.session() as session:
            return session.execute_write(func, *args)

    def execute_read(self, func, *args):
        with self.driver.session() as session:
            return session.execute_read(func, *args)


def crear_nodos_ejemplo(session):

        # Crear Zonas
        session.execute_write(crear_zona, "Z1", "URL", "Chilecito", "50 km²", "Agua, Electricidad, Transporte")
        session.execute_write(crear_zona, "Z2", "URL", "Cordoba", "100 km²", "Agua, Electricidad")
        session.execute_write(crear_zona, "Z1", "URL", "Chilecito", "150 km²", "Agua, Electricidad, Transporte")
        session.execute_write(crear_zona, "Z2", "URL", "Cordoba", "200 km²", "Agua, Electricidad")
        session.execute_write(crear_zona, "Z1", "URL", "Chilecito", "75 km²", "Agua, Electricidad, Transporte")
        session.execute_write(crear_zona, "Z3", "URL", "Cordoba", "120 km²", "Agua, Electricidad")


        # Crear Terrenos
        session.execute_write(crear_terreno, "T1", "Urbana", 50000, 1500, "En Venta", "Residencial", "2024-09-01", "Terreno con vista al parque")
        session.execute_write(crear_terreno, "T2", "Rural", 75000, 2000, "En Venta", "Comercial", "2024-08-10", "Terreno ideal para negocios")
        session.execute_write(crear_terreno, "T3", "Rural", 50000, 1500, "En Venta", "Residencial", "2024-07-01", "Terreno cerca de la plaza")
        session.execute_write(crear_terreno, "T4", "Rural", 75000, 2000, "En Venta", "Comercial", "2024-06-10", "Terreno cerca del lago")
        session.execute_write(crear_terreno, "T5", "Rural", 50000, 1500, "En Venta", "Residencial", "2024-05-01", "Terreno con vista al cristo")
        session.execute_write(crear_terreno, "T6", "Rural", 75000, 2000, "En Venta", "Comercial", "2024-04-10", "Terreno ideal para contrunccion")

        # Crear Propietarios
        session.execute_write(crear_propietario, "P1", "Claramonte Jesus", "jClaramonte@example.com", "123456789")
        session.execute_write(crear_propietario, "P2", "María García", "maria@example.com", "987654321")
        session.execute_write(crear_propietario, "P3", "Nicolas Junin", "NJ@example.com", "1236789")
        session.execute_write(crear_propietario, "P4", "Mirta Gomez", "MG@example.com", "9874321")
        session.execute_write(crear_propietario, "P5", "Franco Hernandez", "FH@example.com", "1256789")


        # Crear Empleados
        session.execute_write(crear_empleado, "E1", "Javier Cordoba", "Z1", "Jcordoba@example.com", "555123456")
        session.execute_write(crear_empleado, "E2", "Luis Martínez", "Z2", "luis@example.com", "555654321")

        # Crear Clientes
        session.execute_write(crear_cliente, "C1", "Juan Pérez", "juan@example.com", "666123456", "Z1", 60000)
        session.execute_write(crear_cliente, "C2", "Laura Sánchez", "laura@example.com", "666654321", "Z2", 80000)

def crear_relaciones_ejemplo(session):

        # Asociar Terrenos a Zonas
        session.execute_write(asociar_terreno_zona, "T1", "Z1")
        session.execute_write(asociar_terreno_zona, "T2", "Z2")
        session.execute_write(asociar_terreno_zona, "T3", "Z1")
        session.execute_write(asociar_terreno_zona, "T4", "Z2")
        session.execute_write(asociar_terreno_zona, "T5", "Z1")
        session.execute_write(asociar_terreno_zona, "T6", "Z3")

        # Asignar Empleados a Zonas
        session.execute_write(asignar_empleado_zona, "E1", "Z1")
        session.execute_write(asignar_empleado_zona, "E2", "Z2")
        session.execute_write(asignar_empleado_zona, "E1", "Z3")


        # Vincular Terrenos a Propietarios
        session.execute_write(vincular_terreno_propietario, "T1", "P1")
        session.execute_write(vincular_terreno_propietario, "T2", "P2")
        session.execute_write(vincular_terreno_propietario, "T3", "P3")
        session.execute_write(vincular_terreno_propietario, "T4", "P4")
        session.execute_write(vincular_terreno_propietario, "T5", "P5")
        session.execute_write(vincular_terreno_propietario, "T6", "P3")
        # Clientes interesados en Terrenos
        session.execute_write(cliente_interesado_en_terreno, "C1", "T1")
        session.execute_write(cliente_interesado_en_terreno, "C2", "T2")
        session.execute_write(cliente_interesado_en_terreno, "C2", "T3")
        session.execute_write(cliente_interesado_en_terreno, "C2", "T1")
        session.execute_write(cliente_interesado_en_terreno, "C1", "T4")
        session.execute_write(cliente_interesado_en_terreno, "C1", "T5")
        session.execute_write(cliente_interesado_en_terreno, "C2", "T6")

        # Clientes interactúan con Empleados
        session.execute_write(cliente_interactua_empleado, "C1", "E1")
        session.execute_write(cliente_interactua_empleado, "C2", "E2")
        session.execute_write(cliente_interactua_empleado, "C2", "E1")
        session.execute_write(cliente_interactua_empleado, "C1", "E2")




def main():


    # Datos de conexión
    uri = "neo4j+s://e4bf8799.databases.neo4j.io"
    usuario = "neo4j"
    password = "HovH_wY1maUy1PPJD6docxtZ99xC_dIUesqK-Z9-Jno"

    # Crear el driver
    try:
        dao = DAO(uri, usuario, password)
        print("Conexión exitosa a Neo4j.")

        crear_nodos_ejemplo(dao)
        crear_relaciones_ejemplo(dao)

        print("Nodos y relaciones creadas exitosamente.")
    except Neo4jError as error:
        print(f"Ocurrió un error al conectarse a Neo4j: {error}")
    finally:
        dao.close()

if __name__ == "__main__":
    main()