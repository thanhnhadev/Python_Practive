# import random

# so_dung = random.randint(1, 10)

# Bài tập với break và continue
# Tìm số đầu tiên lớn hơn 100 chia hết cho cả 7 và 13
# i=101 
# while(True):
#     if i % 7==0 and i % 13==0:
#         print(i)
#         break
#     i+=1;
#  Bài tập về while loop- Trò chơi đoán số
# Sinh một số ngẫu nhiên từ 1 đến 10. Cho người dùng đoán đến khi đúng (gợi ý dùng random.randint()).

#  Bài tập về for loop
# - Tính tổng các số chia hết cho 3 từ 1 đến 100
# Dùng vòng lặp for để cộng tất cả các số chia hết cho 3 trong khoảng này.
# tong = 0
# for i in range(1, 101):  
#     if i % 3 == 0:       
#         tong += i        
# print(f"Tổng các số chia hết cho 3 từ 1 đến 100 là: {tong}")
# Viết hàm sum_digits(n) bằng đệ quy để tính tổng các chữ số của n.
# Ví dụ: sum_digits(1234) → 1 + 2 + 3 + 4 = 10
# n= int(input("nhap số n:"))
# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_digits(n//10)
# a = int(input("Nhập một số nguyên dương: "))
# if a < 0:
#     print("Vui lòng nhập số nguyên dương!")
# else:
#     print("Tổng các chữ số là:", sum_digits(1234))
# print(sum_digits(1234))
# def tim_cac_cap(danh_sach, k):
#     da_xu_ly = set()
#     ket_qua = []
#     for so in danh_sach:
#         can_tim = k - so
#         if can_tim in da_xu_ly:
#             ket_qua.append((min(so, can_tim), max(so, can_tim)))
#         da_xu_ly.add(so)
#     return ket_qua
# ds = [1, 5, 3, 7, 2, 4, 6]
# tong = 7
# kq = tim_cac_cap(ds, tong)
# print(kq)
# def findPairSum(list, k):
#     check = set()
#     pair = []

#     for so in list:
#         remain = k - so
#         if remain in check:
#             cap = tuple(sorted((so, remain)))
#             if cap not in pair:
#                 pair.append(cap)
#         check.add(so)

#     if pair:
#         print(f"Các cặp có tổng bằng {k} là:")
#         for a, b in pair:
#             print(f"({a}, {b})")
#     else:
#         print(f"Không có cặp nào có tổng bằng {k}.")

# n = int(input("Nhập số lượng phần tử trong danh sách: "))

# list = []
# for i in range(n):
#     so = int(input(f"Nhập phần tử thứ {i+1}: "))
#     list.append(so)

# k = int(input("Nhập giá trị k cần tìm tổng: "))
# findPairSum(list, k)

# def findPairSum(list, k):
#     check = []      
#     pair = []   

#     for so in list:
#         remain = k - so
#         if remain in check:
#             a = min(so, remain)
#             b = max(so, remain)
#             cap = [a, b]
#             if cap not in pair:
#                 pair.append(cap)
#         check.append(so)

#     if pair:
#         print(f"Các cặp có tổng bằng {k} là:")
#         for cap in pair:
#             print(f"({cap[0]}, {cap[1]})")
#     else:
#         print(f"Không có cặp nào có tổng bằng {k}.")

# # Nhập danh sách từ bàn phím
# n = int(input("Nhập số lượng phần tử trong danh sách: "))

# list = []
# for i in range(n):
#     so = int(input(f"Nhập phần tử thứ {i+1}: "))
#     list.append(so)

# k = int(input("Nhập giá trị k cần tìm tổng: "))
# findPairSum(list, k)

def timtongcap(ds,k):
    kq=[]
    for i in range(len(ds)):
        for j in range (i+1, len(ds)):
            if[ds[i],ds[j]] not in kq and [ds[j],ds[i]] not in kq:
                kq.append([ds[i],ds[j]])
    return kq;            
ds=[1,5,3,7,2,4,6,0,4,3]
k=7     
a= timtongcap(ds,k)
print(a)           