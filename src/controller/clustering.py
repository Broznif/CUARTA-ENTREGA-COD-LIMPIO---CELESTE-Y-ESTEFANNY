import pandas as pd
from sklearn.cluster import KMeans
from controller.database import Database

def load_data(file_path):
    return pd.read_csv(file_path)

def process_csv_and_cluster(db, file_path, num_clusters):
    try:
        data = load_data(file_path)
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        cluster_results = kmeans.fit_predict(data).tolist()

        db.insert_clustering_result(file_path, num_clusters, cluster_results)
        return True, "Clustering realizado exitosamente y resultados almacenados en la base de datos."
    except Exception as e:
        return False, f"Error al procesar archivo CSV y realizar clustering: {str(e)}"
