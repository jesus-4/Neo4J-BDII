from neo4j import GraphDatabase, Query
class Connection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", password))

    def close(self):
        if self._driver:
            self._driver.close()
            print("Conexión Cerrada")

    def execute_write(self, func, *args):
        with self._driver.session() as session:
            return session.execute_write(func, *args)

    def execute_read(self, func, *args):
         with self._driver.session() as session:
             return session.execute_read(func, *args)

