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
#2.6 Truy vấn dạng phân trang Student (offset3)
cursor = conn.cursor()
sql = "select * from student LIMIT 3 OFFSET 3"
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

#chương trình Paging toàn bộ dữ liệu N dòng sinh viên
print("PAGING!!!!!")
cursor = conn.cursor()
sql = "select count(*) from student"
cursor.execute(sql)
dataset = cursor.fetchone()
rowcount = dataset[0]

limit = 3
step = 3
for offset in range(0, rowcount, step):
    sql = f"select * from student limit {limit} offset {offset}"
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