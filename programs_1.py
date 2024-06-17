'''Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line. '''

x = []
for i in range(2000,3201):
    if (i % 7 == 0) and (i % 5 != 0):
        x.append(str(i))

print(x)

'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:'''

n = int(input("enter your number"))
d = dict()
for i in range (1,n+1):
    d[i] = i*i

print(d)

'''Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.'''

m = input("enter your values")
l = m.split(',')
t = tuple(l)

print(l)
print(t)

'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

class Inoutstring(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s).upper()

obj = Inoutstring()
obj.getString()
obj.printString()

'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]'''

import math
C = 50
H = 30
values = []
items = [x for x in input().split(",")]

for d in items:
    values.append(int(round(math.sqrt(2*C*d)/H)))

print(values)





    
    
