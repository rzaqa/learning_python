def beginning_zeros(a: str) -> int:
    digits = [int(i) for i in a]
    counter = 0
    if digits[0] == 0:
        for digit in digits:
            while digit == 0:
                counter += 1
        return counter
    else:
        return 0


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")


