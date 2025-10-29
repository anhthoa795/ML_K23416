import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Kết nối MySQL
def getConnect(server, port, database, username, password):
    try:
        conn = mysql.connector.connect(
            host=server,
            port=port,
            database=database,
            user=username,
            password=password
        )
        print("Connected to MySQL successfully!")
        return conn
    except mysql.connector.Error as e:
        print("Connection Error:", e)
        return None

# Lấy dữ liệu đặc trưng về mức độ quan tâm phim
def getCustomerInterestData(conn):
    sql = """
        SELECT 
            c.customer_id,
            COUNT(r.rental_id) AS rental_count,
            COUNT(DISTINCT i.film_id) AS distinct_film_count
        FROM customer c
        LEFT JOIN rental r ON c.customer_id = r.customer_id
        LEFT JOIN inventory i ON r.inventory_id = i.inventory_id
        GROUP BY c.customer_id;
    """
    df = pd.read_sql(sql, conn)
    return df

if __name__ == "__main__":
    conn = getConnect("localhost", 3306, "sakila", "root", "thoalalen792005")

    if conn:
        df = getCustomerInterestData(conn)

        X = df[['rental_count', 'distinct_film_count']].values

        # Elbow to find optimal clusters
        inertia = []
        for k in range(1, 11):
            model = KMeans(n_clusters=k, random_state=42)
            model.fit(X)
            inertia.append(model.inertia_)

        plt.plot(range(1, 11), inertia, marker='o')
        plt.xlabel("Number of clusters")
        plt.ylabel("Inertia")
        plt.title("Elbow Method - Customer Interest in Films")
        plt.show()

        # Chọn số cụm (có thể thay đổi sau khi xem biểu đồ Elbow)
        k = 4
        model = KMeans(n_clusters=k, random_state=42)
        df["cluster"] = model.fit_predict(X)

        print("\nResult of K-Means Clustering:")
        print(df.sort_values(by="cluster"))

        # Vẽ scatter plot trực quan
        plt.figure(figsize=(8,6))
        for cluster_id in range(k):
            subset = df[df["cluster"] == cluster_id]
            plt.scatter(subset["rental_count"],
                        subset["distinct_film_count"],
                        label=f"Cluster {cluster_id}")

        plt.xlabel("Rental Count")
        plt.ylabel("Distinct Film Count")
        plt.title("Customer Segmentation by Film Interest")
        plt.legend()
        plt.show()

        conn.close()
        print("\nDONE")
