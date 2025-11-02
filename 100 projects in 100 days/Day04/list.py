fruits  = ["cherry","apple","pear"]
state1 =  "Delaware"
state2 = "Pennsylvania"
states_of_america =["Delaware","Pennsylvania"]
print(states_of_america[0]) # tìm đến vị trí 
print(fruits[-1]) # đếm vị trí theo thứ tự 0 trở đi và ngược lại từ dưới đếm lại
fruits[1]="organge" #thay vị trí
print(fruits)
fruits.append("oragagne") # thêm vào cuối
print(fruits)
fruits.extend(["red","jhon"]) # mở rông thêm 2 dữ liệu trong mảng
print(fruits)
fruits.insert(3,"htk") # thêm vào vị trí index
print(fruits)
fruits.remove("htk") # xóa data có chuỗi
print(fruits)
# fruits.pop([1])
# print(fruits)
fruits.clear()
print(fruits)
print("---------------------")
import random
friends =["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends)) # radom 1 data ngẫu nhiên
random_index = random.randint(0,4) # cách 2
print(friends[random_index])