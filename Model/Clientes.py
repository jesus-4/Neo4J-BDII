def get_clientes_empleado(tx, empleado_id):
    # Obtener todos los clientes que han interactuado con un empleado específico
    result = tx.run("""
        MATCH (e:Empleado {ID_empleado: $empleado_id})<-[:INTERACTUA_CON]-(c:Cliente)
        RETURN 
        c.ID_cliente AS id_cliente, 
        c.Nombre_completo AS nombre_cliente, 
        c.Email AS email_cliente
        ORDER BY c.Nombre_completo;
        """, empleado_id=empleado_id)
    return [record.data() for record in result]

def get_interacciones(tx):
    # Obtener todas las interacciones entre clientes y empleados
    result = tx.run("""
        MATCH (c:Cliente)-[:INTERACTUA_CON]->(e:Empleado)
        RETURN c.ID_cliente AS cliente_id, c.Nombre_completo AS cliente_nombre,
               e.ID_empleado AS empleado_id, e.Nombre_completo AS empleado_nombre
        """)
    return [record.data() for record in result]

def get_empleados_cliente_id(tx, cliente_id, empleado_id):
    # Obtener detalles de interacción entre un cliente y un empleado específicos
    result = tx.run("""
        MATCH (t:Terreno)<-[:INTERESADO_EN]-(c:Cliente {ID_cliente: $cliente_id})-[:INTERACTUA_CON]->(e:Empleado {ID_empleado: $empleado_id})-[:ASIGNADO_A]->(z:Zona)
        RETURN  
        c.Nombre_completo AS nombre_cliente, 
        e.Nombre_completo AS nombre_empleado,
        t.ID_terreno AS Terreno_de_interes,
        z.Nombre_zona AS Zona;
        """, cliente_id=cliente_id, empleado_id=empleado_id)
    return [record.data() for record in result]

def get_empleados_cliente(tx, cliente_id):
    # Obtener todos los empleados con los que un cliente específico ha interactuado
    result = tx.run("""
        MATCH (c:Cliente {ID_cliente: $cliente_id})-[:INTERACTUA_CON]->(e:Empleado)
        RETURN 
        e.ID_empleado AS id_empleado, 
        e.Nombre_completo AS nombre_empleado, 
        e.Email AS email_empleado
        ORDER BY e.Nombre_completo;
        """, cliente_id=cliente_id)
    return [record.data() for record in result]