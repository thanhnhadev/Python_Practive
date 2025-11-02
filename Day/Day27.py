# Quản lý Giỏ Hàng
# Hãy xây dựng một lớp Item, Cart để quản lý các mặt hàng, giỏ hàng.
# Yêu cầu:
# - Tạo lớp Item với các thuộc tính: name, price, quantity.
# - Tạo lớp Cart có thể:
#  - Thêm mặt hàng (add_item)
#  - Tính tổng tiền (total_cost)
#  - So sánh hai giỏ (__eq__)
#  - Gộp 2 giỏ hàng (__add__)
#  - Hiển thị thông tin giỏ hàng (__str__)
# "\n".join(output)
from Item import Item
from Cart import Cart


def main():
    sp1 = Item("tao", 20000, 2)
    sp2 = Item("chuoi", 30000, 1)
    sp3 = Item("Mũ lưỡi trai", 80000, 3)
    cart1 = Cart()
    cart1.add_item(sp1)
    cart1.add_item(sp2)
    cart2 = Cart()
    cart2.add_item(sp3)
    print(" Giỏ hàng 1:")
    print(cart1)
    print("\n Giỏ hàng 2:")
    print(cart2)

    # So sánh
    print("\n Hai giỏ có cùng tổng tiền?", "✅" if cart1 == cart2 else "❌")

    # Gộp 2 giỏ hàng
    cart3 = cart1 + cart2
    print("\nGiỏ hàng sau khi gộp:")
    print(cart3)


if __name__ == "__main__":
    main()

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

class Item:
    def __init__(self,name, price, quantity):
       
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Giá: {self.price:,.0f} VNĐ, SL: {self.quantity})"

    def total_price(self):
        return self.price * self.quantity