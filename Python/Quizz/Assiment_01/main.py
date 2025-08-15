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
file_name = 'transactions.csv'
# Tạo đối tượng Extractor
extractor = Extractor(file_name)
df = extractor.get_data()

print(df)
# Tạo đối tượng Transformer
transformer = Transformer(df)
df = transformer.get_total_transaction_value()
df = transformer.customize_name()

# Tạo đối tượng Transformer
transformer = Transformer(df)
dfTotal = transformer.get_total_amount_everyday()
dfCategory = transformer.get_total_amount_by_category()
dfTopCustomers = transformer.get_top_3_customers()
# Tạo đối tượng Loader

# Ghi báo cáo doanh thu theo ngày
loader = Loader(dfTotal)
loader.load_to_csv('daily_revenue.csv')

# Ghi báo cáo doanh thu theo danh mục
loader = Loader(dfCategory)
loader.load_to_csv('category_revenue.csv')

# Ghi danh sách top 3 khách hàng
loader = Loader(dfTopCustomers)
loader.load_to_csv('top_customers.csv')