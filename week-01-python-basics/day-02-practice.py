# with 3 single quotes we can do multi-line strings
from datetime import datetime, date

long_str = '''
WOW 
0 0
___

'''
print(long_str)

# type conversion
print(type(str(100)))

# escape sequence -> \t -> tab , \ -> keep quotes as is , \n -> new line
weather = "\t It\'s \"kind of\" sunny today \nHope you have a good day"
print(weather)

# formatted strings -> add f to the beginning
name = "charlie"
age = 40

print(f'Hi, {name}! You are {age} years old.')

# negative index in python means start at the end
value = "what is your name"
print(value[-1])

# immutability -> strings cannot be reassigned/modified
# we can either create a string or destroy it

# built-in python functions
# https://docs.python.org/3/library/functions.html

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote)

# a program to take year of birth as input and return the age
birth_year = input('What is your year of birth?')
age = date.today().year - int(birth_year)
print(f'Your age is: {age}')

# a password checker
username = input('Enter your name')
password = input('Enter password')
print(f"{username.capitalize()}, your password '{'*' * len(password)}' is {len(password)} letters long")

