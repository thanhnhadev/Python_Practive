# Numbers, Operations, Type Conversion, f-Strings
# Subscripting
print(len("Hello"))
print("hallo"[4])
print("hallo"[-2])
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
# String
print("123" + "345") # concatenation
# Integer = whole number
print(123 + 345)
# Large Integers
print(123_456_789)
# Float = Floating Point Number
print(3.14159)
# Boolean
print(True)
print(False)
# Data type
len("hello")
print(type("hello"))
print(type(123))
print(type(3.14))
print(type(True))
int("123")
print(int("123")+int("456"))
print(int("abc")+int("456"))
# int()
# float()
# str()
# bool()
name_of_the_user = input("enter your name:")
len_of_name=len(name_of_the_user)
print(type("number of letter in your name:"))
print(type(len_of_name))
print("number of letter in your name: "+ str(len_of_name))
# Mathematical Operations
print("My age:"+str(12))
print(123+456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(type(6 // 3))
print(2 ** 3)
#PEMDASLR
# ()
# **
# *
# /
# +
# -
print(3*3+3//3-3)
height = 1.65 
weight = 84
# Write your code here.
# Calculate the bmi using weight and height.
bmi =weight / height**2
print(bmi)
#-------------------------------------------------------------------------------------------------
xyz=84/1.65**2
print(xyz)
print(int(xyz))
#lam tron
print(round(xyz))
# dau phay dong với do chinh xac 2 chu so
print(round(xyz,2))
score = 0
height= 1.8
is_winning = True
#-------------------------------------------------------------------------------------------------
print(f"your score is ={score},\n your height is {height}.\n You are winning ={is_winning}")
print(6 + 4 / 2 - (1 * 2))
a = int("5") / int(2.7)
print(type(a))
name = input("what is your name?")
print(f"hello,{name}")
print(f"hello,"+name)
age=12
print(f"you are {age} year old")
# print("you are"+age"years old")
print("wellcome to the tip calculator")
bill=float(input("what was the total bill? $"))
tip=int(input("what percentage tip would you like to give?10 12 15"))
people= int(input("how manu people to split the bill?"))
# bill_with_tip = tip/100*bill+bill
# bill_with_tip = bill*(1+tip/100)
# print(bill_with_tip)
tip_as_percent=tip/100
total_tip_amonut = bill*tip_as_percent
total_bill =  bill + total_tip_amonut
bill_per_peson = total_bill/people
final_amount=round(bill_per_peson,2)
print(f"Each personn shoud pay: $ {final_amount}")