class Clientes:

    @staticmethod
    def get_empleados_cliente(cliente_id):
        # Obtener todos los empleados con los que un cliente específico ha interactuado
        def query(tx):
            result = tx.run("""
            MATCH (c:Cliente {ID_cliente: $cliente_id})-[:INTERACTUA_CON]->(e:Empleado)
            RETURN e.ID_empleado AS id, e.Nombre_completo AS nombre, e.Email AS email
            """, cliente_id=cliente_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_clientes_empleado(empleado_id):
        # Obtener todos los clientes que han interactuado con un empleado específico
        def query(tx):
            result = tx.run("""
            MATCH (e:Empleado {ID_empleado: $empleado_id})<-[:INTERACTUA_CON]-(c:Cliente)
            RETURN c.ID_cliente AS id, c.Nombre_completo AS nombre, c.Email AS email
            """, empleado_id=empleado_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_interacciones():
        # Obtener todas las interacciones entre clientes y empleados
        def query(tx):
            result = tx.run("""
            MATCH (c:Cliente)-[:INTERACTUA_CON]->(e:Empleado)
            RETURN c.ID_cliente AS cliente_id, c.Nombre_completo AS cliente_nombre,
                   e.ID_empleado AS empleado_id, e.Nombre_completo AS empleado_nombre
            """)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_empleados_cliente_id(cliente_id, empleado_id):
        # Obtener detalles de interacción entre un cliente y un empleado específicos
        def query(tx):
            result = tx.run("""
            MATCH (c:Cliente {ID_cliente: $cliente_id})-[:INTERACTUA_CON]->(e:Empleado {ID_empleado: $empleado_id})
            RETURN e.ID_empleado AS id, e.Nombre_completo AS nombre, e.Email AS email
            """, cliente_id=cliente_id, empleado_id=empleado_id)
            return [record.data() for record in result]
        return query
