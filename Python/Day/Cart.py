class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_cost(self):
        return sum(item.total_price() for item in self.items)

    def __eq__(self, other):
        return self.total_cost() == other.total_cost()

    def __add__(self, other):
        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart

    def __str__(self):
        if not self.items:
            return "Giỏ hàng trống."
        output = ["Danh sách sản phẩm trong giỏ:"]
        for item in self.items:
            output.append(str(item))
        output.append(f"Tổng tiền: {self.total_cost():,.0f} VND")
        return "\n".join(output)
