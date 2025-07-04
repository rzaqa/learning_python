band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")
print(band)
print(band2)
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# Print all keys
print(band.keys())
print(band.items())

# verify jey exists
print("guitar" in band)
print("triangle" in band)


band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove
print(band.pop("bass"))
print(band)

band["drams"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete and clear
band["drams"] = "Bonham"
del band["drams"]
print(band)

band2.clear()
print(band2)
del band2

# Copy dictionaries
# band2 = band # create a reference
# print("Bad copy! ")
# print(band2)
# print(band)
#
# band2["drams"] = "Dave"
# print(band)


band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)

# Or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)


# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}


band = {
    "member1":member1,
    "member2":member2
}
print(band)
print(band["member1"]["name"])

# Sets
nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No duplicates allowed

nums = {1,2,2,3}
print(nums)

nums = {1, True, 2, False, 3,4,0}
print(nums)

to_order = {10, 5,2 ,3,1,0,6,8,4,2}
print(to_order) # {0, 1, 2, 3, 4, 5, 6, 8, 10}

# Check if value in a set
print(2 in nums)

# But you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)


# You can use update with lists, tuples and dictionaries too.
# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset) # {1, 2, 3, 5, 6, 7}

# Keep only duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one) # {2, 3}

# Keep everything except duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one) # {1, 4}
