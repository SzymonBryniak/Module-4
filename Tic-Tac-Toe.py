import random as rd

free_fields = []
free_fields_display = []

board_positions = [[[1], [2], [3]],
                   [[4], [5], [6]],
                   [[7], [8], [9]]]


def display_board(board):
    abc_counter = 0
    abc = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
    abcd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    abc2 = {}
    for ii in range(0, 3):
        for kk in range(0, 3):
            abc2.update({abcd[abc_counter]: board[ii][kk][0]})
            abc_counter += 1
    #print(abc2, board[-1])

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    board1 = f'''
+-------+-------+-------+
|       |       |       |
|   {abc2['a']}   |   {abc2['b']}   |   {abc2['c']}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {abc2['d']}   |   {abc2['e']}   |   {abc2['f']}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {abc2['g']}   |   {abc2['h']}   |   {abc2['i']}   |
|       |       |       |
+-------+-------+-------+
    '''
    print(board1)
    return


def enter_move(board):                              # start
    ask_for_input = int(input('enter your move '))

    for bb in range(0, 3):
        for cc in range(0, 3):
            if ask_for_input in board[bb][cc]:  #tuples of free spaces to be used instead of the list due to TypeError
                board[bb][cc] = 'O'
                board.append(ask_for_input)

    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    #board.append(ask_for_input)
    make_list_of_free_fields(board)
    return board   # to stage 2


def make_list_of_free_fields(board):  # stage 2
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    for bb in range(0, 3):
        for cc in range(0, 3):
            if board[bb][cc][0] == '0':
                continue

            free_fields.append(tuple((bb, cc)))
            free_fields_display.append(tuple((bb+1, cc+1)))

    return print(free_fields)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    return


def draw_move(board):  # stage 3
    computer_input = rd.randint(1, 9)
    # The function draws the computer's move and updates the board.
    for bb in range(0, 3):
        for cc in range(0, 3):
            if computer_input in board[bb][cc]: # I need to  replace the variable here
                board[bb][cc] = '0'
                board.append(ask_for_input)

    make_list_of_free_fields(board)
    return


game_on = True

#while game_on:
display_board(board_positions)
board_positions = enter_move(board_positions)

## if make list > 0 draw

##################

x = [(1, 1), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
xq = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
board_positions = [[[1], [2], [3]],
                   [[4], [5], [6]],
                   [[7], [8], [9]]]

to_check = []
add = 0



#
# for out_iter in range(0, 8):
#     for in_iter in range(0, 2):
#         print(board_positions[out_iter-1][in_iter-1][0], end=' ')
#
#
# for i in xq:
#     print(i)
#     print(board_positions[i[0]][i[1]][0])