
def read_orders_from_file(file_path):
    try:
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            yield Order(row[0], row[1], row[2], row[3])
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file: {e}")
