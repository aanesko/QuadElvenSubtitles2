import math
import random

first_die = ["Yn", "Ar", "Dori", "Corel", \
 "Cordel", "Adre", "Glorfin", "Omphal", \
 "Othal", "Ophal"]
second_die = ["na", "dea", "vea", "an", "eal",\
 "ea", "las", "lon", "dor"]
third_die = ["Linn", "Gren", "Lothar", "Othal",\
 "Novar", "Vergol"]
fourth_die = ["ena", "owin", "ian", "ea", "ael",\
 "inae"]

print("Welcome to QuadElvenSubtitles! Hit ENTER to roll your first name.")
user_response = input("Keep hitting ENTER to generate new names or q/Q to quit. ")
print("")

keep_playing = len(user_response) == 0 or user_response.lower()[0] != "q"
while keep_playing :
  first = random.choice(first_die)
  second = random.choice(second_die)
  third = random.choice(third_die)
  fourth = random.choice(fourth_die)
  string = first + second + " " + third + fourth
  user_response = input(string + " ")
  keep_playing = len(user_response) == 0 or user_response.lower()[0] != "q"
