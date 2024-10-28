def get_empleados_zonas(tx):
    # Obtener todos los empleados y la cantidad de zonas asignadas a cada uno
    result = tx.run("""
        MATCH (e:Empleado)-[:ASIGNADO_A]->(z:Zona)
        RETURN e.ID_empleado AS Id_Empleado, e.Nombre_completo AS nombre, COUNT(z) AS cantidad_zonas
        """)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Id_Empleado:{ p['Id_Empleado']}   nombre:{ p['nombre']} cantidad_zonas:{ p['cantidad_zonas']} ")
    return "\n".join(formatted_result) 

def get_zonas_empleado(tx, empleado_id):
    # Obtener todas las zonas asignadas a un empleado específico
    result = tx.run("""
        MATCH (e:Empleado {ID_empleado: $empleado_id})-[:ASIGNADO_A]->(z:Zona)
        RETURN z.ID_zona AS ID_Zona, z.Nombre_zona AS nombre;
        """, empleado_id=empleado_id)
    formatted_result = []
    for p in result:
        formatted_result.append(f"ID_Zona:{ p['ID_Zona']}   nombre:{ p['nombre']} ")
    return "\n".join(formatted_result) 



def get_empleados_zona(tx, zona_id):
    # Obtener todos los empleados asignados a una zona específica
    result = tx.run("""
        MATCH (z:Zona {ID_zona: $zona_id})<-[:ASIGNADO_A]-(e:Empleado)
        RETURN e.ID_empleado AS Id_Empleado, e.Nombre_completo AS nombre;
        """, zona_id=zona_id)
    formatted_result = []
    for p in result:
        formatted_result.append(f"Id_Empleado:{ p['Id_Empleado']}   nombre:{ p['nombre']} ")
    return "\n".join(formatted_result) 
