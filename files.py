# Open a file
fo = open('text.txt', 'w')

# Get info
print('Name:', fo.name)
print('Is closed:', fo.closed)
print('Mode:', fo.mode)

fo.write('Python is damn good.')
fo.write('I also love JavaScript.')
fo.close()

fo = open('text.txt', 'a')
fo.write('But i hate PHP')
fo.close()

fo = open('text.txt', 'r')
text = fo.read()
print(text)
fo.close()

fo = open('text2.txt', 'w+')
fo.write('New File')
fo.close()
