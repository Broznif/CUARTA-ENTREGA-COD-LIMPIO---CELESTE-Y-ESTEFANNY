import psycopg2
import pandas as pd
from sklearn.cluster import KMeans

def create_tables():
    # Configurar la conexión a la base de datos PostgreSQL
    connection = psycopg2.connect(
        dbname="entrega_owner",
        user="entrega_owner_owner",
        password="Rofg6C8BcTVk",
        host="ep-muddy-band-a581f951.us-east-2.aws.neon.tech",
        port=5432
    )

    # Crear tabla para almacenar los resultados del clustering
    create_table_query = """
        CREATE TABLE IF NOT EXISTS clustering_results (
            id SERIAL PRIMARY KEY,
            filename TEXT NOT NULL,
            num_clusters INTEGER NOT NULL,
            cluster_results JSONB
        );
    """

    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def process_csv_and_cluster(file_path, num_clusters):
    try:
        # Cargar datos desde el archivo CSV
        data = pd.read_csv(file_path)

        # Realizar clustering con el número de clusters especificado por el usuario
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        cluster_results = kmeans.fit_predict(data)

        # Convertir resultados de clustering a lista
        cluster_results_list = cluster_results.tolist()

        # Insertar resultados de clustering en la base de datos
        connection = psycopg2.connect(
            dbname="tu_base_de_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )

        insert_query = """
            INSERT INTO clustering_results (filename, num_clusters, cluster_results)
            VALUES (%s, %s, %s);
        """

        cursor = connection.cursor()
        cursor.execute(insert_query, (file_path, num_clusters, cluster_results_list))
        connection.commit()
        cursor.close()
        connection.close()

        return True, "Clustering realizado exitosamente y resultados almacenados en la base de datos."
    except Exception as e:
        return False, f"Error al procesar archivo CSV y realizar clustering: {str(e)}"
