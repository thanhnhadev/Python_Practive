# --- Các danh sách ký tự để tạo mật khẩu ---
import random
# Danh sách các chữ cái (bao gồm cả chữ hoa và chữ thường)
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Danh sách các chữ số
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Danh sách các ký tự đặc biệt
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# --- Bắt đầu chương trình ---

# In lời chào mừng
print("Chào mừng bạn đến với Trình tạo mật khẩu PyPassword!")

# --- Lấy thông tin từ người dùng ---

# Hỏi người dùng muốn bao nhiêu chữ cái và chuyển đổi đầu vào thành số nguyên
nt_letters = int(input("Bạn muốn mật khẩu có bao nhiêu chữ cái?\n"))

# Hỏi người dùng muốn bao nhiêu ký tự đặc biệt
nr_symbols = int(input("Bạn muốn mật khẩu có bao nhiêu ký tự đặc biệt?\n"))

# Hỏi người dùng muốn bao nhiêu chữ số
nr_numbers = int(input("Bạn muốn mật khẩu có bao nhiêu chữ số?\n"))

# (Phần tiếp theo của chương trình sẽ sử dụng các biến trên để tạo mật khẩu)
# easy
password = ""
# nt_letters =4
for char in range(0,nt_letters ):
    #1-4
    password +=random.choice(letter)

for char in range(0, nr_symbols):
    password +=random.choice(symbols)

for char in range(0, nr_numbers):
    password +=random.choice(numbers)
print(password)
print("------------------------------------")
# hard
password_list = []
# nt_letters =4
for char in range(0,nt_letters ):
    #1-4
    password_list.append(random.choice(letter))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
passwords =""
for char in password_list:
    passwords += char
print(f"your password in: {password}")