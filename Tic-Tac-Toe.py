# def display_board(board):
#     print('')
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


# def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


# def draw_move(board):
    # The function draws the computer's move and updates the board.

board = [[[[]]]]
plus = '+'
dash = '-'
pipe = '|'
'''
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
'''

board2 = [[dash for char in range(0, 6)] for char1 in range(0, 3)]
board1 = ['+', '-------', '+', '-------', '+', '-------', '+']


board1_join = ''.join(board1)
board2_join = []
for ele in range(len(board2)):
    board2_join += ''.join(board2[ele])


print(board1_join)
print(board2)
print(board2_join)
