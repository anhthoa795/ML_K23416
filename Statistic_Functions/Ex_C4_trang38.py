import pandas as pd

def filter_orders_by_value(df: pd.DataFrame, minValue: float, maxValue: float, sortType: bool) -> pd.DataFrame:
    """
    Trả về danh sách các hóa đơn (OrderID + tổng giá trị) mà tổng trị giá nằm trong [minValue, maxValue],
    sắp xếp tăng dần nếu sortType=True, ngược lại giảm dần.

    Parameters
    ----------
    df : DataFrame
        DataFrame chứa các cột: OrderID, UnitPrice, Quantity, Discount
    minValue : float
        Tổng giá trị tối thiểu
    maxValue : float
        Tổng giá trị tối đa
    sortType : bool
        True = sắp xếp tăng dần, False = giảm dần
    """
    # Đảm bảo kiểu dữ liệu số
    for col in ['UnitPrice', 'Quantity', 'Discount']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Tính tổng trị giá từng hóa đơn
    order_sum = (
        df.assign(Total=df['UnitPrice'] * df['Quantity'] * (1 - df['Discount']))
          .groupby('OrderID')['Total']
          .sum()
          .reset_index(name='Sum')
    )

    # Lọc theo khoảng min-max
    order_sum = order_sum[(order_sum['Sum'] >= minValue) & (order_sum['Sum'] <= maxValue)]

    # Sắp xếp theo yêu cầu
    order_sum = order_sum.sort_values(by='Sum', ascending=sortType).reset_index(drop=True)

    return order_sum

# ------------------- Chạy chương trình -------------------
df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')
minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
sortType = input("Sắp xếp tăng dần? (True/False): ").strip().lower() == 'true'

result = filter_orders_by_value(df, minValue, maxValue, sortType)
print("\nDanh sách các hóa đơn thỏa điều kiện:")
print(result)
