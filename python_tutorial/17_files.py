import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

# f = open("names.txt", "r")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)
# f.close()
#
# try:
#     f = open("name_files.txt", "r")
#     print(f.read())
# except:
#     print("The file you want to read doesn't exist")
# finally:
#     f.close()

# Append

# f = open("names.txt", "a")
# f.write("Neil\n")
# f.close()
#
# f = open("names.txt", "r")
# print(f.read())
# f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted al of the context")
f.close()

# Two ays to create a new file
# Opens a file for writing, creates the file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# Creates teh specified file, but returns an error,
# if the file exist

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file
# avoid an error if it doesn't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")


with open("names.txt") as f:
    content = f.read()

with open("name_list.txt", "w") as f:
    f.write(content)






