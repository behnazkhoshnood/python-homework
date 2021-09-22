#                                                                                       Day 1

# Homework
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

# another version
print("""
#####
#   #
#   #
#####

#   #
#   #
#####
#   #
#   #
    """)

#                                                                                       Day 2
friend_1_name = "Felix"
is_male_1 = True
friend_1_email = "felix.holm@example.com"
friend_1_age = 28
friend_1_the_best = True

friend_2_name = "Fariba Kamani"
is_male_2 = False
friend_2_email = "fariba.kamani@example.com"
friend_2_age = 34
friend_2_the_best = False

friend_3_name = "Mahsa Khoshnood"
is_male_3 = False
friend_3_email = "mahsa.khoshnood@example.com"
friend_3_age = 32
friend_3_the_best = True

print(f"My {'' if friend_1_the_best == False else 'best'} friend name is {friend_1_name}, {'she' if is_male_1 == False else 'he'} is {friend_1_age} y/o and {'her' if is_male_1 == False else 'his'} email address is {friend_1_email}")
print(f"My {'' if friend_2_the_best == False else 'best'} friend name is {friend_2_name}, {'she' if is_male_2 == False else 'he'} is {friend_2_age} y/o and {'her' if is_male_2 == False else 'his'} email address is {friend_2_email}")
print(f"My {'' if friend_3_the_best == False else 'best'} friend name is {friend_3_name}, {'she' if is_male_3 == False else 'he'} is {friend_3_age} y/o and {'her' if is_male_3 == False else 'his'} email address is {friend_3_email}")

# Homework.Advance level
import datetime
from datetime import date

my_name = "Behnaz"
today = date.today()
now = datetime.datetime.now()

print(f"Good day {my_name}!, {today} is a perfect day to learn some Python.")
print ("The time is: = %s:%s:%s" % (now.hour + 2, now.minute, now.second))

#                                                                                       Day 3
friends = [
["Felix Holm", True, "felix.holm@example.com", 28, True],
["Fariba Kamani", False, "fariba.kamani@example.com", 34, False],
["Mahsa Khoshnood", False, "mahsa.khoshnood@example.com", 32, True],
]

for friend in friends:
    print(f"My {'best' if friend[4] == True else ''} friend name is {friend[0]}, {'she' if friend[1] == False else 'he'} is {friend[3]} y/o and {'her' if friend[1] == False else 'his'} email address is {friend[2]}")

# homework
for friend in friends:
    print (f"{friend[0]}, {friend[3]} year old, Email: {friend[2]}")

for friend in friends:
    if friend[4] == True:
        print(friend[0])

# advance homework
numbers = [
["0728085451"], #valid 
["a234bdh345"], #invalid, it contains alphabetic characters
["12345"], #invalid, it doesn't have 10 digits
]

for number in numbers:
    if number[0].isdigit() and len(number[0]) == 10:
        print('Valid Number')

    else:
        print('Invalid Number')