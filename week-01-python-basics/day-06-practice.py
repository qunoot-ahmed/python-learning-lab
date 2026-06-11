# range object
# you can iterate over range
from enum import unique
from idlelib.debugobj import myrepr
from multiprocessing.reduction import duplicate

print(range(100))

for number in range(0,100):
    print(number)

for i in range(10, 0, -1):
    print(i)

print(list(range(10)))

#The enumerate() function is a built-in Python tool that adds a counter to an iterable
# (like a list, tuple, or string) and returns it as an enumerate object.
# This allows you to track both the index and the value of your items simultaneously during a loop,
# completely eliminating the need to manually maintain an external counter variable.

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')

# Exercise: loop through the list of lists, replace 0s with space and 1s with *
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for pic in picture:
    for item in pic:
        if item == 0:
            print(' ', end=' ')
        elif item == 1:
            print('*', end=' ')
    print()

# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# function

def say_hello():
    print('hello')
say_hello()

def isOddOrEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(isOddOrEven(88))

# *args **kwargs
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# Exercise: Highest even number
def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
        else:
            pass
    even.sort()
    return even[-1]

print(highest_even([10, 2, 3, 4, 8, 11]))
# we can also use max function

# walrus operator --> :=