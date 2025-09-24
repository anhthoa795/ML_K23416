import sqlite3
import pandas as pd

def top_n_customers_by_contribution(db_path: str, top_n: int):
    """
    Trả về top_n khách hàng có tổng trị giá (tổng tiền đã chi) cao nhất.
    Kết quả gồm: CustomerId, CustomerName, TotalContribution.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("DB Init")

        query = """
            SELECT 
                c.CustomerId,
                c.FirstName || ' ' || c.LastName AS CustomerName,
                SUM(i.Total) AS TotalContribution
            FROM Customer c
            JOIN Invoice i ON c.CustomerId = i.CustomerId
            GROUP BY c.CustomerId
            ORDER BY TotalContribution DESC
            LIMIT ?;
        """

        cursor.execute(query, (top_n,))
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(rows, columns=col_names)
        return df

    except sqlite3.Error as e:
        print("Error:", e)
        return None
    finally:
        if conn:
            conn.close()
            print("sqlite connection closed")


# ------------------ Chạy chương trình ------------------
db_path = '../databases/Chinook_Sqlite.sqlite'

# Bé nhập số lượng khách hàng muốn lấy
top_n = int(input("Nhập số lượng khách hàng (Top N): "))

result = top_n_customers_by_contribution(db_path, top_n)
print("\nTop", top_n, "khách hàng đóng góp nhiều tiền nhất:")
print(result)
