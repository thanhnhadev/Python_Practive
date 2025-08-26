# Tạo một decorator có tên permission để kiểm tra xem một người dùng có quyền cần thiết để chạy một hàm hay không

# yêu cầu: 
# -xây dựng class User (username, role)
# -permission nhận một tham số là chuỗi required_role ('admin', 'editor')
# -Hàm wrapper sẽ kiểm tra xem user có role có khớp với required_role hay không.
# Nếu quyền hợp lệ, thực thi hàm gốc và trả về kết quả.
# Nếu quyền không hợp lệ, in ra một thông báo lỗi (ví dụ: "Lỗi: Bạn không có quyền truy cập.") và không thực thi hàm gốc.
# -Áp dụng decorator requires_permission cho hai hàm: delete (chỉ dành cho 'admin') và edit(dành cho 'admin' và 'editor')
from user import User
from requires_permission import requires_permission

@requires_permission(['admin'])
def delete(user):
    print(f"{user.username} đã xóa dữ liệu.")

@requires_permission(['admin', 'editor'])
def edit(user):
    print(f"{user.username} đã chỉnh sửa dữ liệu.")

# Ví dụ kiểm thử
if __name__ == "__main__":
    admin_user = User("thanh nhã", "admin")
    editor_user = User("Tuân Úc", "editor")
    viewer_user = User("Dân thường", "viewer")

    delete(admin_user)
    delete(editor_user)
    edit(editor_user)
    edit(viewer_user)

