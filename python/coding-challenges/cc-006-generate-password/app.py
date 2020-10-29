#The purpose of this coding challenge is to write a program that \
# creates a random password from a given full name.
import random

fullname = input ("Please enter your full name(without any spaces): ").lower()

result = random.sample(fullname, k = 3)

result = result + [str(x) for x in random.sample(range(10), k = 4)]
print("".join(result))

