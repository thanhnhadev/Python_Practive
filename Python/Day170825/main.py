# Xử lý dữ liệu nhân viên
# Cho một danh sách các nhân viên, mỗi nhân viên là một dictionary chứa name, role và salary.
# Thực hiện các tác vụ sau:
# Lọc ra các nhân viên ở vị trí "Developer".
# Tính toán mức lương thưởng cho mỗi nhân viên đủ điều kiện (thưởng 10% nếu lương trên 6000).
# Sắp xếp danh sách nhân viên theo mức lương mới từ cao xuống thấp.
# new_list = sorted(list, key (function), reverse=True)

# Lọc ra các nhân viên theo vị trí
# def filter_employees_by_role(employees, role):
#     employees_in_role = list(filter(lambda emp: emp['role'] == role, employees))
#     return employees_in_role
# # Lọc ra các nhân viên ở vị trí "Developer".
# print("Nhân viên ở vị trí Developer:")
# print(filter_employees_by_role(employees, 'Developer'))
# ## Lọc ra các nhân viên theo lương
# def filter_employees_by_role(employees, salary):
#     return list(filter(lambda emp: emp['salary'] >= int(salary), employees))
# def bonus_employees(employees):
#     eligible_employees = filter_employees_by_role(employees, 6000)
#     # Tính toán mức lương thưởng cho mỗi nhân viên đủ điều kiện (thưởng 10% nếu lương trên 6000).
#     list(map(lambda emp: emp.update({'salary': int(emp['salary'] * 1.1)}), eligible_employees))
#     return eligible_employees
# print("Nhân viên đủ điều kiện nhận thưởng:")
# # Sắp xếp danh sách nhân viên theo mức lương mới từ cao xuống thấp.
# print(sorted(bonus_employees(employees), key=lambda emp: emp['salary'], reverse=True))

import pandas as pd
employees = [
    {'name': 'Alice', 'role': 'Developer', 'salary': 7000},
    {'name': 'Bob', 'role': 'Manager', 'salary': 9000},
    {'name': 'Charlie', 'role': 'Developer', 'salary': 5500},
    {'name': 'David', 'role': 'Analyst', 'salary': 6500},
    {'name': 'Eve', 'role': 'Developer', 'salary': 8000}
]
# sắp xếp dùng hàm sorted
sorted_devs = sorted(
    map(
        # Tính toán mức lương thưởng cho mỗi nhân viên đủ điều kiện (thưởng 10% nếu lương trên 6000).
        lambda e: {**e, 'new_salary': e['salary'] * 1.1 if e['salary'] > 6000 else e['salary']},
        # Lọc ra các nhân viên ở vị trí "Developer".
        filter(lambda e: e['role'] == 'Developer', employees)
    ),
    key=lambda e: e['new_salary'],reverse=True
)
df = pd.DataFrame(sorted_devs)
print(df)