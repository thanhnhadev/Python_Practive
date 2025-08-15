# Cho danh sách các từ, lọc ra những từ có độ dài > 3 và chuyển tất cả sang chữ in hoa.
#  -> ["ELEPHANT", "GIRAFFE"]
# Larger3AndUppercase =  [word.upper() for word in words if len(word) > 3]
# words = ["cat", "elephant", "dog", "giraffe", "rat"];
# word= filter(lambda a: len(a) > 3, words)
# e= map(lambda x: x.upper(), word)
# print(list(e))
# print(Larger3AndUppercase)

products = [
    ("Áo thun", 150000),
    ("Quần jeans", 350000),
    ("Giày thể thao", 500000),
    ("Mũ lưỡi trai", 80000)
]

# Dùng map biến đổi ra danh sách mới có dạng ["Sản phẩm: Áo thun - Giá: 165,000 VND",...]
# Giá mới bằng giá cũ * 10%
product=map(lambda x: f"san pham: {x[0]} - Gia: {float(x[1])*1.1: .1f} vnd", products)
print(list(product))

# for i in range(n):
#     ten = input(f"Nhập tên sản phẩm thứ {i+1}: ");
#     gia = float(input(f"Nhập giá của '{ten}' (VND): "));
#     products.append((ten, gia));

# UpdatePriceOfProducts = list(map(
#     lambda p: f"Sản phẩm: {p[0]} - Giá: {float(p[1] * 1.1):,} VND",
#     products
# ))
# print("\nDanh sách sản phẩm sau khi tăng giá 10%:")
# print(UpdatePriceOfProducts);