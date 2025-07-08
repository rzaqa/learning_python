# Recursive function for factorial
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5)) # -> 120
print(fact(4)) # -> 24
print(fact(3)) # -> 6










