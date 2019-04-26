from neo4j import GraphDatabase


class Neo4jService(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def crear_persona(self, tx, nombre):
        tx.run("CREATE (:Persona {nombre: $nombre})", nombre=nombre)

    def crear_modelo(self, tx, nombre):
        tx.run("CREATE (:Modelo {nombre: $nombre})", nombre=nombre)

    def crear_marca(self, tx, nombre, pais):
        tx.run("CREATE (:Marca {nombre: $nombre , pais: $pais})" , nombre=nombre, pais=pais)

    def crear_relacion_le_gusta(self, tx, nombre_persona, nombre_modelo):
        tx.run("MATCH (a:Persona {nombre: $nombre_persona}) "
               "MATCH (b:Modelo {nombre: $nombre_modelo}) "
               "MERGE (a)-[:LE_GUSTA]->(b)",
               nombre_persona=nombre_persona, nombre_modelo=nombre_modelo)

    def crear_relacion_fabricado_por(self, tx, nombre_modelo, nombre_marca):
        tx.run("MATCH (a:Modelo {nombre: $nombre_modelo}) "
               "MATCH (b:Marca {nombre: $nombre_marca}) "
               "MERGE (a)-[:ES_FABRICADO_POR]->(b)",
               nombre_modelo=nombre_modelo, nombre_marca=nombre_marca)

    def imprimir_todos_los_gustos_almacenados(self,tx):
        result = tx.run("MATCH (a)-[:LE_GUSTA]->(b)-[:ES_FABRICADO_POR]->(c) RETURN a.nombre, b.nombre, c.nombre")
        for record in result:
            print("A {} le gusta la motocicleta {} de marca {}".format(record["a.nombre"] ,record["b.nombre"] , record["c.nombre"]))