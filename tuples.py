## Tuples
# Tuples are similar to lists, but are immutable, in that their values cannot be changed simply by reassignment
# We can create tuples by assignment to a pair of parentheses

dimensions = (200, 50)

# Prints
# 200
# 50
print(dimensions[0])
print(dimensions[1])

# If we try to change one of the values of the tuple, we will get an error, so the following will NOT work

# dimensions[0] = 250
# print(dimensions[0])

# Which returns the following error message:

# Traceback (most recent call last):
  # File "/home/brian/Documents/Code/python/python_crash_course/tuples.py", line 15, in <module>
    # dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

# Differentiating a tuple from a simple value within, say, a function, is done by providing at least one comma,
# So defining a tuple with just one value would be done like support

my_t = (3,)

# Looping through a Tuple
# Looping through a tuple is a simple as that of looping over a list

dimensions = (200, 50)
for 
