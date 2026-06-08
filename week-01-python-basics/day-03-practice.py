# Lists -> mutable
# list slicing

amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "grocery"
]

amazon_cart[0] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart[:] #to copy a list
print(new_cart)

# matrix -> to define multi-dimensional lists

# list methods
basket = [1,2,3,4,5]
new_list = basket.append(100)
new_list = basket
print(new_list)
basket.insert(2,20)
print(basket)

# removing
basket.pop() #remove index
print(basket)

basket.remove(20) #remove value
print(basket)

# sorted list
values = ['a', 'e', 'd', 'f', 'c']
values.sort()
print(values)

print(list (range(1,100)))