from neo4j import GraphDatabase

# Datos de conexión
uri = "bolt://localhost:7687"
usuario = "neo4j"
password = "tu_contraseña"

# Crear el driver
driver = GraphDatabase.driver(uri, auth=(usuario, password))

def cerrar_conexion():
    driver.close()

# Funciones para crear nodos
def crear_terreno(tx, id_terreno, ubicacion, precio, tamano, estado, tipo, fecha_de_listado, descripcion):
    query = (
        "CREATE (t:Terreno {"
        "ID_terreno: $id_terreno, "
        "Ubicacion: $ubicacion, "
        "Precio: $precio, "
        "Tamaño: $tamaño, "
        "Estado: $estado, "
        "Tipo: $tipo, "
        "Fecha_de_listado: $fecha_de_listado, "
        "Descripcion: $descripcion"
        "})"
    )
    tx.run(query, 
           id_terreno=id_terreno, 
           ubicacion=ubicacion, 
           precio=precio, 
           tamaño=tamano,
           estado=estado, 
           tipo=tipo, 
           fecha_de_listado=fecha_de_listado, 
           descripcion=descripcion)

def crear_zona(tx, id_zona, nombre_zona, tipo_zona, tamano_zona, infraestructura):
    query = (
        "CREATE (z:Zona {"
        "ID_zona: $id_zona, "
        "Nombre_zona: $nombre_zona, "
        "Tipo_zona: $tipo_zona, "
        "Tamaño_zona: $tamaño_zona, "
        "Infraestructura: $infraestructura"
        "})"
    )
    tx.run(query, 
           id_zona=id_zona, 
           nombre_zona=nombre_zona, 
           tipo_zona=tipo_zona, 
           tamaño_zona=tamano_zona,
           infraestructura=infraestructura)

def crear_cliente(tx, id_cliente, nombre_completo, datos_contacto, intereses, presupuesto):
    query = (
        "CREATE (c:Cliente {"
        "ID_cliente: $id_cliente, "
        "Nombre_completo: $nombre_completo, "
        "Datos_contacto: $datos_contacto, "
        "Intereses: $intereses, "
        "Presupuesto: $presupuesto"
        "})"
    )
    tx.run(query, 
           id_cliente=id_cliente, 
           nombre_completo=nombre_completo, 
           datos_contacto=datos_contacto, 
           intereses=intereses, 
           presupuesto=presupuesto)

def crear_propietario(tx, id_propietario, nombre_completo, datos_contacto):
    query = (
        "CREATE (p:Propietario {"
        "ID_propietario: $id_propietario, "
        "Nombre_completo: $nombre_completo, "
        "Datos_contacto: $datos_contacto"
        "})"
    )
    tx.run(query, 
           id_propietario=id_propietario, 
           nombre_completo=nombre_completo, 
           datos_contacto=datos_contacto)

def crear_empleado(tx, id_empleado, nombre_completo, zona_asignada, datos_contacto):
    query = (
        "CREATE (e:Empleado {"
        "ID_empleado: $id_empleado, "
        "Nombre_completo: $nombre_completo, "
        "Zona_asignada: $zona_asignada, "
        "Datos_contacto: $datos_contacto"
        "})"
    )
    tx.run(query, 
           id_empleado=id_empleado, 
           nombre_completo=nombre_completo, 
           zona_asignada=zona_asignada, 
           datos_contacto=datos_contacto)