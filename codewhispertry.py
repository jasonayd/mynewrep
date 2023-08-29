#write a function that generates a string of current date and time and a random number between 0 and 60 and a letter 

import datetime
import string
import random

def random_string():
    return str(datetime.datetime.now()) + str(random.randint(0,60)) + str(random.choice(string.ascii_letters))
a = random_string()

print(a)

#write a function that generates a string of current year, week number and day name and a number between 0 and 60 and a letter by putting dash in between


import datetime

def random_string():
    return str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().isocalendar()[1]) + "-" + str(datetime.datetime.now().strftime("%A")) + str(random.randint(0,60)) + str(random.choice(string.ascii_letters))

b= random_string()

print(b)
print(a)








