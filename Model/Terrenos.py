class Terrenos:
    @staticmethod
    def get_prov_zona_id(prov_id, zona_id):
        def query(tx):
            result = tx.run("""
            MATCH (t)-[:UBICADO_EN]->(p:Provincia {ID_provincia: $prov_id})
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
            """, zona_id=zona_id, prov_id=prov_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_prov_id(prov_id):
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona {provincia: $prov_id})
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
            """, prov_id=prov_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_zona_id(zona_id):
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)-[:UBICADO_EN]->(z:Zona {ID_zona: $zona_id})
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
            """, zona_id=zona_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get():
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio, t.Tamaño AS tamaño
            """)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_cliente_id(cliente_id, terreno_id=None): #Ajustar porque pusiste mal un parametro en el DAO - ya lo correji pero aca no
        # Terrenos de interés para un cliente específico
        def query(tx):
            if terreno_id:
                result = tx.run("""
                MATCH (t:Terreno {ID_terreno: $terreno_id})<-[:INTERESADO_EN]-(c:Cliente{ID_cliente: $cliente_id})
                RETURN c.ID_cliente AS id, c.Nombre_completo AS nombre, c.Email AS email
                """, terreno_id=terreno_id, cliente_id=cliente_id)
            else:
                result = tx.run("""
                MATCH (c:Cliente {ID_cliente: $cliente_id})-[:INTERESADO_EN]->(t:Terreno)
                RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
                """, cliente_id=cliente_id)
            return [record.data() for record in result]

        return query

    @staticmethod
    def get_terreno_id(terreno_id):
        # Clientes interesados en un terreno específico
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno {ID_terreno: $terreno_id})<-[:INTERESADO_EN]-(c:Cliente)
            RETURN c.ID_cliente AS id, c.Nombre_completo AS nombre, c.Email AS email
            """, terreno_id=terreno_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_clientes_terreno():
        # Todos los terrenos con la cantidad de clientes interesados
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)<-[:INTERESADO_EN]-(c:Cliente)
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, COUNT(c) AS clientes_interesados
            """)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_propietarios_provincia_id(provincia_id, propietario_id=None):
        # Obtener terrenos de propietarios en una provincia o un propietario específico en una provincia
        def query(tx):
            if propietario_id:
                result = tx.run("""
                MATCH (p:Propietario {ID_propietario: $propietario_id})-[:POSEE]->(t:Terreno)-[:UBICADO_EN]->(z:Zona {ID_provincia: $provincia_id})
                RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
                """, propietario_id=propietario_id, provincia_id=provincia_id)
            else:
                result = tx.run("""
                MATCH (p:Propietario)-[:POSEE]->(t:Terreno)-[:UBICADO_EN]->(z:Zona {ID_provincia: $provincia_id})
                RETURN p.ID_propietario AS id, p.Nombre AS nombre, COUNT(t) AS cantidad_terrenos
                """, provincia_id=provincia_id)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_terrenos_disponibles_zona(zona_id= None):
        # Terrenos disponibles en una zona específica
        def query(tx):
            if zona_id:
                result = tx.run("""
                MATCH (t:Terreno {Estado: "En Venta"})-[:UBICADO_EN]->(z:Zona {ID_zona: $zona_id})
                RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
                """, zona_id=zona_id)
            else:
                result = tx.run("""
                MATCH (z:Zona)<-[:UBICADO_EN]-(t:Terreno {Estado: "En Venta"})
                RETURN z.ID_zona AS id, z.Nombre_zona AS nombre, COUNT(t) AS terrenos_disponibles
                """)

            return [record.data() for record in result]
        return query

    @staticmethod
    def get_terrenos_por_rango_precio(min_precio, max_precio):
        # Terrenos cuyo precio está entre un rango
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)
            WHERE t.Precio >= $min_precio AND t.Precio <= $max_precio
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
            """, min_precio=min_precio, max_precio=max_precio)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_terrenos_min_precio(min_precio):
        # Terrenos cuyo precio es mayor o igual a `min_precio`
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)
            WHERE t.Precio >= $min_precio
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
            """, min_precio=min_precio)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_terrenos_max_precio(max_precio):
        # Terrenos cuyo precio es menor o igual a `max_precio`
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)
            WHERE t.Precio <= $max_precio
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
            """, max_precio=max_precio)
            return [record.data() for record in result]
        return query

    @staticmethod
    def get_todos_terrenos_precio():
        # Obtener todos los terrenos con su precio
        def query(tx):
            result = tx.run("""
            MATCH (t:Terreno)
            RETURN t.ID_terreno AS id, t.Ubicacion AS ubicacion, t.Precio AS precio
            """)
            return [record.data() for record in result]
        return query
