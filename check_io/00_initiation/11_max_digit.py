def max_digit(value: int) -> int:
    max_digit = 0
    digits = [int(i) for i in str(value)]
    for digit in digits:
        if digit > max_digit:
            max_digit = digit
    return max_digit


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")