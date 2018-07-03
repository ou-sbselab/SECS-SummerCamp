## OU SECS Summer Camp
## Adventures in Coding 2
## Summer 2018
## Erik Fredericks
## inheritance.py

## This program demonstrates class inheritance.

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
  def __init__(self, name, age, student_id):
    Person.__init__(self, name, age)  # Call the Person class to make a Student a Person
    self.student_id = student_id

  def Print(self):
    print("Name [%s], Age [%d], Student ID [%d]" % (self.name, self.age, self.student_id))

# Create a person
person = Person("Erik", 34)
person.Print()

# Create a student, who is also a person
student = Student("John", 22, 123456789)
student.Print()

