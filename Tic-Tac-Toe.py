def display_board(board):
    print(board)
    abc_counter = -1
    a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
    abc = [a, b, c, d, e, f, g, h, i]
    for ii in range(0, 3):
        for kk in range(0, 3):
            abc_counter += 1
            abc[abc_counter] = board[ii][kk]
            print(abc_counter, board[ii][kk])

    abc_counter += 1

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
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
    return print(board1), print(abc, abc_counter)


def enter_move(board):
    ask_for_input = int(input('enter your move '))

    for bb in range(0, 3):
        for cc in range(0, 3):
            if ask_for_input in board[bb][cc]:
                #print('yes')
                board[bb][cc] = 'O'

    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    return display_board(board)
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

board_positions = [[[1], [2], [3]],
                   [[4], [5], [6]],
                   [[7], [8], [9]]]


'''
# board1 = ['+', '-------', '+', '-------', '+', '-------', '+']
# board2 = [dash for char in range(0, 1)]


enter_move(board_positions)

'''
enter_move(board_positions)
