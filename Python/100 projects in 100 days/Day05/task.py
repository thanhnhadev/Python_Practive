student_scores = [150,142,185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
# total_exam_score =sum(student_scores) # cộng các phần tử trong mảng
# print(total_exam_score) 
# # cách 2
# sum =0 #gán biến tạm 
# for score in student_scores:
#     sum+= score
# print(sum)
# for score in student_scores:
#     print(score) # in ra các phần tử trong mảng
# print(max(student_scores)) # tìm phần tử lớn nhất trong mảng
# cách 2 tìm phần tử lớn nhất trong mảng
# max_score =0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)