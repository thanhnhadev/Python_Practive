# -------------------------
# random_number_0_to_1 = random.random()*10
# print(random_number_0_to_1)
# ---------------------------
# random_float = random.uniform(1,10)
# print(random_float)
# -----------------------------
# random_head_or_tails=random.randint(0,1)
# print(random_head_or_tails)
# if random_head_or_tails == 0:
#     print("mặt ngửa heads")
# else:
#     print("mặt sấp tails")
# ----------------------------------------------------
# states_of_america = [
#     "Delaware",
#     "Pennsylvania",
#     "Alabama",
#     "Alaska",
#     "Arizona",
#     "Arkansas",
#     "California",
#     "Colorado",
#     "Connecticut",
#     "Florida",
#     "Georgia",
#     "Hawaii",
#     "Idaho",
#     "Illinois",
#     "Indiana",
#     "Iowa",
#     "Kansas",
#     "Kentucky",
#     "Louisiana",
#     "Maine",
#     "Maryland",
#     "Massachusetts",
#     "Michigan",
#     "Minnesota",
#     "Mississippi",
#     "Missouri",
#     "Montana",
#     "Nebraska",
#     "Nevada",
#     "New Hampshire",
#     "New Jersey",
#     "New Mexico",
#     "New York",
#     "North Carolina",
#     "North Dakota",
#     "Ohio",
#     "Oklahoma",
#     "Oregon",
#     "Rhode Island",
#     "South Carolina",
#     "South Dakota",
#     "Tennessee",
#     "Texas",
#     "Utah",
#     "Vermont",
#     "Virginia",
#     "Washington",
#     "West Virginia",
#     "Wisconsin",
#     "Wyoming"
# ]
# print(len(states_of_america)) # điếm list danh sách
# num_of_startes = len(states_of_america) # 50->49
# print(states_of_america[num_of_startes -1])
# ----------------------------------------------------
# fruits = [
#     "apples",
#     "bananas",
#     "oranges",
#     "grapes",
#     "strawberries",
#     "blueberries",
#     "pears",
#     "kiwis",
#     "mangoes",
#     "pineapples",
#     "watermelons",
#     "peaches"
# ]
# vegetables = [
#     "carrots",
#     "broccoli",
#     "spinach",
#     "kale",
#     "lettuce",
#     "cucumbers",
#     "tomatoes",
#     "peppers",
#     "onions",
#     "potatoes",
#     "garlic",
#     "zucchini"
# ]
# pesticides = [
#     "glyphosate",
#     "chlorpyrifos",
#     "malathion",
#     "pyrethrins",
#     "neonicotinoids",
#     "imidan",
#     "carbaryl",
#     "diazinon",
#     "rotenone",
#     "captan",
#     "parathion",
#     "dicamba"
# ]
# dirty_dozen =[vegetables, fruits] # gộp 2 list danh sách
# print(dirty_dozen)
# ----------------------------------------------------
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits[-5])
# ----------------------------------------------------
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# ----------------------------------------------------
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])
# # print(dirty_dozen)
# # print(dirty_dozen[0])
# # print(dirty_dozen[1])
# # print(dirty_dozen[1][2])
# # print(dirty_dozen[1][3])
# ----------------------------------------------------
import random
rock = '''
   _______
  /       \ 
 /         |
|    ( )   |
|    ( )   |
|    ( )   |
 \         |
  \_______/
'''

paper = '''
   _______
  /       \ 
 /         |
|    _____ |
|   |     || 
|   |     ||
 \_______/
'''

scissors = '''
   _______
  /       \ 
 /         |
|   / \    |
|  /   \   |
| /     \  |
 \         |
  \_______/
'''
# In các lựa chọn
# print("Búa:")
# print(rock)
# print("Bao:")
# print(paper)
# print("Kéo:")
# print(scissors)
game_images = [rock,paper,scissors]
user_choice = int(input("what do you choose? type 0 for rock-búa, 1 for Paper-bao of 2 for Scissors-kéo \n"))
if user_choice >=0 and user_choice <=2:
   print(game_images[user_choice])

computer_choice = random.randint(0, 2)
# print(f"Computer chose {computer_choice}")
print("Computer chose:")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0:
     print("you typed an invalid number . you lose!")
elif user_choice ==0 and computer_choice ==2:
    print("user wins!")
elif computer_choice==0 and user_choice==2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw!")
