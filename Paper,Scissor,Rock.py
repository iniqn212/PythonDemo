import random

weapons = ["rock", "scissor", "paper"]

result = "null"

print("make a choice : paper , scissor or rock")
print()
print()
print("Use word cheat to see ComputerChoice :) ")
print()
print()

humanWinsScore = 0
computerWinsScore = 0


while True:
    computerChoice = random.choice(weapons)

    while result != "H_win" or "C_win":
        humanChoice = input("Enter your choice here:").lower().strip()
        if humanChoice in ("rock","paper","scissor"):
            pass
        elif humanChoice == "cheat":
            print(computerChoice)
            humanChoice = input("Enter your choice here:").lower().strip()
            if humanChoice in ("rock", "paper", "scissor"):
                pass
            else:
                 print("Wrong input, try again")
                 humanChoice = input("Enter your choice here:").lower().strip()
        else:
            print("Wrong input, try again")
            humanChoice = input("Enter your choice here:").lower().strip()


        if humanChoice == computerChoice:
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Draw")
            print("Choice again")
            print()
            result = "draw"

        elif humanChoice == "rock" and computerChoice == "scissor":
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Human win")
            result = "H_win"
            humanWinsScore = +1
            break

        elif humanChoice == "rock" and computerChoice == "paper":
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Computer win")
            result = "C_win"
            computerWinsScore = +1
            break

        elif humanChoice == "scissor" and computerChoice == "paper":
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Human win")
            result = "H_win"
            humanWinsScore = +1
            break

        elif humanChoice == "scissor" and computerChoice == "rock":
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Computer win")
            result = "C_win"
            computerChoice = +1
            break

        elif humanChoice == "paper" and computerChoice == "rock":
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Human win")
            result = "H_win"
            humanWinsScore = +1
            break

        elif humanChoice == "paper" and computerChoice == "scissor":
            print("Computer:", computerChoice)
            print(humanChoice, "vs", computerChoice)
            print("Computer win")
            result = "C_win"
            computerWinsScore = +1
            break

    more_games = input("Would you like more calculations? (y/n): ")
    if more_games == "n":
        print()
        print("Human Score is:", humanWinsScore, "VS", "Computer Score is:", computerWinsScore)
        humanWinsScore = 0
        computerWinsScore = 0
        break
