# squared = lambda num : num * num
# print(squared(2))
#
# def squared(num): return num * num
# print(squared(3))
#
# addTwo = lambda num : num + 2
# print(addTwo(5))
#
# sum = lambda a, b : a + b
# print(sum(2,2))

###########################################################################

# def funcBuilder(x):
#     return lambda num : num + x
#
# addTen = funcBuilder(10)
# addTwenty = funcBuilder(20)
#
# print(addTen(7))
# print(addTwenty(7))

###########################################################################
# numbers = [3,7,12,18,20,21]
# squared_nums = map(lambda num : num * num, numbers)
# print(list(squared_nums))

###########################################################################
# numbers = [3,7,12,18,20,21]
# odd_nums = filter(lambda num : num % 2 != 0, numbers)
# print(list(odd_nums))

###########################################################################
from functools import reduce
numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr : acc + curr , numbers) # 16
print(total)

print(sum(numbers)) # 16

numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr : acc + curr , numbers, 10)
print(total) # 26

###########################################################################
names = ["Dave Gray", "Sara Ito", "John JAcob Jingleheimerschmidt"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(char_count) # 47






