import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favourite_number)
# -------------------------
# random_number_0_to_1 = random.random()*10
# print(random_number_0_to_1)
# ---------------------------
# random_float = random.uniform(1,10)
# print(random_float)
# -----------------------------
random_head_or_tails=random.randint(0,1)
print(random_head_or_tails)
if random_head_or_tails ==0:
    print("mặt ngửa heads")
else:
    print("mặt sấp tails")