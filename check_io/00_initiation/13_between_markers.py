def between_markers(text: str, start: str, end: str) -> str:
    start_index = 0
    end_index = 0
    for symbol in text:
        if symbol == start:
            start_index = text.index(symbol)
            print(start_index)
        elif symbol == end:
            end_index = text.index(symbol)
            print(end_index)

    return text[start_index+1:end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
