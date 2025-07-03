from platform import python_revision


def changing_direction(elements: list[int]) -> int:
    if len(elements) < 2:
        return 0

    counter = 0
    previous = elements[0]
    direction = 0  # 1 = up, -1 = down, 0 = undefined

    for current in elements[1:]:
        if current > previous:
            new_direction = 1
        elif current < previous:
            new_direction = -1
        else:
            new_direction = direction
        if new_direction != direction and direction != 0:
            counter +=1
        direction = new_direction
        previous = current

    return counter


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
print("The mission is done! Click 'Check Solution' to earn rewards!")