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
