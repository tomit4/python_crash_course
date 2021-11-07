## Working with Lists (for loops)

# A basic for loop can be created as so

# Prints
# alice
# david
# carolina
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Note the standard convention for working with loops
# for item in list_of_items:
#    action to be performed on list

# So let's do more than just print out the items in our list, here's another example of a for loop

# Prints
# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.

# David, that was a great trick!
# I can't wait to see your next trick, David.

# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print('Thank you, everyone. That was a great magic show!')

# Note the indentation indicates closure in Python, without exactly 4 spaces, Python will not recognize this as an enclosed function and will throw an error
# If the last print line above had been indented, Python would have read this as part of the above loop, regardless of how many line breaks you put inbetween item

# Generating a list of numbers
# Generating numbers is relatively easy using the in range syntax, note that due to zero based indexing, the last digit is always less than the number indicated.
# This is equivalent to using the < without the = sign in JS when creating a standard for loop 

# Prints
# 1
# 2
# 3
# 4
for value in range(1, 5):
    print(value)

# One can easily generate a list of numbers by storing the results of the range() method in a variable

# Prints [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)

# Python also allows for a third argument to be given to range which will then divide the results based off the argument.
# In the following case, it is simply returning the even numbers within a given range.

even_numbers = list(range(2, 11, 2))

# Prints [2, 4, 6, 8, 10]
print(even_numbers)

# As just another example, let's  create a for loop that returns the values returned between two numbers, and square those values

# Prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# We can write this more syntactically sweetened like storing

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Or even more syntactically sweetened like so

# This format is known as a comprehension according to the author, and generally interpreted as syntactically shortening our code
# NOte in this format how the value and methods enacted upon it are declared first, then the loop and its range is defined AFTER this declaration
squares = [value**2 for value in range(1, 11)]
print(squares)

# Some basic arithmetic methods have been included with python, here are just a few

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Prints 0
print(min(digits))
# Prints 9
print(max(digits))
# Prints 45
print(sum(digits))

# Python also a slice method, but it is not called upon using a method called slice, instead it appears more like calling on a index of a list like so

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Prints ['charles', 'martina', 'michael']
print(players[0:3])
# Prints ['martina', 'michael', 'florence']
print(players[1:4])

# If you omit the first index, the slice will start at the 0 index

# Also Prints ['charles', 'martina', 'michael']
print(players[:3])

# And if you wish to start at a specific index but go to the end, you would just reverse that logic like so

# Prints ['michael', 'florence', 'eli']
print(players[2:])

# You can also loop from the end of the list by starting with a negative index number, which will start at the end of the list and loop until the number is reached

# Prints ['michael', 'florence', 'eli']
print(players[-3:])

# So now we can get slightly fance with it and loop through a slice like shortening

players = ['charles', 'martina', 'michael', 'florence', 'eli']


# Prints
# Here are the first three players on my team:
# Charles
# Martina
# Michael

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

# Copying a Lists, note that copying a list is very simple, by omitting index numbers within our range and simply referencing a : within our square brackets,
# we can copy our list by storing it in another variable. (note that this is similar to array.map() in JS)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

# Prints
# Here are the first three players on my team:
# Charles
# Martina
# Michael

# Prints 
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_food)

# Note that we did not simply make the two lists equivalent, that would mean that any change we made to the my_foods list would show up in the friend_food list.
# Since we made a copy, appending to one list will not affect the other and visa versa

my_foods.append('cannoli')
friend_food.append('ice cream')

# Prints

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_food)
