import pandas as pd
def top3_products_by_sales_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trả về top 3 sản phẩm (ProductID) có tổng trị giá bán ra lớn nhất.
    Trị giá = UnitPrice * Quantity * (1 - Discount)
    """
    # Đảm bảo cột số là kiểu numeric
    for col in ['UnitPrice', 'Quantity', 'Discount']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Tính trị giá cho từng dòng
    df['SalesValue'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])

    # Gom theo ProductID, cộng trị giá, sắp giảm dần và lấy 3 sản phẩm đầu
    top3 = (
        df.groupby('ProductID')['SalesValue']
          .sum()
          .sort_values(ascending=False)
          .head(3)
          .reset_index()
    )
    return top3
df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')
result = top3_products_by_sales_value(df)
print("Top 3 sản phẩm có tổng trị giá bán ra lớn nhất:")
print(result)
