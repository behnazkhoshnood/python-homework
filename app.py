# Home work
print("Welcome to MyFriends 1.0!")
print()
# Homework.Advance level
# I couldn't make it with only 2 print statements!
for row in range(12):
    if row in range(1,11,4):
        print("#####")
    elif row in range(2, 12) and row != 6:
        print("#   #")
    elif row == 6:
        print()

