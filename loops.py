# Loops
people = ['Dennis', 'Adam', 'Jimmy']

# For loop
for person in people:
    print('Current Person: ', person)

# Iterate by index
for i in range(len(people)):
    print('Current Person in sequence: ', people[i])

# While loop
count = 1

while count <= 10:
    print('Count: ', count)
    count = count + 1

# Breaking out of a while loop
newCount = 0

while newCount <= 10:
    print('New Count: ', newCount)
    if newCount == 5:
        break
    else:
        newCount = newCount + 1
