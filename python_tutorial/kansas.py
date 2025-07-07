from random import choice
capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfacts():
    funfacts = [
        "Fact1",
        "Fact2",
        "Fact3",
        "Fact4",
    ]

    index = choice("0123")
    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfacts()