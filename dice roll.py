import random
while True:
    input("Press Enter to roll the Dice...")
    print("You rolled:",random.randint(1,6))
    choice=input("Roll again? (yes/no):")
    if choice.lower() !="yes":
        break