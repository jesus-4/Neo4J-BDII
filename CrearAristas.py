# Funciones para crear relaciones
def asignar_empleado_zona(tx, id_empleado, id_zona):
    query = (
        "MATCH (e:Empleado {ID_empleado: $id_empleado}), (z:Zona {ID_zona: $id_zona}) "
        "CREATE (e)-[:ASIGNADO_A]->(z)"
    )
    tx.run(query, id_empleado=id_empleado, id_zona=id_zona)

def asociar_zona_provincia(tx, id_zona, id_provincia):
    query = (
        "MATCH (z:Zona {ID_zona: $id_zona}), (p:Provincia {ID_provincia: $id_provincia}) "
        "CREATE (z)-[:PERTENECE_A]->(p)"
    )
    tx.run(query,id_zona=id_zona,id_provincia=id_provincia)

def asociar_terreno_zona(tx, id_terreno, id_zona):
    query = (
        "MATCH (t:Terreno {ID_terreno: $id_terreno}), (z:Zona {ID_zona: $id_zona}) "
        "CREATE (t)-[:UBICADO_EN]->(z)"
    )
    tx.run(query, id_terreno=id_terreno, id_zona=id_zona)


def vincular_terreno_propietario(tx, id_terreno, id_propietario):
    query = (
        "MATCH (t:Terreno {ID_terreno: $id_terreno}), (p:Propietario {ID_propietario: $id_propietario}) "
        "CREATE (t)-[:POSEIDO_POR]->(p)"
    )
    tx.run(query, id_terreno=id_terreno, id_propietario=id_propietario)

def cliente_interesado_en_terreno(tx, id_cliente, id_terreno):
    query = (
        "MATCH (c:Cliente {ID_cliente: $id_cliente}), (t:Terreno {ID_terreno: $id_terreno}) "
        "CREATE (c)-[:INTERESADO_EN]->(t)"
    )
    tx.run(query, id_cliente=id_cliente, id_terreno=id_terreno)

def cliente_interactua_empleado(tx, id_cliente, id_empleado):
    query = (
        "MATCH (c:Cliente {ID_cliente: $id_cliente}), (e:Empleado {ID_empleado: $id_empleado}) "
        "CREATE (c)-[:INTERACTUA_CON]->(e)"
    )
    tx.run(query, id_cliente=id_cliente, id_empleado=id_empleado)