theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

blank_Board = {'7': '7', '8': '8', '9': '9',
               '4': '4', '5': '5', '6': '6',
               '1': '1', '2': '2', '3': '3'}

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+--+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+--+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    # print('\n')


# Now we'll write the main function which has all the gameplay functionality.
def play_game():
    turn = 'X'
    count = 0

    player_1 = input("Enter player name 1 : ")
    player_2 = input("Enter player name 2 : ")

    first_player = True

    printBoard(blank_Board)

    while True:

        if first_player:
            position = input("\nIt's your turn," + player_1 + ". Move to which place? ")
            first_player = False
            turn = 'X'
        else:
            position = input("\nIt's your turn," + player_2 + ". Move to which place? ")
            first_player = True
            turn = '0'

        try:
            if int(position) > 9:
                print("\nPlease enter a position in between 1~9.")

                first_player = True if first_player == False else True
                continue

            if theBoard[position] == ' ':
                theBoard[position] = turn
                count += 1

                printBoard(theBoard)
            else:
                print("\nThat place is already filled. Move to which place? ")
                printBoard(theBoard)

                first_player = True if first_player == False else True
                continue

            # Now we will check if player X or O has won,for every move after 5 moves.
            if count >= 5:

                
                winner = player_1 if turn == "X" else player_2

                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                    print("\nGame Over.\n")
                    printBoard(theBoard)
                    print("**** " + winner + " won. ****")
                    break

                    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over. It's a Tie!!\n")
                printBoard(theBoard)
                break

        except ValueError:
            isInt = False

            if isInt:
                first_player = True if first_player == False else True
                print('Input value is an integer')
            else:
                first_player = True if first_player == False else True
                print('Invalid position. Please enter a position in between 1~9.\n')

    # Now we will ask if player wants to restart the game or not.
    restart = input("\n\nDo want to play Again?(y/n): ")
    if restart.upper() == "Y":
        for key in board_keys:
            theBoard[key] = " "

        play_game()


if __name__ == "__main__":
    play_game()
