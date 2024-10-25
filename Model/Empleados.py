class Empleados:

    @staticmethod
    def get_zonas_empleado(empleado_id):
        # Obtener todas las zonas asignadas a un empleado específico
        def query(tx):
            result = tx.run("""
            MATCH (e:Empleado {ID_empleado: $empleado_id})-[:ASIGNADO_A]->(z:Zona)
            RETURN z.ID_zona AS id, z.Nombre_zona AS nombre, z.Descripcion AS descripcion
            """, empleado_id=empleado_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_empleados_zona(zona_id):
        # Obtener todos los empleados asignados a una zona específica
        def query(tx):
            result = tx.run("""
            MATCH (z:Zona {ID_zona: $zona_id})<-[:ASIGNADO_A]-(e:Empleado)
            RETURN e.ID_empleado AS id, e.Nombre_completo AS nombre, e.Email AS email
            """, zona_id=zona_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_empleados_zonas():
        # Obtener todos los empleados y la cantidad de zonas asignadas a cada uno
        def query(tx):
            result = tx.run("""
            MATCH (e:Empleado)-[:ASIGNADO_A]->(z:Zona)
            RETURN e.ID_empleado AS id, e.Nombre_completo AS nombre, COUNT(z) AS cantidad_zonas
            """)
            return [record.data() for record in result]
        return query
