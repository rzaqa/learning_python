def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    data_copy = data.copy()
    result = []

    while len(result) < limit and data_copy:
        max_price = -1
        max_item = None

        for item in data_copy:
            if item["price"] > max_price:
                max_price = item["price"]
                max_item = item
        result.append(max_item)
        data_copy.remove(max_item)
    return result


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")



