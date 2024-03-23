import random

def roll(numberDice, typeDice, modifier):
    result = 0
    dieRoll = random.randint(1, typeDice)
    i = 0
    while i < numberDice:
        result = dieRoll + modifier
        print(f"d{typeDice}: {dieRoll} + {modifier} = {result}")
        i += 1


            