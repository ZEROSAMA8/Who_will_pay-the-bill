# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

namesl= (len(names))
random_choice = random.randint(0,namesl -1)
#print(random_choice)
person_pay =names[random_choice]
print( person_pay + " is going to buy the meal today!")

