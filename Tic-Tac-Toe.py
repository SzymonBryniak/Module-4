def display_board(board):
    print(board)
    return
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    ask_for_input = int(input('enter your move '))

    # for it in range(0, 9):
    #     for pos in board

    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    return print(ask_for_input in board[0][0])
# def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

# def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

# def draw_move(board):
    # The function draws the computer's move and updates the board.


plus = '+'
dash = '+-------'
pipe = '|'
a, b, c, d, e, f, g, h, i = '1', '2', 3, 4, 5, 6, 7, 8, 9
board_positions = [[[1], ['2'], [3]],
                   [[4], [5], [6]],
                   [[7], [8], [9]]]

board1 = f'''
+-------+-------+-------+
|       |       |       |
|   {a}   |   {b}   |   {c}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {d}   |   {e}   |   {f}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {g}   |   {h}   |   {i}   |
|       |       |       |
+-------+-------+-------+
'''
# board1 = ['+', '-------', '+', '-------', '+', '-------', '+']
# board2 = [dash for char in range(0, 1)]



display_board(board1)
enter_move(board_positions)
