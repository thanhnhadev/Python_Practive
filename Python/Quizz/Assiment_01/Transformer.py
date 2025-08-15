class Transformer:
    def __init__(self, df):
        self.df = df
        
    # Tổng giá trị giao dịch
    def get_total_transaction_value(self):
        self.df['amount'] = self.df['quantity'] * self.df['unitPrice']
        return self.df
    
    # Chuẩn hóa tên khách hàng (viết hoa chữ cái đầu)
    def customize_name(self):
        self.df['customerName'] = self.df['customerName'].str.title()
        return self.df
    
    # Tính tổng doanh thu theo từng ngày
    def get_total_amount_everyday(self):
        self.df.groupby('transactionDate')['amount'].sum()
        return self.df[['transactionDate', 'amount']]

    # Tính tổng doanh thu theo từng danh mục sản phẩm (category)
    def get_total_amount_by_category(self):
        self.df.groupby('category')['amount'].sum()
        return self.df[['category', 'amount']]

    # Tìm top 3 khách hàng có tổng chi tiêu cao nhất.
    def get_top_3_customers(self):
        self.df.groupby('customerName')['amount'].sum().nlargest(3)
        return self.df[['customerName', 'amount']]