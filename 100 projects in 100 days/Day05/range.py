# range function
print(range(1, 10))
print("-------------------------")
# range function with for loop
for number in range(1,11): # lấy phạm vi từ 1 -> 11
    print(number)
print("-------------------------")
for number in range(1,11, 3): # lấy phạm vi từ 1 -> 11 tăng dần theo 3 đến cuối cùng
    print(number)
print("-------------------------")
total =0
for num in range(1, 101):
    total+= num # cộng phạm vi từ 1 -> 101
print(total)
print("-------------------------")
# Loop through numbers from 1 to 100
for nu in range(1, 101):
    # Check for divisibility by both 3 and 5 FIRST
    if nu % 3 == 0 and nu % 5 == 0:
        print("FizzBuzz")
    # Then, check for divisibility by 3
    elif nu % 3 == 0:
        print("Fizz")
    # Then, check for divisibility by 5
    elif nu % 5 == 0:
        print("Buzz")
    # If none of the above are true, print the number
    else:
        print(nu)    
