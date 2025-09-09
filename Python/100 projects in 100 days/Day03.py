# print("welcome to the rollercoaster !")
# height = int(input("what's your height in cm?"))
# if height>=120:
#     print("you can ride the rollercoaster")
# else:
#     print("sorry you have to grow taller before you can ride.")
# if height==120:
#     print("you can ride the rollercoaster")
# else:
#     print("sorry you have to grow taller before you can ride.")
# if height!=120:
#     print("you can ride the rollercoaster")
# else:
#     print("sorry you have to grow taller before you can ride.")
#-------------------------------------------------------------------------------------------------
# even number 12 % 2==0
# number_to_check=int(input("what is the number you want to check?"))
# print(number_to_check)
# print(number_to_check % 2)
# if number_to_check % 2 ==0:
#     print("even")
# else:
#     print("Odd")
#-------------------------------------------------------------------------------------------------
# print("welcome to the rollercoaster!")
# height= int(input("what is your height?\n"))
# if height < 120:
#     print("your height is too small")
#     age= int(input("what is your age?\n"))
#     if age < 12:
#         print("your age pag $5")
#     elif age < 18:
#         print("your age pay $7")
#     elif age < 22:
#         print("your age pay $20")
#     else:
#         print("your age pay $12")
# else:
#     print("your height is too big")
#-------------------------------------------------------------------------------------------------
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
#
# If the bmi is under 18.5 (not including), print out "underweight"
#
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#
# If the bmi is 25 (including) or over, print out "overweight"
#
# Refer to this graphic for help:
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("underweight")
# print(f"Weight: {weight}kg, BMI: {bmi:.2f}", end=" - ")
#-------------------------------------------------------------------------------------------------
# print("wellcome to the rollersoaster!")
# height= int(input("what is your height?\n"))
# bill = 0
# if height>120:
#     print("you can ride the rollercoaster")
#     age= int(input("what is your age?\n"))
#     if age<=12:
#         bill = 5
#         print("child ticket ar $5")
#     elif age<=18:
#         bill = 7
#         print("youth ticket ar $7")
#     else:
#         bill = 12
#         print("you have $12")
#     wants_photo=input("do you want to have a photo take? type y for yes and n for no?\n")
#     if wants_photo=="y":
#         bill+=3
#     print(f"your final bill is ${bill}")
# else:
#     print("sorry you have to grow taller before you can ride")
#-------------------------------------------------------------------------------------------------
print("wellcome to python pizza deliveries!")
size=input("what size pizza do you want? S, M, or L?\n")
pepperoni=input("do you want pepperoni on your pizza? Y or N:\n")
extra_cheese =input("do you want extra cheese? Y or N:\n")
