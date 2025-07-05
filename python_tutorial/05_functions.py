
# def sum(num1, num2):
#     if (type(num1) is not int or type(num2) is not int):
#         return
#     return num1 + num2
#
# total = sum("2", 3)
# print(total)

# def sum(num1, num2=3):
#     if (type(num1) is not int or type(num2) is not int):
#         return
#     return num1 + num2
#
# total = sum(1)
# print(total)

# def sum(num1=0, num2=0):
#     if (type(num1) is not int or type(num2) is not int):
#         return
#     return num1 + num2
#
# total = sum()
# print(total)

#
# def sum(num1=0, num2=0):
#     if (type(num1) is not int or type(num2) is not int):
#         return 0
#     return num1 + num2
#
# total = sum()
# print(total)


# def multiple_items(*args):
#     print(args)
#     print(type(args))
#
# multiple_items("Dave", "John", "Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave",second = "John", last = "Sara")












