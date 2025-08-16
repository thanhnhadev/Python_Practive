# Xây dựng hệ thống quản lý sinh viên
# Hệ thống cho phép người dùng thêm, xem, tìm kiếm, và xóa thông tin sinh viên.
#
# Student
#
# attribute:
# -student_id: Mã số sinh viên (chuỗi).
# -name: Tên đầy đủ của sinh viên (chuỗi).
# -age: Tuổi của sinh viên (số nguyên).
# -gpa: Điểm trung bình (số thực).
#
# method
# __init__(self, student_id, name, age, gpa)
# __str__(self): Trả về một chuỗi biểu diễn đối tượng Student (in thông tin sinh viên).
# to_dict(self): Trả về một dictionary chứa thông tin của sinh viên
# {'student_id': 'sv001', 'name': 'Nguyen Van A', 'age' : 18, 'gpa': 7.4}
#
# StudentManager
#
# attribute:
# -file_name: Tên file để lưu trữ dữ liệu sinh viên ('students.json')
# -students: danh sách (list) để lưu trữ các đối tượng Student.
#
# method
# init__(self, file_name)
# load_students(self)
# save_students(self)
# add_student(self, student)
# find_student(self, student_id)
# delete_student(self, student_id)
# display_all_students(self)
#
# Chương trình chính (main)
# Tạo một vòng lặp while để hiển thị menu cho người dùng và xử lý các lựa chọn của họ:
#
# 1.Thêm sinh viên mới
# 2.Xem danh sách sinh viên
# 3.Tìm kiếm sinh viên theo ID
# 4.Xóa sinh viên theo ID
# 5.Thoát
# dùng json file để store student
# json.dump(data, f, ensure_ascii=False, indent=4)
# json.dump(student_dicts, f, ensure_ascii=False, indent=4)
import pandas as pd
import json
import os

class StudentManager:
    def __init__(self, file_name="students.json"):

        self.file_name = file_name
        self.df = self.load_students()

    def load_students(self):
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0:
            try:
                df = pd.read_json(self.file_name)
                print("Đã tải dữ liệu sinh viên thành công.")
                return df
            except pd.errors.EmptyDataError:
                print("Lỗi: File JSON rỗng. Khởi tạo DataFrame mới.")
                return pd.DataFrame(columns=['student_id', 'name', 'age', 'gpa'])
            except Exception as e:
                print(f"Lỗi khi tải file JSON: {e}. Khởi tạo DataFrame mới.")
                return pd.DataFrame(columns=['student_id', 'name', 'age', 'gpa'])
        else:
            print("File dữ liệu không tồn tại hoặc trống. Khởi tạo DataFrame mới.")
            return pd.DataFrame(columns=['student_id', 'name', 'age', 'gpa'])

    def save_students(self):
        self.df.to_json(self.file_name, orient='records', indent=4,force_ascii=False)
        print("Đã lưu dữ liệu sinh viên thành công.")

    def add_student(self, student_id, name, age, gpa):
        if student_id in self.df['student_id'].values:
            print(f"Lỗi: Sinh viên với ID '{student_id}' đã tồn tại.")
            return False

        new_data = pd.DataFrame([{
            'student_id': student_id,
            'name': name,
            'age': age,
            'gpa': gpa
        }])

        self.df = pd.concat([self.df, new_data], ignore_index=True)
        print(f"Đã thêm sinh viên '{name}' thành công.")
        self.save_students()
        return True

    def find_student(self, student_id):
        result = self.df[self.df['student_id'] == student_id]
        if not result.empty:
            return result.iloc[0].to_dict()
        else:
            return None

    def delete_student(self, student_id):
        initial_count = len(self.df)
        self.df = self.df[self.df['student_id'] != student_id].reset_index(drop=True)

        if len(self.df) < initial_count:
            print(f"Đã xóa sinh viên với ID '{student_id}' thành công.")
            self.save_students()
            return True
        else:
            print(f"Lỗi: Không tìm thấy sinh viên với ID '{student_id}'.")
            return False

    def display_all_students(self):
        if self.df.empty:
            print("Danh sách sinh viên trống.")
        else:
            print("\n--- DANH SÁCH SINH VIÊN ---")
            print(self.df)
            print("---------------------------\n")


#main.py
def main():
    manager = StudentManager()

    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ SINH VIÊN ---")
        print("1. Thêm sinh viên mới")
        print("2. Xem danh sách sinh viên")
        print("3. Tìm kiếm sinh viên theo ID")
        print("4. Xóa sinh viên theo ID")
        print("5. Thoát")

        choice = input("Vui lòng chọn một tùy chọn (1-5): ")

        if choice == '1':
            print("\n--- THÊM SINH VIÊN ---")
            student_id = input("Nhập mã số sinh viên: ")
            name = input("Nhập tên đầy đủ: ")

            while True:
                try:
                    age = int(input("Nhập tuổi: "))
                    break
                except ValueError:
                    print("Tuổi phải là một số nguyên. Vui lòng nhập lại.")

            while True:
                try:
                    gpa = float(input("Nhập điểm trung bình (GPA): "))
                    if 0 <= gpa <= 10:
                        break
                    else:
                        print("GPA phải từ 0 đến 10. Vui lòng nhập lại.")
                except ValueError:
                    print("GPA phải là một số thực. Vui lòng nhập lại.")

            # check kết quả thêm sinh viên
            success = manager.add_student(student_id, name, age, gpa)
            if not success:
                print("Không thể thêm sinh viên vì mã số đã tồn tại.")
        elif choice == '2':
            manager.display_all_students()

        elif choice == '3':
            print("\n--- TÌM KIẾM SINH VIÊN ---")
            student_id = input("Nhập mã số sinh viên cần tìm: ")
            found_student = manager.find_student(student_id)
            if found_student:
                print("Đã tìm thấy sinh viên:")
                for key, value in found_student.items():
                    print(f"{key}: {value}")
            else:
                print(f"Không tìm thấy sinh viên với ID '{student_id}'.")

        elif choice == '4':
            print("\n--- XÓA SINH VIÊN ---")
            student_id = input("Nhập mã số sinh viên cần xóa: ")
            manager.delete_student(student_id)

        elif choice == '5':
            print("Đang thoát chương trình. Tạm biệt!")
            break

        else:
            print("Tùy chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 5.")

if __name__ == "__main__":
    main()
