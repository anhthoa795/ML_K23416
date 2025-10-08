import traceback

import mysql.connector

server="localhost"
port=3306
database="k23416_retail"
username="root"
password="thoalalen792005"
try:
    conn = mysql.connector.connect(
                    host=server,
                    port=port,
                    database=database,
                    user=username,
                    password=password)
except:
    traceback.print_exc()
print("---Tiếp tục phần mềm---") #có try except thì dù lỗi nó qlai nó chạy tiếp print, còn hông có thì nó bị crash
print("--CRUD----")
#Câu 1: Đăng nhập cho Customer
def login_customer(email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
          "WHERE Email = '" + email + "' and Password = '" + pwd + "'"
    print(sql)
    cursor.execute(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failded!")
    cursor.close()
login_customer("hocamdao@gmail.com", "123")

def login_employee(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee " \
          "WHERE Email = %s and Password = %s"
    val = (email,pwd)
    cursor.execute(sql, val)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failded!")
    cursor.close()
login_employee("obama@gmail.com", "123")