# This is just a comment


## Basics of Strings and Variables

# A basic variable in python looks like this
message =  'hello from python!'

# And a simple printing of the message to the console looks like this
# Prints 'hello from python!'
print(message)

# If you want to convert the first letter of each word to uppercase you can use the .title() method
# prints 'Hello From Python!'
print(message.title())

# You also can convert all the case to upper or loser case as such
# prints 'HELLO WORLD FROM PYTHON!'
print(message.upper())
# prints 'hello world from python!'
print(message.lower())

# You can also print variables in string literals like so by placing an f(format) before mustache braces encapsulating the variables
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

# Combining some of the things you can do with format
# prints 'Hello, Ava Lovelace!'
print(f'Hello, {full_name.title()}!')

# And you can of course assign this to a variable and then call it like some
# Also prints 'Hello, Ava Lovelace!'
second_message = f'Hello, {full_name.title()}!'
print(second_message)

# you can also print to the console using nonprinting characters such as tabs spaces or end of line symbols, here's an example of a tabs
# prints    Python
print('\tPython')

# And newline characters
print('Languages:\nPython\nC\nJavaScript')
# prints
# Languages
# Python
# C
# JavaScript

# And newline characters with newline and tab characters
print('Languages:\n\tPython\n\tC\n\tJavaScript')
# prints
#   Languages
#   Python
#   C
#   JavaScript

# Python makes it easy to strip away whitespace that is in a string at the end with the strip() methods, 
# there is rstrip() (right side spaces are stripped) lstrip() (obvious) and strip() which does both
favorite_language = 'python '

# Although they will look the same, the space in the above string is printed in the first instance, but not the second
print(favorite_language)

favorite_language.rstrip()

print(favorite_language)
