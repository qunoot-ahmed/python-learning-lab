# range object
# you can iterate over range
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
