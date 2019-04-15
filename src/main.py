import neo4j_service

uri = "bolt://localhost:7687"
user = "neo4j"
password = "123"

neo4j = neo4j_service.Neo4jConnection(uri,user,password)
neo4j.print_greeting("Hola Mundo")
neo4j.print_greeting("Adios Mundo")
neo4j.print_relation("Hola Mundo", "Adios Mundo")
