def order_report_generator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("--- Báo cáo doanh số ---")

        order_generator = func(*args, **kwargs)
        product_quantities = defaultdict(int)
        product_prices = {}
        product_revenues = defaultdict(float)
        total_revenue = 0.0

        for order in order_generator:
            product_quantities[order.product_name] += order.quantity
            product_prices[order.product_name] = order.price_per_unit
            revenue = order.quantity * order.price_per_unit
            product_revenues[order.product_name] += revenue
            total_revenue += revenue

        print("\nThống kê số lượng theo sản phẩm:")
        for product, quantity in product_quantities.items():
            print(f"  - {product}: {quantity}")

        print("\nThống kê giá bán theo sản phẩm:")
        for product, price in product_prices.items():
            print(f"  - {product}: ${price:,.2f}")

        print("\nThống kê tổng tiền theo sản phẩm:")
        for product, revenue in product_revenues.items():
            print(f"  - {product}: ${revenue:,.2f}")

        print(f"\nTổng doanh thu: ${total_revenue:,.2f}")

        print("\n--- Kết thúc báo cáo ---")
        return None
    return wrapper
# decorate to report
@order_report_generator
def process_order_file(file_path):
    print(f"Bắt đầu xử lý file: {file_path}...")
    return read_orders_from_file(file_path)