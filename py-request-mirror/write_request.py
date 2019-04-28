import json
from sqlalchemy import create_engine

class write_request:
    def __init__(self, connection):
        self.connection = connection
        self.engine = create_engine(self.connection, echo=False)
        self.query = "" 

    def write(self, headers):
        query = """INSERT INTO request (headers) VALUES (%s)"""

        with self.engine.connect() as connection:
            json_headers = json.dumps(headers)
            result = connection.execute(query, [json_headers])
            connection.close()

        
