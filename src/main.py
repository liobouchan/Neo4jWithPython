import Neo4jService

neo4j = Neo4jService.Neo4jService('bolt://localhost:7687', 'neo4j', '123')

with neo4j._driver.session() as session:

    session.write_transaction(neo4j.crear_marca, "Yamaha", "Japón")
    session.write_transaction(neo4j.crear_marca, "Harley Davidson", "Estados Unidos")

    session.write_transaction(neo4j.crear_modelo, "YZF-R6")
    session.write_transaction(neo4j.crear_modelo, "YZF-R1S")
    session.write_transaction(neo4j.crear_modelo, "Iron 883")
    session.write_transaction(neo4j.crear_modelo, "Roadster")

    session.write_transaction(neo4j.crear_relacion_fabricado_por, "YZF-R6" , "Yamaha")
    session.write_transaction(neo4j.crear_relacion_fabricado_por, "YZF-R1S", "Yamaha")
    session.write_transaction(neo4j.crear_relacion_fabricado_por, "Iron 883", "Harley Davidson")
    session.write_transaction(neo4j.crear_relacion_fabricado_por, "Roadster", "Harley Davidson")

    session.write_transaction(neo4j.crear_persona , "Leonardo")
    session.write_transaction(neo4j.crear_persona, "Valentino Rossi")

    session.write_transaction(neo4j.crear_relacion_le_gusta, "Leonardo", "YZF-R6")
    session.write_transaction(neo4j.crear_relacion_le_gusta, "Leonardo", "Iron 883")
    session.write_transaction(neo4j.crear_relacion_le_gusta, "Valentino Rossi", "YZF-R1S")

    session.read_transaction(neo4j.imprimir_todos_los_gustos_almacenados)
