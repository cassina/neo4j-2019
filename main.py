from neo4j import GraphDatabase, basic_auth

from config import NEO4J_PASSWORD, NEO4J_USERNAME, NEO4J_URI
from queries import ENTITIES

# Configurar driver
driver = GraphDatabase.driver(
    uri=NEO4J_URI,
    auth=basic_auth(
        user=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )
)
# Crear nueva sesión
session = driver.session()

results = session.run(
    ENTITIES,
    parameters={
        'limit': 100
    }
)

print([record['name'] for record in results])
