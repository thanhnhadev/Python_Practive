# Xây dựng pipeline xử lý ETL từ nguồn dữ liệu là 1 file csv như sau 

# id,name,email,salary
# 1,Nguyen Van A,a@example.com,1000
# 2,Tran Thi B,b@example.com,1500
# 3,Le Van C,c@example.com,1200

# Biến đổi nó thành dạng file excel 

# id name email salary tax net_salary
# 1 Nguyen Van A a@example.com 1000 100.0 900.0
# 2 Tran Thi B b@example.com 1500 150.0 1350.0
# 3 Le Van C c@example.com 1200 120.0 1080.0

# Từ danh sách ban đầu chỉ lấy dữ liệu có salary > =1000, thêm vào col Tax và net salary

# Tax = salary * 0.1

# Net = salary - tax

# Yêu cầu : Xây dựng class Extractor , Transformer , Loader
import pandas as pd
data={
    'id':[1,2,3],
    'name':['Nguyen Van A','Tran Thi B','Le Van C'],
    'email':['a@example.com','b@example.com','c@example.com'],
    'salary':[1000,1500,1200]
}
df=pd.DataFrame(data)
df.head()
print(df)
df['tax']=df['salary']*0.1
df['Net']=df['salary']-df['tax']
print(df)
df.to_csv(r'output.csv',index=False)
print(df.head(5))

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
