 # milestone project 1
 # Tic Tac Toe Game
def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9] + '|')
    print(board[4] + '|' + board[5] + '|' + board[6] + '|')
    print(board[1] + '|' + board[2] + '|' + board[3] + '|')
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
print(display_board(test_board))

def input_player():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('player1: choose X or O:').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player1_marker, player2_marker = input_player()
print(player2_marker)

def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board,'$',8)
display_board(test_board)

def check_win(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[7] == mark and board[3] == mark and board[5] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark))

display_board(test_board)
print(check_win(test_board,'X'))

import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9):'))
    return position

def replay():
    choice = input('play again? Enter Yes or No:')
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' ']*10
    player2_marker, player1_marker = input_player()
    turn = choose_first()
    print(turn +' will go first.')

    play_game = input('Are you ready to play? Enter yes or no.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if check_win(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if check_win(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

