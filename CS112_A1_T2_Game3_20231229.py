
# Purpose: This game purpose it that each player removes a pile of non-zero square coins and the winner
# is the player who removes tha last coin
# Author: Maria Atef Edward Marid


# this functions allows the computer to choose a random non-zero and non-square number
import random
import math
def random_non_square():
    while True:
        num = random.randint(100, 500)
        # I used math.isqrt to calculate the square of a number
        sqrt = math.isqrt(num)
        if sqrt * sqrt != num:
            return num

# this functions ensures that the players removes a non-zero square number of coins.
def  get_valid_moves(pile):
    return [x ** 2 for x in range(1, int(math.sqrt(pile)) + 1)]

# this function allows the user to choose a non-zero and non-sqaured number between 1 and 1000
def manual_choice(pile):
    while True:
        choice = int(input("Please choose a number between 1 and 1000: "))
        if choice <= 0 or math.isqrt(choice) ** 2 == choice or choice > 1000:
            print("Invalid number, please try again")
        else:
            return choice



# functions for player 1 and 2
def player_2():
    valid_moves = get_valid_moves(pile)
    while True:
        move = int(input("Player 2, remove a number of coins: "))
        # checking on 3 things whether move is 0 or less , not a square number & more than pile to print invalid
        if move not in valid_moves :
            print("Invalid input, Please pick a non-zero,square number of coins")
        else:
            return move

def player_1():
    valid_moves = get_valid_moves(pile)
    while True:
        move = int(input("Player 1,remove a number of coins: "))
        if move not in valid_moves :
            print("Invalid input, Please pick a non-zero,square number of coins")
        else:
            return move

# game loop
pile = 0
while True:
    print("Subtract a square")
    choice2 = input("A generate a random number, B to choose a number between 1 and 1000: ").lower()
    if choice2 == 'a':
        pile = random_non_square()
        print("Initial pile size:", pile)
    elif choice2 == 'b':
        pile = manual_choice(pile)
        print("Initial pile size:", pile)

    while pile > 0:
        print("\nPlayer 1's turn")
        coins_removed = player_1()
        pile -= coins_removed
        print("Pile size after Player 1's turn:", pile)
        if pile <= 0:
            print("Player 1 wins!")
            break

        print("\nPlayer 2's turn")
        coins_removed = player_2()
        pile -= coins_removed
        print("Pile size after Player 2's turn:", pile)
        if pile <= 0:
            print("Player 2 wins!")
            break
    # give the user a choice to play again or not
    while True:
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y' and play_again != 'n':
            print("Invalid input. Please enter 'Y' or 'N'.")
        else:
            break

    if play_again == 'n':
        print("Game over")
    break


