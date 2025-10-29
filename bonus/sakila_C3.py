import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from flask import Flask, render_template_string, request
import os
import webbrowser
import threading

app = Flask(__name__)

# Kết nối DB
def getConnect():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        database="sakila",
        user="root",
        password="thoalalen792005"
    )

# Lấy dữ liệu ML
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
    return pd.read_sql(sql, conn)

# Load DB + Training
conn = getConnect()
df = getCustomerInterestData(conn)

X = df[['rental_count', 'distinct_film_count']].values

# KMeans
k = 4
model = KMeans(n_clusters=k, random_state=42)
df["cluster"] = model.fit_predict(X)

# Tạo thư mục hình ảnh
os.makedirs("static", exist_ok=True)

# Vẽ Elbow
inertia = []
for c in range(1, 11):
    km = KMeans(n_clusters=c, random_state=42)
    km.fit(X)
    inertia.append(km.inertia_)

plt.figure()
plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method - Customer Film Interest")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.savefig("static/elbow.png")
plt.close()

# Scatter Plot
plt.figure()
for cid in range(k):
    data_subset = df[df["cluster"] == cid]
    plt.scatter(data_subset["rental_count"], data_subset["distinct_film_count"], label=f"Cluster {cid}")
plt.title("Customer Segmentation by Film Interest")
plt.xlabel("Rental Count")
plt.ylabel("Distinct Film Count")
plt.legend()
plt.savefig("static/cluster.png")
plt.close()

# Hàm tải dữ liệu chi tiết từng cụm
def getClusterDetails(conn):
    cursor = conn.cursor()
    cluster_info = {}
    col_names = []

    for cid in sorted(df["cluster"].unique()):
        ids = df[df["cluster"] == cid]["customer_id"].tolist()
        sql = f"SELECT customer_id, first_name, last_name, email FROM customer WHERE customer_id IN ({','.join(map(str, ids))})"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cluster_info[cid] = rows
        col_names = [desc[0] for desc in cursor.description]

    return cluster_info, col_names

# Routes
@app.route("/")
def home():
    return """
    <h1>Customer Clustering System</h1>
    <a href='/dashboard'>Xem dashboard phân cụm</a><br><br>
    <a href='/check_customer'>Tra cứu khách hàng theo ID</a><br><br>
    <a href='/select_cluster'>Xem danh sách từng cụm</a>
    """

@app.route("/dashboard")
def dashboard():
    return """
    <h2>Dashboard phân cụm khách hàng</h2>
    <img src='/static/elbow.png' width='600'><br><br>
    <img src='/static/cluster.png' width='600'><br><br>
    <a href='/'>Về trang chủ</a>
    """

@app.route("/check_customer")
def check_customer():
    customer_id = request.args.get("id")

    if not customer_id:
        return """
        <h2>Tra cứu khách hàng theo Customer ID</h2>
        <form method='get'>
            <input type='number' name='id' placeholder='Customer ID...' required>
            <button type='submit'>Check</button>
        </form>
        <br>
        <a href='/'>Về trang chủ</a>
        """

    cid = int(customer_id)
    if cid not in df["customer_id"].values:
        return f"""
        <h3>Customer ID {cid} không tồn tại</h3>
        <a href='/check_customer'>Thử lại</a> |
        <a href='/'>Về trang chủ</a>
        """

    cluster = int(df[df["customer_id"] == cid]["cluster"].values[0])
    return f"""
        <h2>Kết quả tra cứu</h2>
        <p><b>Customer ID:</b> {cid}</p>
        <p><b>Thuộc Cluster:</b> {cluster}</p>
        <a href='/check_customer'>Kiểm tra khách khác</a> |
        <a href='/'>Về trang chủ</a>
    """

@app.route("/select_cluster")
def select_cluster():
    options = "".join([f"<option value='{c}'>{c}</option>" for c in sorted(df['cluster'].unique())])
    return f"""
    <h2>Chọn Cluster để xem danh sách khách hàng</h2>
    <form action='/show_cluster'>
        <select name='cid'>{options}</select>
        <button type='submit'>Xem</button>
    </form>
    <br>
    <a href='/'>Về trang chủ</a>
    """

@app.route("/show_cluster")
def show_cluster():
    cid = int(request.args.get("cid"))
    cluster_info, col_names = getClusterDetails(conn)

    rows = cluster_info[cid]

    html = f"<h2>Danh sách khách hàng thuộc cluster {cid}</h2>"
    html += "<table border=1><tr>"
    for col in col_names:
        html += f"<th>{col}</th>"
    html += "</tr>"

    for row in rows:
        html += "<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>"

    html += "</table><br><a href='/'>Về trang chủ</a>"
    return html

# Auto open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, use_reloader=False)
