users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

# print("Dave" in users)
# print(users[0])
# print(users[-1])
# print(users.index("Sara"))
# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(len(users))

users.append("Elsa")
# print(users)
# users += "Catherin Max Viktor"
# print(users)

users += ["Jason"]
# print(users)

users.extend(["Robert", "Jimmy"])
# print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)
users[2:2] = ["Eddie", "Alex"]
# print(users)
users[1:3] = ["Robert", "JPJ"]
# print(users)




users.remove("Bob")
# print(users)
# print(users.pop())
del users[0]
# print(users)

# del data
data.clear()
# print(data)

print("========="*20)
users[1:2] = ["dave"]
users.sort()
print(users)
users.sort(key=str.lower)
# print(users)
# print("========="*20)
nums = [4, 42, 78, 1,5]
nums.reverse()
# print(nums)

# nums.sort(reverse=True)
# print(nums)
# print("*"*15)
# print(sorted(nums, reverse=True))
# print(nums)



# print("SMALL TASK")
# digits = [1,2,3,4,5]
# new_order = []
# for i in digits[::-1]:
#     new_order.append(i)
# print(new_order)
# print("========="*20)


# print(nums)
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
# print(numscopy)
# print(mynums)
# print(mycopy)

# Tuple

mytuple = tuple(("Dave", 42, True))
anothertuple = (1,4,2,8,2,2)
print(type(mytuple))


newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))











