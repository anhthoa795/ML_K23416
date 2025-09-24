# import sqlite3
# import pandas as pd
# try:
#     # Connect to DB and create a cursor
#     sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
#     cursor = sqliteConnection.cursor()
#     print('DB Init')
#     # Write a query and execute it with cursor
#     query = 'SELECT * FROM InvoiceLine LIMIT 5;'
#     cursor.execute(query)
#     # Fetch and output result
#     df = pd.DataFrame(cursor.fetchall())
#     print(df)
#     # Close the cursor
#     cursor.close()
# #Handle errors
# except sqlite3.Error as error:
#     print('Error occured -', error)
# #Close DB Connection irrespective of success or failure
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print('sqlite connection closed')

import sqlite3
import pandas as pd

try:
    # Kết nối database
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Truy vấn dữ liệu
    query = 'SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)

    # Lấy dữ liệu và tên cột
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]

    # Tạo DataFrame với tên cột chuẩn
    df = pd.DataFrame(rows, columns=col_names)
    print(df)

    cursor.close()

except sqlite3.Error as error:
    print('Error occurred -', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('sqlite connection closed')
