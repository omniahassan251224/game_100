#File: CS112_A1_T2_GameNumber1_20231027
#Purpuse:the game aim to create competition between two players start from 0 and alternatively add anumber from 1 to 10 to the sum
#the player who reaches 100 wins
#Author: Omnia Hassan Sayed
#ID:20231027



def game_100():
    # Welcome message and game instructions
    print("Welcome to our game!")
    print("The game requires two players.")
    print("Each player should enter a number from 1 to 10.")
    print("The player who reaches the sum of 100 first wins, and the game ends.")

    sum = 0

    # Main game loop
    while sum < 100:
        try:
            # Player 1's turn
            move = int(input('Player 1: Please enter a number from 1 to 10: '))
            # Validate input to be within the range [1, 10]
            while move < 1 or move > 10:
                move = int(input('Invalid input. Player 1: Please enter a number from 1 to 10: '))
            # Ensure the sum doesn't exceed 100
            while sum + move > 100:
                move = int(input('Player 1: Please enter a number from 1 to 10 without going over 100: '))
            # Update the sum
            sum += move
            print(f'Now we have {sum}')
            # Check if Player 1 has won
            if sum >= 100:
                print('Player 1 is the winner!')
                break

            # Player 2's turn
            move = int(input('Player 2: Please enter a number from 1 to 10: '))
            while move < 1 or move > 10:
                move = int(input('Invalid input. Player 2: Please enter a number from 1 to 10: '))
            while sum + move > 100:
                move = int(input('Player 2: Please enter a number from 1 to 10 without going over 100: '))
            sum += move
            print(f'Now we have {sum}')
            # Check if Player 2 has won
            if sum >= 100:
                print('Player 2 is the winner!')
                break
        except ValueError:
            print("Please enter a valid integer.")


# Call the function to start the game
game_100()
