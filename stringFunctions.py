# String Functions
myString = 'Hello World'

# Capitalize first letter
print(myString.capitalize())

# Swap Case - swaps lowercase and lowercase letters
print(myString.swapcase())

# Length
print(len(myString))

# Replace
print(myString.replace('World', 'Everyone'))

# Count - counts letters inside a string
print(myString.count('l'))

# Startswith
print(myString.startswith('Hello'))

# Endswith
print(myString.endswith('World'))

# Split to list
print(myString.split())

# Find substring
print(myString.find('World'))

# Index - same as find except that it can throw errors
print(myString.index(' '))

# Is all alphanumeric
print(myString.isalnum())

# Is all alphabetic
print(myString.isalpha())

# Is all numeric
print(myString.isnumeric())
