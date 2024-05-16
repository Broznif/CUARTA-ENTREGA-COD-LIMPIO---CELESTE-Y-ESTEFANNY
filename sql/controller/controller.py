import psycopg2
import pandas as pd
import SecretConfig

class Database:
    def __init__(self, Database, user, password, host='localhost', port='5432'):
        self.dbname = Database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to database successfully!")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to database closed.")

    def create_table(self, table_name, columns):
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")
            self.connection.commit()
            print(f"Table '{table_name}' created successfully!")
        except Exception as e:
            print(f"Error creating table: {e}")

    def insert_row(self, table_name, values):
        try:
            placeholders = ', '.join(['%s'] * len(values))
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(insert_query, values)
            self.connection.commit()
            print("Row inserted successfully!")
        except Exception as e:
            print(f"Error inserting row: {e}")
