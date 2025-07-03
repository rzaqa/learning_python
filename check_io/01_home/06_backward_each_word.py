def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return ""
    splited = text.split(" ")
    new_order_list = []
    for word in splited:
        new_word = word[::-1]
        new_order_list.append(new_word)
    return " ".join(new_order_list)

word = "string"
print(word[::-1])


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
