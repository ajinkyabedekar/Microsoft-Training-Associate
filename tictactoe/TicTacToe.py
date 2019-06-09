import random
import os


# for printing the grid after each move as well as before the game
def draw_grid(grid):
    print("   ||   ||   ")
    print(" " + grid[1] + " || " + grid[2] + " || " + grid[3])
    print("   ||   ||   ")
    print("=============")
    print("   ||   ||   ")
    print(" " + grid[4] + " || " + grid[5] + " || " + grid[6])
    print("   ||   ||   ")
    print("=============")
    print("   ||   ||   ")
    print(" " + grid[7] + " || " + grid[8] + " || " + grid[9])
    print("   ||   ||   ")


# for receiving the input for the grid
def input_grid():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input("What would you like to play with 'X' or 'O' : ").upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# randomly deciding who plays first the player or the computer
def who_plays_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


# yes or no function asking the user whether he wants to play again or not
def yes_or_no():
    return input("Do you want to play again? ( yes or no) : ").lower().startswith('y')


# assigning the letter to the grid
def m_move(grid, letter, move):
    grid[move] = letter


# returning true for all the winning cases
def check_winner(grid, l):
    return ((grid[1] == l and grid[2] == l and grid[3] == l) or  # horizontal top
            (grid[4] == l and grid[5] == l and grid[6] == l) or  # horizontal middle
            (grid[7] == l and grid[8] == l and grid[9] == l) or  # horizontal bottom
            (grid[1] == l and grid[4] == l and grid[7] == l) or  # vertical left
            (grid[2] == l and grid[5] == l and grid[8] == l) or  # vertical middle
            (grid[3] == l and grid[6] == l and grid[9] == l) or  # vertical right
            (grid[1] == l and grid[5] == l and grid[9] == l) or  # diagonal 1-5-9
            (grid[3] == l and grid[5] == l and grid[7] == l))    # diagonal 3-5-7


# duplicating the grid list and returning the duplicate
def grid_copy(grid):
    d_grid = []
    for i in grid:
        d_grid.append(i)
    return d_grid


# return true if the slot in the grid is empty
def check_space_free(grid, move):
    return grid[move] == ' '


# the user entering his move
def player_move(grid):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_space_free(grid, int(move)):
        move = input("Next move please (1 - 9) : ")
    return int(move)


# to return a valid move from the grid list if not None
def selecting_random_moves_from_list(grid, move_list):
    possible_move = []
    for i in move_list:
        if check_space_free(grid, i):
            possible_move.append(i)

    if len(possible_move) != 0:
        return random.choice(possible_move)
    else:
        return None


def computer_move(grid, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # checking if we can win in the next move
    for i in range(1, 10):
        copy = grid_copy(grid)
        if check_space_free(copy, i):
            m_move(copy, computer_letter, i)
            if check_winner(copy, computer_letter):
                return i

    # checking if the player can win in the next move
    for i in range(1, 10):
        copy = grid_copy(grid)
        if check_space_free(copy, i):
            m_move(copy, player_letter, i)
            if check_winner(copy, player_letter):
                return i

    # next try to take one of the corners if available
    move = selecting_random_moves_from_list(grid, [1, 3, 7, 9])
    if move != None:
        return move

    # try to take the center if available
    if check_space_free(grid, 5):
        return 5

    # next is moving on one of the sides that are available
    return selecting_random_moves_from_list(grid, [2, 4, 6, 8])


# if board is full
def check_board_full(grid):
    for i in range(1, 10):
        if check_space_free(grid, i):
            return False
    return True


while True:
    os.system('cls')
    print("\t \t  TicTacToe.exe")
    the_grid = [' '] * 10
    player_letter, computer_letter = input_grid()
    turn = who_plays_first()
    print(turn + " plays first")
    continue_game = True

    while continue_game:
        # players turn
        if turn == 'player':
            draw_grid(the_grid)
            move = player_move(the_grid)
            m_move(the_grid, player_letter, move)

            if check_winner(the_grid, player_letter):
                draw_grid(the_grid)
                print(" The player (you) have won the game")
                continue_game = False
            else:
                if check_board_full(the_grid):
                    draw_grid(the_grid)
                    print("The game ends in a tie !!!")
                    break
                else:
                    turn = 'computer'

        else:
            # computers turn
            move = computer_move(the_grid, computer_letter)
            m_move(the_grid, computer_letter, move)

            if check_winner(the_grid, computer_letter):
                draw_grid(the_grid)
                print(" The Computer have won the game")
                continue_game = False
            else:
                if check_board_full(the_grid):
                    draw_grid(the_grid)
                    print("The game ends in a tie !!!")
                    break
                else:
                    turn = 'player'

    if not yes_or_no():
        break
