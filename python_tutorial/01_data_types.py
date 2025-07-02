import math

#String data type

# literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Construction function

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = first + " " + last
# fullname += "!"
# print(fullname)

# Casting a number to a string
decade = str(1980)
# print(type(decade))

statement = "I like rock music from " + decade + "s. "
# print(statement)

# Multiple lines
multiple = """
Hey, how are you? 

I was just checking in. 
                All good? 
"""
# print(multiple)

# Escaping special characters
sentence = 'I\'m back at work! \t Hey! \n\nWhere\'s this at\\located'
# print(sentence)

# String Methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiple.title())
# print(multiple.replace("good", "ok"))
# print(multiple)

# print(len(multiple))
multiple += "                                                "
multiple = "              " + multiple
# print(len(multiple))

# print(len(multiple.strip()))
# print(len(multiple.lstrip()))
# print(len(multiple.rstrip()))

# Build a menu
title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# print("")
# String index value
# print(first[0])
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# Some methods return boolean data
# print(first.startswith("D"))
# print(first.endswith("Z"))



# Boolean data type
myvalue = True
x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))
# ================================================================================================

# Numeric data types
price = 100
best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
# print(type(gpa))
# print(type(y))

# Complex type
comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Built-in functions for numbers
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))

# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if cast incorrect data
# zip_value = int("New York") #  ValueError: invalid literal for int() with base 10: 'New York'



