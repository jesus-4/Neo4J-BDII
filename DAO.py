from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario,asociar_zona_provincia
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona,crear_provincia
from Query import get_zonas_provincias,get_terrenos_por_zona,get_propietarios_terrenos,get_empleados_por_zona,get_clientes_by_terreno,get_sentenciageneral,get_consultageneral
from DAO import DAO

def crear_nodos_ejemplo(dao):

        # Crear Zonas
        dao.execute_write(crear_zona, "Z1", "Chilecito", "350 km²")
        dao.execute_write(crear_zona, "Z2", "Chamical", "250 km²")
        dao.execute_write(crear_zona, "Z3", "Carlos Paz", "900 km²")
        dao.execute_write(crear_zona, "Z4", "Villa Soto", "650 km²")
        dao.execute_write(crear_zona, "Z5", "Merlo", "350 km²")
        dao.execute_write(crear_zona, "Z6", "La Plata", "650 km²")

        # Crear Provincias
        dao.execute_write(crear_provincia,"Pro1","La Rioja")
        dao.execute_write(crear_provincia,"Pro2","Córdoba")
        dao.execute_write(crear_provincia,"Pro3","Buenos Aires")

        # Crear Terrenos
        dao.execute_write(crear_terreno, "T1", "Periurbanas","URL", 5000, 1500, "En Venta", "Residencial", "2024-09-01", "Terreno con vista al parque")
        dao.execute_write(crear_terreno, "T2", "Rural","URL", 7500, 2000, "En Tramite", "Residencial", "2024-08-10", "Terreno serca del campo")
        dao.execute_write(crear_terreno, "T3", "Centro","URL", 50000, 3500, "En Venta", "Residencial", "2024-07-01", "Terreno preparado para contrunccion")
        dao.execute_write(crear_terreno, "T4", "Urbana","URL", 75000, 4500, "En Tramite", "Comercial", "2024-06-10", "Terreno cerca de univercidades")
        dao.execute_write(crear_terreno, "T5", "Urbana","URL", 150000, 5500, "En Venta", "Comercial", "2024-05-01", "Terreno para negocio")
        dao.execute_write(crear_terreno, "T6", "Urbana","URL", 275000, 8000, "Vendida", "Comercial", "2024-04-10", "Terreno ideal para negocio")
        dao.execute_write(crear_terreno, "T7", "Urbana","URL", 295000, 8000, "En Venta", "Comercial", "2024-04-10", "Terreno ideal para negocio")

        # Crear Propietarios
        dao.execute_write(crear_propietario, "P1", "Claramonte Jesus", "jClaramonte@example.com", "123456789")
        dao.execute_write(crear_propietario, "P2", "María García", "maria@example.com", "987654321")
        dao.execute_write(crear_propietario, "P3", "Nicolas Junin", "NJ@example.com", "1236789")
        dao.execute_write(crear_propietario, "P4", "Mirta Gomez", "MG@example.com", "9874321")
        dao.execute_write(crear_propietario, "P5", "Franco Hernandez", "FH@example.com", "1256789")


        # Crear Empleados
        dao.execute_write(crear_empleado, "E1", "Javier Cordoba", "Jcordoba@example.com", "555123456")
        dao.execute_write(crear_empleado, "E2", "Luis Martínez", "luis@example.com", "555654321")
        dao.execute_write(crear_empleado, "E3", "Matias Alvares",  "Matias@example.com", "5556543321")
        dao.execute_write(crear_empleado, "E4", "Franco Colapintos", "Franco@example.com", "5542324321")
        dao.execute_write(crear_empleado, "E5", "German Varquez", "ger@example.com", "5542324321")
        dao.execute_write(crear_empleado, "E6", "Alfonso Fernanades", "alf@example.com", "5542324321")
        dao.execute_write(crear_empleado, "E7", "Sofia Gonzales", "sof@example.com", "5542324321")

        # Crear Clientes
        dao.execute_write(crear_cliente, "C1", "Juan Pérez", "juan@example.com", "666123456", 60000)
        dao.execute_write(crear_cliente, "C2", "Laura Sánchez", "laura@example.com", "666654321", 80000)
        dao.execute_write(crear_cliente, "C3", "Javier Sanchez", "jav@example.com", "666112312312", 160000)
        dao.execute_write(crear_cliente, "C4", "Agustin Gomez", "agu@example.com", "666113123", 260000)
        dao.execute_write(crear_cliente, "C5", "Julio Cesar", "jul@example.com", "666112345", 360000)
        dao.execute_write(crear_cliente, "C6", "Matina Sosa", "mar@example.com", "66612321312", 460000)
        dao.execute_write(crear_cliente, "C7", "David Herrera", "Dad@example.com", "6661esaasd2", 490000)

def crear_relaciones_ejemplo(dao):

        # Asociar Zonas a Provincias
        dao.execute_write(asociar_zona_provincia, "Z1", "Pro1")
        dao.execute_write(asociar_zona_provincia, "Z2", "Pro1")
        dao.execute_write(asociar_zona_provincia, "Z3", "Pro2")
        dao.execute_write(asociar_zona_provincia, "Z4", "Pro2")
        dao.execute_write(asociar_zona_provincia, "Z5", "Pro3")
        dao.execute_write(asociar_zona_provincia, "Z6", "Pro3")
        # Asociar Terrenos a Zonas
        dao.execute_write(asociar_terreno_zona, "T2", "Z1")
        dao.execute_write(asociar_terreno_zona, "T1", "Z2")
        dao.execute_write(asociar_terreno_zona, "T3", "Z3")
        dao.execute_write(asociar_terreno_zona, "T4", "Z4")
        dao.execute_write(asociar_terreno_zona, "T5", "Z5")
        dao.execute_write(asociar_terreno_zona, "T6", "Z6")
        dao.execute_write(asociar_terreno_zona, "T7", "Z6")

        # Asignar Empleados a Zonas
        dao.execute_write(asignar_empleado_zona, "E1", "Z1")
        dao.execute_write(asignar_empleado_zona, "E2", "Z2")
        dao.execute_write(asignar_empleado_zona, "E3", "Z3")
        dao.execute_write(asignar_empleado_zona, "E4", "Z4")
        dao.execute_write(asignar_empleado_zona, "E5", "Z5")
        dao.execute_write(asignar_empleado_zona, "E6", "Z6")
        dao.execute_write(asignar_empleado_zona, "E7", "Z6")

        # Vincular Terrenos a Propietarios
        dao.execute_write(vincular_terreno_propietario, "T1", "P1")
        dao.execute_write(vincular_terreno_propietario, "T2", "P2")
        dao.execute_write(vincular_terreno_propietario, "T3", "P3")
        dao.execute_write(vincular_terreno_propietario, "T4", "P4")
        dao.execute_write(vincular_terreno_propietario, "T5", "P5")
        dao.execute_write(vincular_terreno_propietario, "T6", "P3")
        dao.execute_write(vincular_terreno_propietario, "T7", "P5")
        # Clientes interesados en Terrenos
        dao.execute_write(cliente_interesado_en_terreno, "C1", "T1")
        dao.execute_write(cliente_interesado_en_terreno, "C6", "T2")
        dao.execute_write(cliente_interesado_en_terreno, "C3", "T3")
        dao.execute_write(cliente_interesado_en_terreno, "C4", "T4")
        dao.execute_write(cliente_interesado_en_terreno, "C5", "T5")
        dao.execute_write(cliente_interesado_en_terreno, "C2", "T6")
        dao.execute_write(cliente_interesado_en_terreno, "C6", "T3")
        dao.execute_write(cliente_interesado_en_terreno, "C7", "T7")

        # Clientes interactúan con Empleados
        dao.execute_write(cliente_interactua_empleado, "C1", "E2")
        dao.execute_write(cliente_interactua_empleado, "C2", "E6")
        dao.execute_write(cliente_interactua_empleado, "C3", "E3")
        dao.execute_write(cliente_interactua_empleado, "C4", "E4")
        dao.execute_write(cliente_interactua_empleado, "C5", "E5")
        dao.execute_write(cliente_interactua_empleado, "C6", "E3")
        dao.execute_write(cliente_interactua_empleado, "C6", "E1")
        dao.execute_write(cliente_interactua_empleado, "C7", "E7")

def query_ejemplo(dao):
        print("Zonas y Provincias")
        print(dao.execute_read(get_zonas_provincias))
        print("Terrenos por Zona con su Estado")
        print(dao.execute_read(get_terrenos_por_zona))
        print("Propietarios y Terrenos que poseen")
        print(dao.execute_read(get_propietarios_terrenos))
        print("Empleados asignados por Zona")
        print(dao.execute_read(get_empleados_por_zona))
        #print("zone_by_id")
        #print(dao.execute_read(get_zone_by_id,"Z2"))
        #print("terrenos_by_zone")
        #print(dao.execute_read(get_terrenos_by_zone,"Z1"))
        #print("propietario_by_terreno")
        #print(dao.execute_read(get_propietario_by_terreno,"T5"))
        #print("terrenos_by_propietario")
        #print(dao.execute_read(get_terrenos_by_propietario,"P2"))
        #print("empleados_by_zone")
        #print(dao.execute_read(get_empleados_by_zone,"Z1"))
        #print("clientes_by_terreno")
        #print(dao.execute_read(get_clientes_by_terreno,"T3"))
        #print("terrenos_by_cliente")
        #print(dao.execute_read(get_terrenos_by_cliente,"C2"))
        #print("interacciones_cliente_empleado")
        #print(dao.execute_read(get_interacciones_cliente_empleado,"C1"))


def consulta_consola(dao):
      print("Escribir sentencia")
      sentencia=str(input())
      print("Consulta: ",sentencia)
      print("Resultado")
      print(dao.execute_read(get_consultageneral,sentencia))

def modificar_eliminar(dao):
      print("Escribir sentencia")
      sentencia=str(input())
      print("Sentencia: ",sentencia)
      dao.execute_write(get_sentenciageneral,sentencia)
      print("sentencia realisada")

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
        op=-1
        dao = DAO(uri, usuario, password)
        print("Conexión exitosa a Neo4j.")

        #sacas estos comentarios para crear una ves y volvelos a comentar
        #crear_nodos_ejemplo(dao)
        #crear_relaciones_ejemplo(dao)
        print("Nodos y relaciones creadas exitosamente.")
        while op!=0:
              print("#####menu####")
              print("op1--->Ejemplo de consulta echos")
              print("op2--->Escribir sentencia de consulta")
              print("op3--->Escribir sentencia de modificar o eliminar")
              op=int(input())
              if op==1:
                   query_ejemplo(dao)
              elif op==2:
                    consulta_consola(dao)
              elif op==3:
                    modificar_eliminar(dao)
              elif op==0:
                    print("Fin del Programa")
              else:
                    print("Opcion no valida")


        #delet_ejemplo(dao)
        #query_ejemplo(dao)


    except Neo4jError as error:
        print(f"Ocurrió un error al conectarse a Neo4j: {error}")
    finally:
        dao.close()

if __name__ == "__main__":
    main()