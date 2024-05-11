import random as rd


free_fields = []
move = {'computer': [],
        'user': []

        }
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
            if board[bb][cc] == 'O' or board[bb][cc] == 'X':
                continue
            elif ask_for_input in board[bb][cc]:
                board[bb][cc] = 'O'


    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    #move[f'user choice {ask_for_input}'] = ['O']
    move['user'].append(ask_for_input)
    return  # to stage 2


def make_list_of_free_fields(board):  # stage 2
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    # board_positions = [[[1], [2], [3]],
    #                    [[4], [5], [6]],
    #                    [[7], [8], [9]]]
    for bb in range(0, 3):
        for cc in range(0, 3):
            if board[bb][cc][0] == '0' or board[bb][cc] == 'X':
                continue
            elif board[bb][cc][0] != 'O' or board[bb][cc] == 'X':
                free_fields.append(tuple((bb, cc)))

    return


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # board_positions = [[[1], [2], [3]],
    #                    [[4], [5], [6]],
    #                    [[7], [8], [9]]]

    wins = {
        'win1': [1, 2, 3],
        'win2': [4, 5, 6],
        'win3': [7, 8, 9],
        'win4': [1, 4, 7],
        'win5': [2, 5, 8],
        'win6': [3, 6, 9],
        'win7': [3, 5, 7],
        'win8': [1, 5, 9]
    }

    if move['computer'] in wins:
        print('yes')

    return


def draw_move(board):  # stage 3
    computer_input = rd.randrange(9)
    print(computer_input)
    computer_round = 0
    global move
    # The function draws the computer's move and updates the board.
    computer_round += 1
    loop_on = True

    while loop_on:
        for bb in range(0, 3):
            for cc in range(0, 3):
                if computer_input == board[bb][cc][0]:
                    move['computer'].append(board[bb][cc][0])
                    board[bb][cc] = 'X'
                    loop_on = False
                    break

                elif board[bb][cc] == 'O' or board[bb][cc] == 'X':
                    computer_input = rd.randrange(9)

                    continue

                ########## to reenter the loop at the same iteration
            # if computer_input in board[bb][cc]: # I need to  replace the variable here
    #move[f'computer choice {computer_input}'] = ['X']

    return


game_on = True
display_board(board_positions)
while game_on:
    enter_move(board_positions)
    display_board(board_positions)
    draw_move(board_positions)
    display_board(board_positions)
    print(move)



print(board_positions)



##################

#
# for out_iter in range(0, 8):
#     for in_iter in range(0, 2):
#         print(board_positions[out_iter-1][in_iter-1][0], end=' ')
#
#
# for i in xq:
#     print(i)
#     print(board_positions[i[0]][i[1]][0])
