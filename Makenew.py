import os
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_thing_working():
    strings = []
    for _ in range(5):
        random_string = get_random_string(length=5)
        strings.append(random_string)
    return strings

x = get_thing_working()
for item in x:
    newfilestuff = open(item + ".py", "w")


