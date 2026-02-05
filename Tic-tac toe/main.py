import random

# Define the sum function
sum = lambda x, y, z: x + y + z

def printBoard(xstate, zstate):
    symbols = ["X", "O"]
    boards = [(symbols[0] if xstate[i] else (symbols[1] if zstate[i] else i)) for i in range(9)]
    print(f'\n{boards[0]} | {boards[1]} | {boards[2]}')
    print('--|---|--')
    print(f'{boards[3]} | {boards[4]} | {boards[5]}')
    print('--|---|--')
    print(f'{boards[6]} | {boards[7]} | {boards[8]}')

def get_comp_move(xstate, zstate):
    avail_position = [i for i in range(9) if not xstate[i] and not zstate[i]]
    return random.choice(avail_position)

def checkWins(xstate, zstate):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:  # Check for X
            print("X won the Match")
            return 1
        if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:  # Check for O
            print("O won the Match")
            return 0
        
    return -1

# Function to get the user's symbol choice
def get_user_symbol():
    while True:
        user_choice = input("Choose your symbol (X or O): ").upper()
        if user_choice == 'X' or user_choice == 'O':
            return user_choice
        else:
            print("Invalid input. Please choose 'X' or 'O'.")

# Main function
def main():
    # Get user's choice of symbol
    user_symbol = get_user_symbol()
    computer_symbol = 'O' if user_symbol == 'X' else 'X'
    
    # Initialize game states
    xstate = [0 for _ in range(9)]  # Player X's state
    zstate = [0 for _ in range(9)]  # Player O's state

    print("Welcome to Tic Tac Toe")
    print(f"You are {user_symbol} and the computer is {computer_symbol}")

    while True:
        printBoard(xstate, zstate)

        # Player's turn
        while True:
            try:
                if user_symbol == 'X':
                    value = int(input("Enter a value (0-8):"))
                else:
                    value = int(input("Enter a value (0-8):"))
                if value < 0 or value > 8:
                    print("Enter a value between (0-8)")
                    continue

                if xstate[value] or zstate[value]:
                    print("Position is already taken")
                    continue

                if user_symbol == 'X':
                    xstate[value] = 1  # Player X's move
                else:
                    zstate[value] = 1  # Player O's move
                break
            except ValueError:
                print("Invalid input")
                continue

        if checkWins(xstate, zstate) == 1:
            printBoard(xstate, zstate)
            print("Match Over")
            break

        # Computer's turn
        comp_move = get_comp_move(xstate, zstate)
        if computer_symbol == 'X':
            xstate[comp_move] = 1  # Player X's move (Computer)
        else:
            zstate[comp_move] = 1  # Player O's move (Computer)

        printBoard(xstate, zstate)
        print(f"Computer ({computer_symbol}) placed at position {comp_move}")

        if checkWins(xstate, zstate) == 0:
            printBoard(xstate, zstate)
            print("Match Over")
            break

# Run the game
main()
