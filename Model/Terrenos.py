def get_prov_zona_id(tx,prov_id, zona_id):
        result=[]
        result = tx.run("""
            MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona{ID_zona: $zona_id})-[:PERTENECE_A]->(p:Provincia {ID_provincia: $prov_id})
            RETURN t.ID_terreno AS Terreno, z.Nombre_zona AS Zona, p.Nombre_provincia AS Provincia;
            """, zona_id=zona_id, prov_id=prov_id)
        formatted_result = []
        for p in result:
            formatted_result.append(f"Terreno:{ p["Terreno"]}   Zona:{ p["Zona"]}   Provincia:{p["Provincia"]}")
        return "\n".join(formatted_result)

def get_prov_id(tx, prov_id):
    result = tx.run("""
        MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(p:Provincia {ID_provincia: $prov_id})
        RETURN t.ID_terreno AS Terreno, z.Nombre_zona AS Zona, p.Nombre_provincia AS Provincia;
        """, prov_id=prov_id)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Terreno:{ p["Terreno"]}   Zona:{ p["Zona"]}   Provincia:{p["Provincia"]}")
    return "\n".join(formatted_result)
    

def get_zona_id(tx, zona_id):
    result = tx.run("""
        MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona {ID_zona: $zona_id})
        RETURN t.ID_terreno AS Terreno, z.Nombre_zona AS Zona;
        """, zona_id=zona_id)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Terreno:{ p["Terreno"]}   Zona:{ p["Zona"]}")
    return "\n".join(formatted_result)
    
def get(tx):
    result = tx.run("""
        MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(p:Provincia)
        RETURN t.ID_terreno AS Terreno, z.Nombre_zona AS Zona, p.Nombre_provincia AS Provincia;
        """)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Terreno:{ p["Terreno"]}   Zona:{ p["Zona"]}   Provincia:{p["Provincia"]}")
    return "\n".join(formatted_result)
    
def get_cliente_id(tx, cliente_id, terreno_id=None):
    if terreno_id :
        result = tx.run("""
            MATCH (t:Terreno {ID_terreno: $terreno_id})<-[:INTERESADO_EN]-(c:Cliente{ID_cliente: $cliente_id})
            RETURN t.Tipo_zona AS TipoZona,c.ID_cliente AS ID_Cliente, c.Nombre_completo AS Nombre;
            """, terreno_id=terreno_id, cliente_id=cliente_id)
        formatted_result = []
        for p in result:
            formatted_result.append(f"TipoZona:{ p["TipoZona"]}   ID_Cliente:{ p["ID_Cliente"]}   Nombre:{p["Nombre"]}")
        return "\n".join(formatted_result)
    else:
        result = tx.run("""
            MATCH (c:Cliente {ID_cliente: $cliente_id})-[:INTERESADO_EN]->(t:Terreno)
            RETURN t.Tipo_zona AS TipoZona,c.ID_cliente AS ID_Cliente, c.Nombre_completo AS Nombre;
            """, cliente_id=cliente_id)
        formatted_result = []
        for p in result:
            formatted_result.append(f"TipoZona:{ p["TipoZona"]}   ID_Cliente:{ p["ID_Cliente"]}   Nombre:{p["Nombre"]}")
        return "\n".join(formatted_result)

def get_terreno_id(tx, terreno_id):
    result = tx.run("""
        MATCH (t:Terreno {ID_terreno: $terreno_id})<-[:INTERESADO_EN]-(c:Cliente)
        RETURN c.ID_cliente AS ID_Cliente, c.Nombre_completo AS Nombre, t.ID_terreno AS Terreno;
        """, terreno_id=terreno_id)
    formatted_result = []
    for p in result:
        formatted_result.append(f"ID_Cliente:{ p["ID_Cliente"]}   Nombre:{ p["Nombre"]}   Terreno:{p["Terreno"]}")
    return "\n".join(formatted_result)

def get_clientes_terreno(tx):
    result = tx.run("""
        MATCH (t:Terreno)<-[:INTERESADO_EN]-(c:Cliente)
        RETURN t.ID_terreno AS ID_Terreno, COUNT(c) AS clientes_interesados
        """)
    formatted_result = []
    for p in result:
        formatted_result.append(f"ID_Terreno:{ p["ID_Terreno"]}   clientes_interesados:{ p["clientes_interesados"]}")
    return "\n".join(formatted_result)

def get_propietarios_provincia_id(tx, provincia_id, propietario_id=None):
    if propietario_id:
        result = tx.run("""
            MATCH (p:Propietario {ID_propietario: $propietario_id})<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia {ID_provincia: $provincia_id})
            RETURN 
            p.ID_propietario AS ID_propietario, 
            p.Nombre_completo AS Nombre, 
            COUNT(t) AS cantidad_terrenos;
            """, propietario_id=propietario_id, provincia_id=provincia_id)
        formatted_result = []
        for p in result:
            formatted_result.append(f"ID_propietario:{ p["ID_propietario"]}   Nombre:{ p["Nombre"]}   cantidad_terrenos:{p["cantidad_terrenos"]}")
        return "\n".join(formatted_result)
    else:
        result = tx.run("""
            MATCH (p:Propietario)<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia {ID_provincia: $provincia_id})
            WITH p, COUNT(t) AS cantidad_terrenos
            RETURN 
            p.ID_propietario AS ID_Propietario, p.Nombre_completo AS Nombre,cantidad_terrenos
            ORDER BY cantidad_terrenos DESC;
            """, provincia_id=provincia_id)
        formatted_result = []
        for p in result:
            formatted_result.append(f"ID_Propietario:{ p["ID_Propietario"]}   Nombre:{ p["Nombre"]}   cantidad_terrenos:{p["cantidad_terrenos"]}")
        return "\n".join(formatted_result)
    

def get_propietario_id(tx, propietario_id):
    # Obtener todos los terrenos de un propietario específico
    result = tx.run("""
        MATCH (p:Propietario {ID_propietario: $propietario_id})<-[:POSEIDO_POR]-(t:Terreno)-[:UBICADO_EN]->(z:Zona)-[:PERTENECE_A]->(pr:Provincia)
        RETURN 
        t.ID_terreno AS ID_Terreno, 
        t.Tipo_zona AS Zona_terreno, 
        z.Nombre_zona AS Zona, 
        pr.Nombre_provincia AS Provincia, 
        p.Nombre_completo AS Propietario;
        """, propietario_id=propietario_id)
    formatted_result = []
    for p in result:
        formatted_result.append(f"ID_Terreno:{ p["ID_Terreno"]}   Zona_terreno:{ p["Zona_terreno"]}   Zona:{p["Zona"]} Provincia:{p["Provincia"]} Propietario:{p["Propietario"]}")
    return "\n".join(formatted_result)

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
    formatted_result = []
    for p in result:
        formatted_result.append(f"id_propietario:{ p["id_propietario"]}   nombre_propietario:{ p["nombre_propietario"]}   provincia:{p["provincia"]} cantidad_terrenos:{p["cantidad_terrenos"]} ")
    return "\n".join(formatted_result)


def get_terrenos_disponibles_zona(tx, zona_id=None):
    if zona_id:
        result = tx.run("""
            MATCH (t:Terreno {Estado: "En Venta"})-[:UBICADO_EN]->(z:Zona {ID_zona:$zona_id})
            RETURN t.ID_terreno AS ID_Terreno, z.Nombre_zona AS Zona, t.Precio AS precio
            """, zona_id=zona_id)
        formatted_result = []
        for p in result:
            formatted_result.append(f"ID_Terreno:{ p["ID_Terreno"]}   Zona:{ p["Zona"]}  precio:{p["precio"]}")
        return "\n".join(formatted_result)
    else:
        result = tx.run("""
            MATCH (t:Terreno {Estado: "En Venta"})-[:UBICADO_EN]->(z:Zona)
            RETURN 
            z.Nombre_zona AS zona, 
            COLLECT(t.ID_terreno) AS terrenos_en_venta, 
            COUNT(t) AS cantidad_terrenos_en_venta
            ORDER BY zona;
            """)
        formatted_result = []
        for p in result:
            formatted_result.append(f"zona:{ p["zona"]}   terrenos_en_venta:{ p["terrenos_en_venta"]}  cantidad_terrenos_en_venta:{p["cantidad_terrenos_en_venta"]}")
        return "\n".join(formatted_result)
def get_terrenos_por_rango_precio(tx, min_precio, max_precio):
    result = tx.run("""
        MATCH (t:Terreno)
        WHERE t.Precio >= $min_precio AND t.Precio <= $max_precio
        RETURN t.ID_terreno AS Id_terreno, t.Precio AS precio
        """, min_precio=min_precio, max_precio=max_precio)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Id_terreno:{ p["Id_terreno"]}   precio:{ p["precio"]} ")
    return "\n".join(formatted_result)

def get_terrenos_min_precio(tx, min_precio):
    result = tx.run("""
        MATCH (t:Terreno)
        WHERE t.Precio >= $min_precio
        RETURN t.ID_terreno AS Id_Terreno, t.Precio AS precio
        """, min_precio=min_precio)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Id_Terreno:{ p["Id_Terreno"]}   precio:{ p["precio"]} ")
    return "\n".join(formatted_result)

def get_terrenos_max_precio(tx, max_precio):
    result = tx.run("""
        MATCH (t:Terreno)
        WHERE t.Precio <= $max_precio
        RETURN t.ID_terreno AS Id_Terreno, t.Precio AS precio
        """, max_precio=max_precio)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Id_Terreno:{ p["Id_Terreno"]}   precio:{ p["precio"]} ")
    return "\n".join(formatted_result)

def get_todos_terrenos_precio(tx):
    result = tx.run("""
        MATCH (t:Terreno)
        RETURN t.ID_terreno AS Id_Terreno, t.Precio AS precio;
        """)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Id_Terreno:{ p["Id_Terreno"]}   precio:{ p["precio"]} ")
    return "\n".join(formatted_result) 