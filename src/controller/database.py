import psycopg2
import json

class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(self.connection_string)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_tables(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS clustering_results (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                num_clusters INTEGER NOT NULL,
                cluster_results JSONB NOT NULL
            );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_clustering_result(self, filename, num_clusters, cluster_results):
        insert_query = """
            INSERT INTO clustering_results (filename, num_clusters, cluster_results)
            VALUES (%s, %s, %s);
        """
        self.cursor.execute(insert_query, (filename, num_clusters, json.dumps(cluster_results)))
        self.connection.commit()