import re


def sum_numbers(text: str) -> int:
    numbers = re.findall(r"\b\d+\.?\d*\b", text)
    print(f"Numbers are: {numbers}")
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return int(numbers[0])
    else:
        return sum(int(n) for n in numbers)

    # better solution
    # sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())



print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")