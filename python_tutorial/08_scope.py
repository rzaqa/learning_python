# name = "Dave"
# def greeting():
#     print(name)
# greeting()

# name = "Dave"
# def greeting():
#     color = "blue"
#     print(color)
#     print(name)
# greeting()

# name = "Dave"
# def greeting(firstname):
#     color = "blue"
#     print(color)
#     print(name)
#     print(firstname)
#
# greeting("John")

# name = "Dave"
# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)
#
# greeting("John")

# name = "Dave"
# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)
#
# greeting("John")
#
# def another():
#     greeting("Dave")
# another()


# name = "Dave"
#
# def another():
#     color = "blue"
#
#     def greeting(name):
#         print(color)
#         print(name)
#
#     greeting("Dave")
# another()

# name = "Dave"
# count = 1
#
# def another():
#     color = "blue"
#     global count
#     count = 2
#     print(count)
#
#     def greeting(name):
#         print(color)
#         print(name)
#
#     greeting("Dave")
#
# another()


# name = "Dave"
# count = 1
#
# def another():
#     color = "blue"
#     count += 1
#     print(count)
#
#     def greeting(name):
#         print(color)
#         print(name)
#
#     greeting("Dave")
#
# another()

name = "Dave"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()











