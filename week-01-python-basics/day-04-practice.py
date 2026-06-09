# Dictionary methods

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}
user.update({'age':39})
print('age' in user.keys())
print('hello' in user.values())
print(user.items())

# user.clear()
# user2 = user.copy()

# Tuples -> tuples are immutable lists

my_tuple = (1,2,3,4,5,5,6)
print(my_tuple)

x,y,z,*other = (1,2,3,4,5)
print(other)

#there are 2 tuple methods, i.e. count & index
print(my_tuple.count(5))
print(my_tuple.index(5))

# Set -> unordered collection of unique objects

my_list = {1,2,3,4,5,5,100}
print(my_list)
uniques = set(my_list)
print(uniques)
