## Basics of Numbers

# Prints 5
print(2 + 3)
# Prints 1
print(3 - 2)
# Prints 6
print(2 * 3)
# prints 1.5
print(3 / 2)

# Similar to JS, python also requires parens in order to differentiate the order of operations

# Prints 14
print(2 + 3*4)
# Prints 20
print((2 + 3) * 4)

# Floating point numbers
# As the book says, for the most part you don't have to worry about adding decimals

# Prints 0.2
print(0.1 + 0.1)
# Prints 0.4
print(0.2 + 0.2)
# Prints 0.2
print(2 * 0.1)
# Prints 0.4
print(2 * 0.2)

# And again, as the book says, this is for the MOST part...


# Prints 0.30000000000000004
print(0.2 + 0.1)
print(3 * 0.1)

# Division or any operation involving a floating point number will return a floating point number as a result

# Prints 2.0
print(4/2)

# Prints 6.0
print(2 * 3.0)

# Prints 9.0
print(3.0 ** 2)

# Very much like commas in standard mathematical notation, python allows the use of underscores to delinate very large numbers
# Please note that this is soley for human readability and you don't have to use any underscores to represent the same number,
# it is outright ommitted in the printing to the console

# Prints 14000000000
print(14_000_000_000)
print(14000000000)

# Just like in JS, you can assign multiple variables at once

# Prints 0, 0, 0
x, y, z = 0, 0, 0
print(x, y, z)

# Python does not support constant variables, and so it is by convention that variables that are meant to be constants are
# delineated as such by using all capital letters

MAX_CONNECTIONS = 5000



