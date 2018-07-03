## OU SECS Summer Camp
## Adventures in Coding 2
## Summer 2018
## Erik Fredericks
## inheritance-loops.py

## This program demonstrates class inheritance along with loops and lists.
## The Person and Student classes are the same as inheritance.py

import random
from copy import deepcopy

# Parent Person class.  This should store the general attributes that define a Person
class Person(object):
  # Store the incoming variables to the class object
  def __init__(self, name, age):
    self.name = name
    self.age  = age

  # Print out the person's information
  def Print(self):
    print("Name [%s], Age [%d]" % (self.name, self.age))

# Child Student class.  This extends the Parent class with Student-specific attributes
class Student(Person):
  # Store Student-specific information AND instantiate as a Person
  def __init__(self, name, age, student_id, classes):
    Person.__init__(self, name, age)  # Call the Person class to make a Student a Person
    self.student_id = student_id
    self.classes    = classes

  def Print(self):
    print("Name [%s], Age [%d], Student ID [%d]" % (self.name, self.age, self.student_id))

  def PrintClasses(self):
    print("Classes for Student [%s]" % self.name)
    for my_class in self.classes:  # class is a reserved word so don't use it as a variable
      print("* " + my_class)
    print("------------------------")

# Create and print out our list of students
students = []
all_classes = ["Math", "Social Studies", "English", "Programming", "Gadgets", "Gym"]
for i in range(10):  # 10 students in our class
  student_name = "Student %d" % i
  student_age  = random.randint(10,18)
  student_id   = random.randint(1,1000000)

  # Select random classes per student
  student_classes = deepcopy(all_classes) # Make a copy of the classes
  random.shuffle(student_classes)         # Shuffle the list
  student_classes = student_classes[:3]  # A student can only take 3 classes so snip the list
  print(student_classes)

  # Create a local instance of a Student and add it to our list
  s = Student(student_name, student_age, student_id, student_classes)
  students.append(s)

# Now, print out all student information in a foreach-style loop
for student in students:
  student.Print()
  student.PrintClasses()
