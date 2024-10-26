def get_prov_zona_id(tx,prov_id, zona_id):
        result=[]
        result = tx.run("""
            MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona{ID_zona: $zona_id})-[:PERTENECE_A]->(p:Provincia {ID_provincia: $prov_id})
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
            """, zona_id=zona_id, prov_id=prov_id)
        return [record.data() for record in result]

def get_prov_id(tx, prov_id):
    result = tx.run("""
        MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(p:Provincia {ID_provincia: $prov_id})
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
        """, prov_id=prov_id)
    return [record.data() for record in result]

def get_zona_id(tx, zona_id):
    result = tx.run("""
        MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona {ID_zona: $zona_id})
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
        """, zona_id=zona_id)
    return [record.data() for record in result]

def get(tx):
    result = tx.run("""
        MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(p:Provincia)
        RETURN t.ID_terreno ,z.ID_zona ,p.ID_provincia, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
        """)
    return [record.data() for record in result]

def get_cliente_id(tx, cliente_id, terreno_id=None):
    if terreno_id :
        result = tx.run("""
            MATCH (t:Terreno {ID_terreno: $terreno_id})<-[:INTERESADO_EN]-(c:Cliente{ID_cliente: $cliente_id})
            RETURN t.Tipo_zona AS Zona,c.ID_cliente AS id, c.Nombre_completo AS nombre, c.Email AS email
            """, terreno_id=terreno_id, cliente_id=cliente_id)
    else:
        result = tx.run("""
            MATCH (c:Cliente {ID_cliente: $cliente_id})-[:INTERESADO_EN]->(t:Terreno)
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
            """, cliente_id=cliente_id)
    return [record.data() for record in result]

def get_terreno_id(tx, terreno_id):
    result = tx.run("""
        MATCH (t:Terreno {ID_terreno: $terreno_id})<-[:INTERESADO_EN]-(c:Cliente)
        RETURN c.ID_cliente AS id, c.Nombre_completo AS nombre, c.Email AS email
        """, terreno_id=terreno_id)
    return [record.data() for record in result]

def get_clientes_terreno(tx):
    result = tx.run("""
        MATCH (t:Terreno)<-[:INTERESADO_EN]-(c:Cliente)
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, COUNT(c) AS clientes_interesados
        """)
    return [record.data() for record in result]
def get_propietarios_provincia_id(tx, provincia_id, propietario_id=None):
    if propietario_id:
        result = tx.run("""
            MATCH (p:Propietario {ID_propietario: $propietario_id})<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia {ID_provincia: $provincia_id})
            RETURN 
            p.ID_propietario AS id_propietario, 
            p.Nombre_completo AS Nombre, 
            COUNT(t) AS cantidad_terrenos;
            """, propietario_id=propietario_id, provincia_id=provincia_id)
    else:
        result = tx.run("""
            MATCH (p:Propietario)<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia {ID_provincia: $provincia_id})
            WITH p, COUNT(t) AS cantidad_terrenos
            RETURN 
            p.ID_propietario AS id, p.Nombre_completo AS nombre,cantidad_terrenos
            ORDER BY cantidad_terrenos DESC;
            """, provincia_id=provincia_id)
    return [record.data() for record in result]

def get_propietario_id(tx, propietario_id):
    # Obtener todos los terrenos de un propietario específico
    result = tx.run("""
        MATCH (p:Propietario {ID_propietario: $propietario_id})<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia)
        RETURN 
        t.ID_terreno AS id_terreno, 
        t.Tipo_zona AS Zona_terreno, 
        z.Nombre_zona AS Zona, 
        pr.Nombre_provincia AS Provincia, 
        p.Nombre_completo AS propietario;
        """, propietario_id=propietario_id)
    return [record.data() for record in result]

def get_propietario_provincia(tx):
    result = tx.run("""
            MATCH (p:Propietario)<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia)
            WITH p, pr, COUNT(t) AS cantidad_terrenos
            RETURN 
            p.ID_propietario AS id_propietario, 
            p.Nombre_completo AS nombre_propietario, 
            pr.Nombre_provincia AS provincia, 
            cantidad_terrenos
            ORDER BY provincia, cantidad_terrenos DESC;
            """)
    return [record.data() for record in result]


def get_terrenos_disponibles_zona(tx, zona_id=None):
    if zona_id:
        result = tx.run("""
            MATCH (t:Terreno {Estado: "En Venta"})-[:UBICADO_EN]->(z:Zona {ID_zona:$zona_id})
            RETURN t.ID_terreno AS id, z.Nombre_zona AS Zona, t.Precio AS precio
            """, zona_id=zona_id)
    else:
        result = tx.run("""
            MATCH (t:Terreno {Estado: "En Venta"})-[:UBICADO_EN]->(z:Zona)
            RETURN 
            z.Nombre_zona AS zona, 
            COLLECT(t.ID_terreno) AS terrenos_en_venta, 
            COUNT(t) AS cantidad_terrenos_en_venta
            ORDER BY zona;
            """)
    return [record.data() for record in result]
def get_terrenos_por_rango_precio(tx, min_precio, max_precio):
    result = tx.run("""
        MATCH (t:Terreno)
        WHERE t.Precio >= $min_precio AND t.Precio <= $max_precio
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
        """, min_precio=min_precio, max_precio=max_precio)
    return [record.data() for record in result]

def get_terrenos_min_precio(tx, min_precio):
    result = tx.run("""
        MATCH (t:Terreno)
        WHERE t.Precio >= $min_precio
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
        """, min_precio=min_precio)
    return [record.data() for record in result]

def get_terrenos_max_precio(tx, max_precio):
    result = tx.run("""
        MATCH (t:Terreno)
        WHERE t.Precio <= $max_precio
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
        """, max_precio=max_precio)
    return [record.data() for record in result]

def get_todos_terrenos_precio(tx):
    result = tx.run("""
        MATCH (t:Terreno)
        RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
        """)
    return [record.data() for record in result] 