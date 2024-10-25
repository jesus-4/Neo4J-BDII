def get_zonas_empleado(tx, empleado_id):
    # Obtener todas las zonas asignadas a un empleado específico
    result = tx.run("""
        MATCH (e:Empleado {ID_empleado: $empleado_id})-[:ASIGNADO_A]->(z:Zona)
        RETURN z.ID_zona AS id, z.Nombre_zona AS nombre, z.Descripcion AS descripcion
        """, empleado_id=empleado_id)
    return [record.data() for record in result]

def get_empleados_zona(tx, zona_id):
    # Obtener todos los empleados asignados a una zona específica
    result = tx.run("""
        MATCH (z:Zona {ID_zona: $zona_id})<-[:ASIGNADO_A]-(e:Empleado)
        RETURN e.ID_empleado AS id, e.Nombre_completo AS nombre, e.Email AS email
        """, zona_id=zona_id)
    return [record.data() for record in result]

def get_empleados_zonas(tx):
    # Obtener todos los empleados y la cantidad de zonas asignadas a cada uno
    result = tx.run("""
        MATCH (e:Empleado)-[:ASIGNADO_A]->(z:Zona)
        RETURN e.ID_empleado AS id, e.Nombre_completo AS nombre, COUNT(z) AS cantidad_zonas
        """)
    return [record.data() for record in result]
