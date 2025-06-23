def most_frequent(data: list[str]) -> str:
    data_set = {}
    for i in data:
        if i not in data_set:
            data_set[i] = 1
        else:
            data_set[i] += 1
    most_common = max(data_set, key=data_set.get)
    return most_common


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")





