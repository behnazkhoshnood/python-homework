#                                                                                       Day 1

# Homework

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(f"{color.PURPLE}W{color.CYAN}e{color.DARKCYAN}l{color.BLUE}c{color.GREEN}o{color.YELLOW}m{color.RED}e {color.PURPLE}t{color.CYAN}o {color.DARKCYAN}M{color.BLUE}y{color.GREEN}F{color.YELLOW}r{color.RED}i{color.PURPLE}e{color.CYAN}n{color.DARKCYAN}d{color.BLUE}s {color.GREEN}1.0!{color.END}")

# Homework.Advance lolor
# I couldn't make it with only 2 print statements!
for row in range(12):
    if row in range(1,11,4):
        print(f"{color.PURPLE}#####{color.END}")
    elif row in range(2, 12) and row != 6:
        print(f"{color.CYAN}#   #{color.END}")
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

print(f"My {color.RED}{'' if friend_1_the_best == False else 'best'}{color.END} friend name is {color.RED}{friend_1_name}{color.END}, {'she' if is_male_1 == False else 'he'} is {friend_1_age} y/o and {'her' if is_male_1 == False else 'his'} email address is {friend_1_email}")
print(f"My {color.YELLOW}{'' if friend_2_the_best == False else 'best'}{color.END} friend name is {color.YELLOW}{friend_2_name}{color.END}, {'she' if is_male_2 == False else 'he'} is {friend_2_age} y/o and {'her' if is_male_2 == False else 'his'} email address is {friend_2_email}")
print(f"My {color.GREEN}{'' if friend_3_the_best == False else 'best'}{color.END} friend name is {color.GREEN}{friend_3_name}{color.END}, {'she' if is_male_3 == False else 'he'} is {friend_3_age} y/o and {'her' if is_male_3 == False else 'his'} email address is {friend_3_email}")

# Homework.Advance level
import datetime
from datetime import date

my_name = "Behnaz"
today = date.today()
now = datetime.datetime.now()

print(f"Good day {color.CYAN}{my_name}!{color.END}, {color.GREEN}{today}{color.END} is a perfect day to learn some Python.")
print (" The time is: = %s:%s:%s" % (now.hour + 2, now.minute, now.second))

#                                                                                       Day 3
friends = [
["Felix Holm", True, "felix.holm@example.com", 28, True],
["Fariba Kamani", False, "fariba.kamani@example.com", 34, False],
["Mahsa Khoshnood", False, "mahsa.khoshnood@example.com", 32, True],
]

for friend in friends:
    print(f"{color.PURPLE}My {'best' if friend[4] == True else ''} friend name is {friend[0]}, {'she' if friend[1] == False else 'he'} is {friend[3]} y/o and {'her' if friend[1] == False else 'his'} email address is {friend[2]}{color.END}")

# homework
for friend in friends:
    print (f"{color.YELLOW}{friend[0]}, {friend[3]} year old, Email: {friend[2]}{color.END}")

for friend in friends:
    if friend[4] == True:
        print(f"{color.BOLD}{color.BLUE}{friend[0]}{color.END}")

# advance homework
numbers = [
["0728085451"], #valid 
["a234bdh345"], #invalid, it contains alphabetic characters
["12345"], #invalid, it has less than 10 digit
["12345345789"], #invalid, it has more than 10 digit
]

for number in numbers:
    if number[0].isdigit() and len(number[0]) == 10:
        print(f'{color.GREEN}Valid Number{color.END}')

    else:
        print(f'{color.RED}Invalid Number{color.END}')

# Day 4

answer = input(f"{color.BOLD}{color.YELLOW} To see a list of all of my friends press (a) {color.UNDERLINE}{color.GREEN} or to see a list of only the best friends press (b) ?{color.END}")
if answer == "a":
    for friend in friends:
        print(f"{color.YELLOW}{friend[0]}{color.END}")

elif answer == "b":
    for friend in friends:
        if friend[4] == True:
            print(f"{color.GREEN}{friend[0]}{color.END}")
else:
    print(f"{color.RED}Your answer was {answer}{color.END}")
    print(f"{color.RED}You should choose between a or b. Please try again.{color.END}")

# Advance Homework
import random

computer = random.randint(1, 10)
# print(computer)
number = input(f"{color.BOLD}Guess a number between 1 to 10?{color.END}")
try:
    if int(number) == computer:
        print(f"{color.GREEN}Congradulations. You win.{color.END}")

    elif int(number) != computer and int(number) in range(1,11):
        print(f"{color.CYAN}Sorry you guessed a wrong number. Please try again.{color.END}")

    else:
        print(f"{color.RED}Wrong Number. Please enter a number between 1 to 10.{color.END}")
except:
    raise Exception(f'{color.RED}You only can enter a number. Please try again.{color.END}')
