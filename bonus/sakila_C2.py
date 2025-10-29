import mysql.connector


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
#C2
def customersByCategory(conn):
    sql = """
        SELECT DISTINCT
            ct.name AS category_name,
            c.customer_id,
            CONCAT(c.first_name, ' ', c.last_name) AS customer_name
        FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category ct ON fc.category_id = ct.category_id
        JOIN customer c ON r.customer_id = c.customer_id
        ORDER BY ct.name, customer_name;
    """

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    category_dict = {}

    # Gom nhóm khách theo Category
    for category, cid, cname in rows:
        if category not in category_dict:
            category_dict[category] = []
        category_dict[category].append((cid, cname))

    # Xuất ra Console
    print("\n========== CUSTOMER GROUPING BY CATEGORY ==========\n")

    for category, customers in category_dict.items():
        print(f"Category: {category}")
        print(f"Total Customers: {len(customers)}")
        print("-" * 60)

        for cid, cname in customers:
            print(f"{cid:<10} {cname}")

        print("-" * 60 + "\n")

    cursor.close()
if __name__ == "__main__":
    conn = getConnect("localhost", 3306, "sakila", "root", "thoalalen792005")
    if conn:
        customersByCategory(conn)
        conn.close()
        print("DONE")