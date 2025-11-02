from Transformer import Transformer
class Loader:
    def __init__(self, df):
        self.df = df

    # Ghi báo cáo doanh thu theo ngày ra file daily_revenue.csv
    def load_to_csv(self, filename):
        self.df.to_csv(filename, index=False)
        print(f"Data đã được export thành công ra file {filename}!")

