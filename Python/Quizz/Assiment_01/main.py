# transactionId,customerId,customerName,product,category,quantity,unitPrice,transactionDate
# T001,C001,john doe,Laptop,Electronics,1,1200,2023-07-01
# T002,C002,Jane smith,Mouse,Accessories,2,25,2023-07-01
# T003,C001,John Doe,Keyboard,Accessories,1,75,2023-07-02
# T004,C003,emily Davis,Laptop,Electronics,1,1150,2023-07-03
# T005,C002,Jane Smith,Laptop,Electronics,1,1190,2023-07-03
# T006,C004,Alex Nguyen,Monitor,Electronics,2,300,2023-07-04

# Extract
# - Đọc dữ liệu từ file transactions.csv bằng pandas.
# - Xử lý lỗi nếu file không tồn tại
# Transform
# - Tính tổng giá trị giao dịch (quantity * unit_price) cho mỗi dòng.
# - Chuẩn hóa tên khách hàng (viết hoa chữ cái đầu).
# - Tính tổng doanh thu theo từng ngày.
# - Tính tổng doanh thu theo từng danh mục sản phẩm (category).
# - Tìm top 3 khách hàng có tổng chi tiêu cao nhất.
#  Load
# - Ghi báo cáo doanh thu theo ngày ra file daily_revenue.csv.
# - Ghi báo cáo doanh thu theo danh mục ra file category_revenue.csv.
# - Ghi danh sách top 3 khách hàng ra file top_customers.csv.
import pandas as pd
from Transformer import Transformer
from Loader import Loader
from Extract import Extract
import os
import pandas as pd

class Extractor:
    def __init__(self, filepath):
        self.filepath = filepath

    def preprocess_input(self):
        """Thực hiện các yêu cầu: tính totalValue và chuẩn hóa tên khách hàng trên file input."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Không tìm thấy file: {self.filepath}")

        df = pd.read_csv(self.filepath)

        # Tính tổng giá trị giao dịch (quantity * unit_price hoặc unitPrice)
        if 'unit_price' in df.columns:
            df['totalValue'] = df['quantity'] * df['unit_price']
        elif 'unitPrice' in df.columns:
            df['totalValue'] = df['quantity'] * df['unitPrice']
        else:
            raise KeyError("Không tìm thấy cột 'unit_price' hoặc 'unitPrice' trong file CSV.")

        # Chuẩn hóa tên khách hàng (viết hoa chữ đầu, các chữ sau thường)
        df['customerName'] = df['customerName'].str.title()

        # Ghi đè lại file input
        df.to_csv(self.filepath, index=False, encoding='utf-8-sig')
        print(f"✅ Đã cập nhật file input: {self.filepath}")

    def extract(self):
        return pd.read_csv(self.filepath)


class Transformer:
    def __init__(self, df):
        self.df = df

    def transform(self):
        df_copy = self.df.copy()

        # Tính tổng doanh thu theo ngày
        daily_revenue = df_copy.groupby('transactionDate')['totalValue'].sum().reset_index()
        daily_revenue.rename(columns={'totalValue': 'dailyRevenue'}, inplace=True)

        # Tính tổng doanh thu theo danh mục
        category_revenue = df_copy.groupby('category')['totalValue'].sum().reset_index()
        category_revenue.rename(columns={'totalValue': 'categoryRevenue'}, inplace=True)

        # Top 3 khách hàng chi tiêu nhiều nhất
        customer_spending = df_copy.groupby(['customerId', 'customerName'])['totalValue'].sum().reset_index()
        customer_spending.rename(columns={'totalValue': 'totalSpending'}, inplace=True)
        top_customers = customer_spending.sort_values(by='totalSpending', ascending=False).head(3)

        return daily_revenue, category_revenue, top_customers

class Loader:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def load(self, daily_revenue, category_revenue, top_customers):
        daily_revenue.to_csv(os.path.join(self.output_dir, "daily_revenue.csv"), index=False)
        category_revenue.to_csv(os.path.join(self.output_dir, "category_revenue.csv"), index=False)
        top_customers.to_csv(os.path.join(self.output_dir, "top_customers.csv"), index=False)


if __name__ == "__main__":
    input_path = r"C:\Users\Admin\Desktop\Python_Practive\Python\Quizz\Assiment_01\input01.csv"
    output_dir = r"C:\Users\Admin\Desktop\Python_Practive\Python\Quizz\Assiment_01"

    try:
        # Extract + Preprocess file input
        extractor = Extractor(input_path)
        extractor.preprocess_input()
        raw_data = extractor.extract()

        # Transform
        daily_revenue, category_revenue, top_customers = Transformer(raw_data).transform()

        # Load
        Loader(output_dir).load(daily_revenue, category_revenue, top_customers)

        print("✅ ETL pipeline hoàn thành. Các file báo cáo đã được lưu trong thư mục:", output_dir)

    except FileNotFoundError as e:
        print("Lỗi:", e)
    except Exception as e:
        print("Đã xảy ra lỗi:", e)