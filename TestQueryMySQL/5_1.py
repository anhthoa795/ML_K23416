import mysql.connector
#Lập trình Python kết nối MySQL Server
server = "localhost"
port = 3306
database = "studentmanagement"
username = "root"
password = "thoalalen792005"
conn = mysql.connector.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    passwd=password)
"""(5) Lập trình Python xóa dữ liệu MySQL Server"""
#(5.1) Xóa Student có ID=14
conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql="DELETE from student where ID=14"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount," record(s) affected")

