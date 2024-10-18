# Obtener detalles de una zona por ID

def get_zone_by_id(tx, id_zona):
   query = (
        "MATCH (z:Zona {ID_zona: $id_zona}) "
        "RETURN z"
        )
   result = tx.run(query, id_zona=id_zona)
   zonas= [record["z"] for record in result]
   formatted_result = []
   for zona in zonas:
        formatted_result.append(f"Zona: {zona['Nombre_zona']}, Tamaño: {zona['Tamaño_zona']}, "
                                f"Infraestructura: {zona['Infraestructura']}, ID: {zona['ID_zona']}")
   return "\n".join(formatted_result)

# Obtener todos los terrenos en una zona específica
def get_terrenos_by_zone(tx, id_zona):
    query = (
        "MATCH (z:Zona {ID_zona: $id_zona})<-[:PERTENECE_A]-(t:Terreno) "
        "RETURN t"
    )
    result = tx.run(query, id_zona=id_zona)
    terrenos=[record["t"] for record in result]
    formatted_result = []
    for terreno in terrenos:
        formatted_result.append(f"Terreno ID: {terreno['ID_terreno']}, Tipo_zona: {terreno['Tipo_zona']}, "
                                f"Ubicación: {terreno['Ubicacion']}, Precio: {terreno['Precio']}, "
                                f"Tamaño: {terreno['Tamaño']}, Estado: {terreno['Estado']},Tipo: {terreno['TipO']}, "
                                f"Fecha de listado: {terreno['Fecha_de_listado']}")
    return "\n".join(formatted_result)



# Obtener los propietarios de un terreno
def get_propietario_by_terreno(tx, id_terreno):
    query = (
        "MATCH (p:Propietario)-[:POSEE]->(t:Terreno {ID_terreno: $id_terreno}) "
        "RETURN p"
    )
    result = tx.run(query, id_terreno=id_terreno)
    propietarios= [record["p"] for record in result]
    formatted_result = []
    for propietario in propietarios:
        formatted_result.append(f"Propietario: {propietario['Nombre_completo']}, Email: {propietario['Email']}, "
                                f"Teléfono: {propietario['Telefono']}, ID: {propietario['ID_propietario']}")
    return "\n".join(formatted_result)




# Obtener todos los terrenos de un propietario

def get_terrenos_by_propietario(tx, id_propietario):
    query = (
        "MATCH (p:Propietario {ID_propietario: $id_propietario})-[:POSEE]->(t:Terreno) "
        "RETURN t"
    )
    result = tx.run(query, id_propietario=id_propietario)
    terrenos= [record["t"] for record in result]
    formatted_result = []
    for terreno in terrenos:
        formatted_result.append(f"Terreno ID: {terreno['ID_terreno']}, Ubicación: {terreno['Ubicacion']}, "
                                f"Precio: {terreno['Precio']}, Tamaño: {terreno['Tamaño']}, "
                                f"Estado: {terreno['Estado']}, Fecha de listado: {terreno['Fecha_de_listado']}")
    return "\n".join(formatted_result)




# Obtener todos los empleados asignados a una zona
def get_empleados_by_zone(tx, id_zona):
    query = (
        "MATCH (e:Empleado {Zona_asignada: $id_zona}) "
        "RETURN e"
    )
    result = tx.run(query, id_zona=id_zona)
    empleados= [record["e"] for record in result]
    formatted_result = []
    for empleado in empleados:
        formatted_result.append(f"Empleado: {empleado['Nombre_completo']}, Email: {empleado['Email']}, "
                                f"Teléfono: {empleado['Telefono']}, Zona Asignada: {empleado['Zona_asignada']}, "
                                f"ID: {empleado['ID_empleado']}")
    return "\n".join(formatted_result)



    # Obtener los clientes interesados en un terreno
def get_clientes_by_terreno(tx, id_terreno):
    query = (
        "MATCH (c:Cliente)-[:INTERESADO_EN]->(t:Terreno {ID_terreno: $id_terreno}) "
        "RETURN c"
    )
    result = tx.run(query, id_terreno=id_terreno)
    clientes= [record["c"] for record in result]
    formatted_result = []
    for cliente in clientes:
        formatted_result.append(f"Cliente: {cliente['Nombre_completo']}, Email: {cliente['Email']}, "
                                f"Teléfono: {cliente['Telefono']}, Presupuesto: {cliente['Presupuesto']}, "
                                f"ID: {cliente['ID_cliente']}, Intereses: {cliente['Intereses']}")
    return "\n".join(formatted_result)



def get_terrenos_by_cliente(tx, id_cliente):
    query = (
        "MATCH (c:Cliente {ID_cliente: $id_cliente})-[:INTERESADO_EN]->(t:Terreno) "
        "RETURN t"
    )
    result = tx.run(query, id_cliente=id_cliente)
    terrenos= [record["t"] for record in result]
    formatted_result = []
    for terreno in terrenos:
        formatted_result.append(f"Terreno ID: {terreno['ID_terreno']}, Ubicación: {terreno['Ubicacion']}, "
                                f"Precio: {terreno['Precio']}, Tamaño: {terreno['Tamaño']}, "
                                f"Estado: {terreno['Estado']}, Fecha de listado: {terreno['Fecha_de_listado']}")
    return "\n".join(formatted_result)



    # Obtener las interacciones de un cliente con los empleados
def get_interacciones_cliente_empleado(tx, id_cliente):
    query = (
        "MATCH (c:Cliente {ID_cliente: $id_cliente})-[:INTERACTUA_CON]->(e:Empleado) "
        "RETURN e"
    )
    result = tx.run(query, id_cliente=id_cliente)
    interacciones=[record["e"git] for record in result]
    formatted_result = []
    for interac in interacciones:
        liente = interac['c']
        empleado = interac['e']
        formatted_result.append(f"Cliente: {['Nombre_completo']} interactuó con Empleado: {empleado['Nombre_completo']}")
    return "\n".join(formatted_result)


