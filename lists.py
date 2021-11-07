## Introduction to Python Lists
# Lists are, at least so far, pretty much just the same as JS arrays

# Prints ['trek', 'cannondale', 'redline', 'specialized']
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Prints 'trek'
print(bicycles[0])

# And, of course, you can reference string methods at this point
print(bicycles[0].title())

# You can of course reference any index very much the same way as in other programming languages

# Prints 'cannondale'
print(bicycles[1])
# Prints 'redline'
print(bicycles[2])

# Interestingly, python also has a way of referencing the last index using -1

# Prints 'specialized'
print(bicycles[-1])

# And just like in most programming languages we can now use various methods on the string returned

message = f'My first bicycle was a {bicycles[0].title()}.'

# Prints 'My first bicycle was a Trek'
print(message)

# And of course, there are no constants in python, so we can reassign variables, or in this case variables in a list by referencing it and then changing it

motorcycles = ['honda', 'yamaha', 'suzuki']

# Prints the array above
print(motorcycles)

motorcycles[0] = 'ducati'
# Prints ['ducati', 'yamaha', 'suzuki']
print(motorcycles)

## List Methods

# You can append to the end of a list by using the append() method (note this is the same as push() in JS)
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')

#Prints  ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# You can insert items into a list at any index you would like by simply using the insert() method, which takes two arguments, the first argument being the index,
# the second being the string,number,etc you'd like to put in the list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')

# Prints  ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles)

# You can also easily remove elements from a list using the del() method, which is invoked differently, simply type del before the list reference

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]

# Prints ['yamaha', 'suzuki']
print(motorcycles)

# Like JS, Python has a pop() method, and works pretty much the same way, it will store the value of whatever is removed at the end of the list to be utilized later if need be

motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()

# Prints ['honda', 'yamaha']
print(motorcycles)
# Prints suzuki
print(popped_motorcycle)

# Unlike JS, Python has a remove() method that allows you to reference an item within a list by actual name (something tells me this method is computationaly expensive)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')

# Prints ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# You can store the value of what you wish to remove() in a varaible and use remove() on it later

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

# Prints ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Prints 
# A Ducati is too expensive for me.
print(f'\nA {too_expensive.title()} is too expensive for me.')

# Python has a sort() method which will sort a list (in this example by alphabetical order)
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()

# Prints ['audi', 'bmw', 'subaru', 'toyota']
print(cars)

# You can easily sort it in reverse alphabetical order by using a reverse=True argument in the sort() method, note the capitalization of True
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort(reverse=True)

# Prints ['toyota', 'subaru', 'bmw', 'audi']
print(cars)

# Note that the sort() method sorts the list in such a fashion that the list is PERMANENTLY altered, if you don't wish to alter the list in this way, use the sorted() function
# to present the list sorted by without PERMANENTLY changing it

# Note here how the sorted() method is not called on the list, but rather the list is an argument on a function call
cars = ['bmw', 'audi', 'toyota', 'subaru']

print('\nHere is the original list')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nBut the original list stays the same, even after using sorted()')
print(cars)

# A list can be simply reversed (with no note on alphabetical order as was the case in the reverse=True example above)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# Prints ['subaru', 'toyota', 'audi', 'bmw']
cars.reverse()
print(cars)

# Finding a length of a list is syntactically very different than the array.length method found in JS, instead it uses len(list) syntax

# Prints 4
print(len(cars))


