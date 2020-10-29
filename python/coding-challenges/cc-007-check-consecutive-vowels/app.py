# The purpose of this coding challenge is to write a program that checks if\
#  a word contains consecutive vowels or not.

entery = input("Please enter a string: ")

vowel_set = {"a", "e", "u", "i", "o"}

iter_entery = iter(entery)
result = "Negative"
for i in iter_entery:
    if i in vowel_set and next(iter_entery,len(entery)) in vowel_set:
        result = "Positive"

print(result)

