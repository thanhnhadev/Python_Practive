# Xây dựng một pipeline xử lý danh sách sinh viên theo phong cách functional, không dùng vòng lặp for,
# không thay đổi trạng thái (no mutation), và không dùng class.
from functools import reduce
students = [
    {'name': 'An', 'score': 8.5, 'major': 'CS'},
    {'name': 'Binh', 'score': 6.0, 'major': 'Math'},
    {'name': 'Chi', 'score': 9.0, 'major': 'CS'},
    {'name': 'Dung', 'score': 5.5, 'major': 'Physics'},
    {'name': 'Hoa', 'score': 7.5, 'major': 'Math'},
]
# Yêu Cầu
# - Lọc ra các sinh viên ngành "CS" có điểm >= 8.0.
# Lọc ra các nhân viên ở vị trí "Developer".
# - Chuyển đổi danh sách thành dạng: ["An (8.5)", "Chi (9.0)"].
# - Sắp xếp theo điểm giảm dần.
# - Tính trung bình điểm của các sinh viên đã lọc.
# - Không dùng vòng lặp, chỉ dùng map, filter, reduce, sorted, lambda.
# from functools import reduce
# - Lọc ra các sinh viên ngành "CS" có điểm >= 8.0.
filtered_students = filter(lambda s: s['major'] == 'CS' and s['score'] >= 8.0, students)
#  Sắp xếp theo score giảm dần
sorted_students = sorted(filtered_students, key=lambda s: s['score'], reverse=True)
#  Chuyển thành dạng "Tên (điểm)"
formatted_students = list(map(lambda s: f"{s['name']} ({s['score']})", sorted_students))
#  Tính trung bình điểm
avg_score = reduce(lambda acc, s: acc + s['score'], sorted_students, 0) / len(sorted_students)
# Kết quả
print("Danh sách sau xử lý:", formatted_students)
print("Điểm trung bình:", avg_score)