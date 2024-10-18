from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona
from Qury import get_zone_by_id, get_terrenos_by_zone, get_propietario_by_terreno, get_terrenos_by_propietario,get_empleados_by_zone, get_clientes_by_terreno, get_terrenos_by_cliente, get_interacciones_cliente_empleado
from DAO import DAO


def crear_nodos_ejemplo(dao):

        # Crear Zonas
        dao.execute_write(crear_zona, "Z1", "Chilecito", "50 km²", "Agua, Electricidad, Transporte")
        dao.execute_write(crear_zona, "Z2", "Cordoba", "100 km²", "Agua, Electricidad")

        # Crear Terrenos
        dao.execute_write(crear_terreno, "T1", "Urbana","URL", 50000, 1500, "En Venta", "Residencial", "2024-09-01", "Terreno con vista al parque")
        dao.execute_write(crear_terreno, "T2", "Rural","URL", 75000, 2000, "En Venta", "Comercial", "2024-08-10", "Terreno ideal para negocios")
        dao.execute_write(crear_terreno, "T3", "Urbana","URL", 50000, 1500, "En Venta", "Residencial", "2024-07-01", "Terreno cerca de la plaza")
        dao.execute_write(crear_terreno, "T4", "Rural","URL", 75000, 2000, "En Venta", "Comercial", "2024-06-10", "Terreno cerca del lago")
        dao.execute_write(crear_terreno, "T5", "Urbana","URL", 50000, 1500, "En Venta", "Residencial", "2024-05-01", "Terreno con vista al cristo")
        dao.execute_write(crear_terreno, "T6", "Alcaldesa","URL", 75000, 2000, "En Venta", "Comercial", "2024-04-10", "Terreno ideal para contrunccion")

        # Crear Propietarios
        dao.execute_write(crear_propietario, "P1", "Claramonte Jesus", "jClaramonte@example.com", "123456789")
        dao.execute_write(crear_propietario, "P2", "María García", "maria@example.com", "987654321")
        dao.execute_write(crear_propietario, "P3", "Nicolas Junin", "NJ@example.com", "1236789")
        dao.execute_write(crear_propietario, "P4", "Mirta Gomez", "MG@example.com", "9874321")
        dao.execute_write(crear_propietario, "P5", "Franco Hernandez", "FH@example.com", "1256789")


        # Crear Empleados
        dao.execute_write(crear_empleado, "E1", "Javier Cordoba", "Z1", "Jcordoba@example.com", "555123456")
        dao.execute_write(crear_empleado, "E2", "Luis Martínez", "Z2", "luis@example.com", "555654321")

        # Crear Clientes
        dao.execute_write(crear_cliente, "C1", "Juan Pérez", "juan@example.com", "666123456", "Z1", 60000)
        dao.execute_write(crear_cliente, "C2", "Laura Sánchez", "laura@example.com", "666654321", "Z2", 80000)

def crear_relaciones_ejemplo(dao):

        # Asociar Terrenos a Zonas
        dao.execute_write(asociar_terreno_zona, "T1", "Z1")
        dao.execute_write(asociar_terreno_zona, "T2", "Z2")
        dao.execute_write(asociar_terreno_zona, "T3", "Z1")
        dao.execute_write(asociar_terreno_zona, "T4", "Z2")
        dao.execute_write(asociar_terreno_zona, "T5", "Z1")
        dao.execute_write(asociar_terreno_zona, "T6", "Z2")

        # Asignar Empleados a Zonas
        dao.execute_write(asignar_empleado_zona, "E1", "Z1")
        dao.execute_write(asignar_empleado_zona, "E2", "Z2")


        # Vincular Terrenos a Propietarios
        dao.execute_write(vincular_terreno_propietario, "T1", "P1")
        dao.execute_write(vincular_terreno_propietario, "T2", "P2")
        dao.execute_write(vincular_terreno_propietario, "T3", "P3")
        dao.execute_write(vincular_terreno_propietario, "T4", "P4")
        dao.execute_write(vincular_terreno_propietario, "T5", "P5")
        dao.execute_write(vincular_terreno_propietario, "T6", "P3")
        # Clientes interesados en Terrenos
        dao.execute_write(cliente_interesado_en_terreno, "C1", "T1")
        dao.execute_write(cliente_interesado_en_terreno, "C2", "T2")
        dao.execute_write(cliente_interesado_en_terreno, "C2", "T3")
        dao.execute_write(cliente_interesado_en_terreno, "C2", "T1")
        dao.execute_write(cliente_interesado_en_terreno, "C1", "T4")
        dao.execute_write(cliente_interesado_en_terreno, "C1", "T5")
        dao.execute_write(cliente_interesado_en_terreno, "C2", "T6")

        # Clientes interactúan con Empleados
        dao.execute_write(cliente_interactua_empleado, "C1", "E1")
        dao.execute_write(cliente_interactua_empleado, "C2", "E2")
        dao.execute_write(cliente_interactua_empleado, "C2", "E1")
        dao.execute_write(cliente_interactua_empleado, "C1", "E2")

def query_ejemplo(dao):
        print("zone_by_id")
        print(dao.execute_read(get_zone_by_id,"Z1"))
        #print("terrenos_by_zone")
        #print(dao.execute_read(get_terrenos_by_zone,"Z1"))
        #print("propietario_by_terreno")
        #print(dao.execute_read(get_propietario_by_terreno,"T1"))
        #print("terrenos_by_propietario")
        #print(dao.execute_read(get_terrenos_by_propietario,"P1"))
        print("empleados_by_zone")
        print(dao.execute_read(get_empleados_by_zone,"Z1"))
        print("clientes_by_terreno")
        print(dao.execute_read(get_clientes_by_terreno,"T1"))
        print("terrenos_by_cliente")
        print(dao.execute_read(get_terrenos_by_cliente,"C2"))
        #print("interacciones_cliente_empleado")
        #print(dao.execute_read(get_interacciones_cliente_empleado,"C1"))


def main():


    # Datos de conexión
    #uri = "neo4j+s://e4bf8799.databases.neo4j.io"
    #usuario = "neo4j"
    #password = "HovH_wY1maUy1PPJD6docxtZ99xC_dIUesqK-Z9-Jno"

    uri = "bolt://localhost:7687"
    usuario=""
    password = ""
    # Crear el driver
    try:
        dao = DAO(uri, usuario, password)
        print("Conexión exitosa a Neo4j.")

        #sacas estos comentarios para crear una ves y volvelos a comentar
        #crear_nodos_ejemplo(dao)
        #crear_relaciones_ejemplo(dao)
        query_ejemplo(dao)

        print("Nodos y relaciones creadas exitosamente.")
    except Neo4jError as error:
        print(f"Ocurrió un error al conectarse a Neo4j: {error}")
    finally:
        dao.close()

if __name__ == "__main__":
    main()