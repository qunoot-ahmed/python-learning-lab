# comparing sets
from operator import truediv

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# print(my_set.discard(5))

# print(my_set.difference_update(your_set))
# print(my_set)

print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))

print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))

# conditional logic

is_old = True
is_licensed = True

if is_old and is_licensed:
    print('you are old enough')
else:
    print('you are not of age')

# Logical operators -> and, > < =
print(4>5)

# Exercise
is_magician = True
is_expert = False

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('At least you are getting it')
else:
    print('You need magic powers')

# == checks for equality in value
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
# is (stricter) checks if the location in memory where the value is saved is same
# print(True is 1)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])

# Loops
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)

user = {
    'name': 'jack',
    'age': 55,
    'can_swim': False
}
for k,v in user.items():
    print(k,v)

# Exercise: Counter

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

