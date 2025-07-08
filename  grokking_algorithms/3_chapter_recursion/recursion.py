# Recursion with a base depth 996 times - don't use it
# def countdown(i):
#     print(i)
#     countdown(i-1)
# countdown(5)

# Recursion with a base case and recursive case
def countdown(i):
    print(i)
    if i <= -100:
        return
    else:
        countdown(i -1)
countdown(5)












