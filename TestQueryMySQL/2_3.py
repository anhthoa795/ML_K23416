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
"""(2) Lập trình Python truy vấn dữ liệu MySQL Server"""
#2.3 Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần
cursor = conn.cursor()
sql = "SELECT * FROM student order by Age asc"
cursor.execute(sql)
dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format("ID", "Code", "Name", "Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))
cursor.close()
print("----------")