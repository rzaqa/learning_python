# person = "Dave"
# coins = 3

# print(f"\n ")
# message = "\n%s has %s coins left." % (person, coins)
# print(message)

# f-strings
# player = {"person": "Karen", "coins": 7}
# print(f"{player["person"]} has {player["coins"]} coins left.")


# print(f"{person} has {coins} coins left.")
# print(f"{person.lower()} has {2*5} coins left.")


# You can pass formatting options
num = 10
# print(f"\n2.25 times {num} is {2.25*num:.2f}")
# print(f"\n2.25 times {num} is {2.25*num:.2}")


for num in range(1,11):
    print(f"2.25 times {num} is {2.25*num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
