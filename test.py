def student_info(*arg, **kwarg):
    print(arg)
    print(kwarg)

courses = ['Math', 'Art']
info = {'name' : 'John', 'age' : 22}

student_info(*courses, **info)

# need clarification!!!

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)