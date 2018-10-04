# Conditionals
x = 4
color = 'blue'

# Basic If/Else
if x < 6:
    print('Less than 6')
else:
    print('Greater that 6')

# Else If
if x > 4:
    print('Greater than 4')
elif x < 4:
    print('Less than 4')
else:
    print('Equals 4')

# Nested If Statements
if x < 10:
    if color == 'blue':
        print('Color is blue and x is less than 10')
else:
    print('Color is not blue and x is greater than 10')

# Logical Operators
if color == 'blue' and x < 10:
    print('Color is blue and x is less than 10')
else:
    print('Color is not blue and x is greater than 10')
