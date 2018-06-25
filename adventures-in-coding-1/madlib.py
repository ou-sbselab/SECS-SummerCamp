## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## madlib.py

## This program demonstrates a sipmle madlib with the intent of learning user input.

place   = raw_input("Enter a place: ")
verb1   = raw_input("Enter the first verb: ")
vehicle = raw_input("Enter a vehicle: ")
number  = raw_input("Enter a number: ")
nouns   = raw_input("Enter a noun: ")
animals = raw_input("Enter a type of animal: ")
verb2   = raw_input("Enter another verb: ")
noun    = raw_input("Enter the last noun: ")

sentence1 = "Last summer, my family and I went to a %s on vacation." % place
sentence2 = "We %sed in a %s, and it took %s days to get there." % (verb1, vehicle, str(number))
#sentence3 = "I took lots of photos of the %s there, and saw wild %s %ing in the %s." % (nouns, animals, verb2, noun)

sentence3 = "I took lots of photos of the %ss there, and saw wild %s %sing in the %s." % (nouns, animals, verb2, noun)

print sentence1
print sentence2
print sentence3
