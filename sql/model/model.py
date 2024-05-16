import psycopg2

class Database:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(create_query)
        self.conn.commit()

    def insert_row(self, table_name, values):
        insert_query = f"INSERT INTO {table_name} VALUES ({','.join('%s' for _ in values)})"
        self.cursor.execute(insert_query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
