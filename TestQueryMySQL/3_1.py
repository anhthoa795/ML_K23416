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
"""(3) Lập trình Python thêm mới dữ liệu MySQL Server:"""
#(3.1) Thêm mới 1 Student
cursor = conn.cursor()

sql="insert into student (code,name,age) values (%s,%s,%s)"

val=("sv07","Trần Duy Thanh",45)

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record inserted")

cursor.close()
