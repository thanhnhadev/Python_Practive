# bài tập về nhà: Xây Dựng Hệ Thống Quản Lý Thư Viện Đơn Giản
# Mô tả: Xây dựng một hệ thống quản lý thư viện đơn giản bằng Python. 
# Hệ thống cần có khả năng quản lý các loại sách khác nhau, bao gồm Sách Giáo Khoa (Textbook) và Sách Tiểu Thuyết (Novel) xử lý việc mượn/trả sách.
# Yêu Cầu Chi Tiết:
# 1. Abstraction (Tính trừu tượng)
# •	Tạo một lớp trừu tượng tên là Item (abc.ABC).
# •	Lớp Item này phải có các thuộc tính chung cho tất cả các loại sách: title (tiêu đề), author (tác giả), và available (trạng thái sẵn có, mặc định là True).
# •	Lớp Item phải có một phương thức trừu tượng tên là display_info(). Phương thức này sẽ hiển thị thông tin chi tiết của sách.
# 2. Inheritance (Tính kế thừa)
# •	Tạo hai lớp con kế thừa từ Item:
# o	Textbook: Sách giáo khoa, có thêm thuộc tính subject (môn học).
# o	Novel: Sách tiểu thuyết, có thêm thuộc tính genre (thể loại).
# •	Mỗi lớp con phải triển khai phương thức display_info() của riêng mình để hiển thị thông tin đầy đủ, bao gồm cả thuộc tính đặc thù của nó.
# 3. Encapsulation (Tính đóng gói)
# •	Trong lớp Item và các lớp con, thuộc tính available phải được bảo vệ khỏi việc thay đổi trực tiếp từ bên ngoài.
# •	Tạo các phương thức công khai (public methods) để thay đổi trạng thái available một cách an toàn:
# o	borrow(): Chuyển trạng thái available thành False nếu sách đang có sẵn.
# o	return_item(): Chuyển trạng thái available thành True nếu sách đang được mượn.
# •	Hãy sử dụng quy ước đặt tên của Python (_ hoặc __) để thể hiện tính đóng gói này.
# 4. Polymorphism (Tính đa hình)
# •	Viết một hàm process_library_item(item) bên ngoài các class.
# •	Hàm này nhận vào một đối tượng bất kỳ thuộc lớp Item hoặc các lớp con của nó.
# •	Trong hàm, gọi phương thức display_info() của đối tượng đó.
# •	Nhờ tính đa hình, hàm này sẽ tự động gọi đúng phương thức display_info() của Textbook hoặc Novel tùy thuộc vào loại đối tượng được truyền vào.
# 5. Kết hợp và Chạy chương trình
# •	Khởi tạo một vài đối tượng Textbook và Novel.
# •	Sử dụng hàm process_library_item() để hiển thị thông tin của các đối tượng này.
# •	Thực hiện một số thao tác mượn/trả sách bằng các phương thức borrow() và return_item() để kiểm tra tính đóng gói.
from textbook import Textbook
from novel import Novel

def process_library_item(item):
    item.display_info()

if __name__ == "__main__":
    book1 = Textbook("Toán 12", "Nguyễn Văn A", "Toán học")
    book2 = Novel("Đắc Nhân Tâm", "Dale Carnegie", "Tâm lý học")
    book3 = Textbook("Vật Lý 10", "Trần Văn B", "Vật lý")
    book4 = Novel("Harry Potter", "J.K. Rowling", "Fantasy")

    print("Thông tin sách ban đầu:")
    for book in [book1, book2, book3, book4]:
        process_library_item(book)

    print("\nThao tác mượn sách:")
    book1.borrow()
    book2.borrow()

    print("\nThông tin sau khi mượn:")
    for book in [book1, book2]:
        process_library_item(book)

    print("\nThao tác trả sách:")
    book1.return_item()
    book2.return_item()

    print("\nThông tin sau khi trả:")
    for book in [book1, book2]:
        process_library_item(book)
