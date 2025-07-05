def between_markers(text: str, begin: str, end: str) -> str:
    start_index = text.find(begin)
    end_index = text.find(end)

    if start_index == -1:
        start_index = 0
    else:
        start_index += len(begin)

    if end_index == -1:
        end_index = len(text)

    if end_index < start_index:
        return ""

    return text[start_index:end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")




