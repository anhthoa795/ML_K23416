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
#2.5 Truy vấn chi tiết thông tin Sinh viên khi biết Id:
cursor = conn.cursor()
sql = "select * from student where ID = 1"

cursor.execute(sql)

dataset = cursor.fetchone()
if dataset!=None:
    id,code,name,age,avatar,intro=dataset
    print("Id=",id)
    print("code=",code)
    print("name=",name)
    print("age=",age)

cursor.close()
print("----------")