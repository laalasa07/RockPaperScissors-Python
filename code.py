import random

def rule(player, computer):
    if player == computer:
        return 0
    if player == 'r' and computer == 'p':
        return -1
    elif player == 's' and computer == 'p':
        return 1
    elif player == 'p' and computer == 'r':
        return 1
    elif player == 's' and computer == 'r':
        return -1
    elif player == 'r' and computer == 's':
        return 1
    elif player == 'p' and computer == 's':
        return -1

def main():
    print("\t\t\t\t", end="")
    print("-" * 50)
    print("\t\t\t\t\t Welcome to Rock, Paper, and Scissors Game")
    print("\t\t\t\t", end="")
    print("-" * 50)
    print("\t\t\t\t\t Note: ")
    print("\t\t\t\t\t\t r : Rock")
    print("\t\t\t\t\t\t p : Paper")
    print("\t\t\t\t\t\t s : Scissors")
    print("\t\t\t\t", end="")
    print("-" * 50)

    while True:
        # Computer's choice
        number = random.randint(0, 99)
        if number < 33:
            computer = 'r'
        elif number > 66:
            computer = 's'
        else:
            computer = 'p'

        # Player's choice
        player = input("\t\t\t\tEnter your choice (r/p/s): ").lower()
        while player not in ['r', 'p', 's']:
            print("\t\t\t\tInvalid choice! Please try again.")
            player = input("\t\t\t\tEnter your choice (r/p/s): ").lower()

        # Determine the result
        result = rule(player, computer)
        if result == 1:
            print("\t\t\t\tYou won! Hurray")
        elif result == -1:
            print("\t\t\t\tYou lose! Bad Luck")
        else:
            print("\t\t\t\tWoah! That's a Tie!")

        # Ask to play again
        playmore = input("\t\t\t\tDo you want to Play Again? (Press 'n' to exit, or anything else to continue): ").lower()
        if playmore == 'n':
            break

        print("\t\t\t\t", end="")
        print("-" * 50)

if __name__ == "__main__":
    main()
