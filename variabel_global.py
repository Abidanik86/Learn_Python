x = "Abid Hasan Anik"
y = 26
z = "Dhaka"


def myfunc():

  print("My Name Is: " + x)
  print("My age is :", y)
  global w
  w = "Global Variable"

  print("My Name Is: " + x)
  print("My age is :", y)
  print("My city is: " + z)
  print("Global variable is: " + w)

myfunc()


