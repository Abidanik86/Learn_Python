# Creating a string
my_string = "Hello, World!"

# Accessing characters in a string
print(my_string[0])  # Output: H
print(my_string[-1])  # Output: !

# Concatenating strings
greeting = "Hello"
name = "Abid Hasan Anik"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!

# String length
print(len(my_string))  # Output: 13

# Splitting a string
words = my_string.split(", ")
print(words)  # Output: ['Hello', 'World!']

# Replacing characters in a string
new_string = my_string.replace("World", "Python")
print(new_string)  # Output: Hello, Python!

# Converting to uppercase and lowercase
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!

# Iterating over each character in a string
for char in my_string:
    print(char)