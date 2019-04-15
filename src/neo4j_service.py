from neo4j import GraphDatabase

class Neo4jConnection(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    def print_relation(self, message1, message2):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._relation_greeting, message1, message2)
            print(greeting)
            for greet in greeting:
                print(greet.value())

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    @staticmethod
    def _relation_greeting(tx, message1, message2):
        result = tx.run("MATCH (first:Greeting{ message: $message1}), "
                        "(second:Greeting{ message: $message2})"
                        "CREATE (first)-[:RELATION]->(second)"
                        "RETURN first.message + ', relationated with ' + second.message", message1=message1 , message2=message2)
        #entire_result = []  # Will contain all the items
        #for record in result:
        #    entire_result.append(record)
        return result.records()

