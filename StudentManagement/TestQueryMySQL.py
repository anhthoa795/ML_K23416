import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="thoalalen792005",
        database="studentmanagement"
    )
    print("✅ Kết nối MySQL thành công!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for table in cursor.fetchall():
        print(table)
    conn.close()
except Exception as e:
    print("❌ Lỗi MySQL:", e)
