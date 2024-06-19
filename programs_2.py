'''Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after 
sorting them alphabetically.'''

items = [x for x in input().split(',') ]
items.sort()
print(",").join(items)

'''Write a program that accepts sequence of lines as input and prints the lines after making all characters 
in the sentence capitalized.'''

lines = []

while True:
    x = input()

    if x:
        lines.append()(x.upper())
    else:
        break;
for s in lines:
    print(s)

