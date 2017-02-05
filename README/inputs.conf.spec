[neo4j://<name>]
strURI = http://localhost:7474/db/data/cypher
strQuery = {  "query" : "CREATE (n:Person { name : {name} }) RETURN n",  "params" : {    "name" : "Andres"  }}