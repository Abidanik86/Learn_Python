# String Methods in Python

# 1. capitalize() - Converts the first character of a string to uppercase and the rest to lowercase
string = "abid hasan anik"
capitalized_string = string.capitalize()
print(capitalized_string)  

# 2. upper() - Converts all characters in a string to uppercase
string = "abid hasan anik"
uppercased_string = string.upper()
print(uppercased_string)  

# 3. lower() - Converts all characters in a string to lowercase
string = "ABID HASAN ANIK"
lowercased_string = string.lower()
print(lowercased_string)  

# 4. strip() - Removes leading and trailing whitespace from a string
string = "   abid hasan anik   "
stripped_string = string.strip()
print(stripped_string)  

# 5. split() - Splits a string into a list of substrings based on a delimiter
string = "abid,hasan,anik"
split_string = string.split(",")
print(split_string)  

# 6. join() - Joins a list of strings into a single string using a specified delimiter
list_of_strings = ['abid', 'hasan', 'anik']
joined_string = ','.join(list_of_strings)
print(joined_string) 

# 7. replace() - Replaces all occurrences of a substring in a string with another substring
string = "abid hasan anik"
replaced_string = string.replace("hasan", "universe")
print(replaced_string) 

# 8. find() - Returns the index of the first occurrence of a substring in a string
string = "abid hasan anik"
index = string.find("hasan")
print(index)  

# 9. count() - Returns the number of occurrences of a substring in a string
string = "abid hasan anik"
count = string.count("a")
print(count)  

# 10. len() - Returns the length of a string
string = "abid hasan anik"
length = len(string)
print(length)  
