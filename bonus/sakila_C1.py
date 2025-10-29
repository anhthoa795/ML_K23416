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


# C1: Hàm phân loại khách theo từng phim đã thuê
def customersByFilm(conn):
    sql = """
          SELECT f.title                                AS film_title, \
                 c.customer_id, \
                 CONCAT(c.first_name, ' ', c.last_name) AS customer_name
          FROM rental r
                   JOIN inventory i ON r.inventory_id = i.inventory_id
                   JOIN film f ON i.film_id = f.film_id
                   JOIN customer c ON r.customer_id = c.customer_id
          ORDER BY f.title, customer_name; \
          """

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    film_dict = {}

    # Gom nhóm khách theo từng phim
    for film, cid, cname in rows:
        if film not in film_dict:
            film_dict[film] = []
        film_dict[film].append((cid, cname))

    # Xuất ra console đẹp và rõ ràng
    print("\n========== CUSTOMER GROUPING BY FILM ==========\n")

    for film, customers in film_dict.items():
        print(f"Film: {film}")
        print(f"Total Customers: {len(customers)}")
        print("-" * 60)

        for cid, cname in customers:
            print(f"{cid:<10} {cname}")

        print("-" * 60 + "\n")

    cursor.close()


# Chạy chính
if __name__ == "__main__":
    conn = getConnect("localhost", 3306, "sakila", "root", "thoalalen792005")
    if conn:
        customersByFilm(conn)
        conn.close()
        print("DONE")


