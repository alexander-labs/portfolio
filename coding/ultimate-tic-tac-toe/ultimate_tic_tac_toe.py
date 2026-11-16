print('HAPPY BIRTHDAY!')
print('ULTIMATE TIC TAC TOE')

ultimateBoard = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

def print_board(tttList):
    '''print_board(tttList) -> None
    prints a tic-tac-toe board corresponding to tttList'''
    return [
    tttList[0]+'|'+tttList[1]+'|'+tttList[2],  #row 1
    '-+-+-',                                   #grid
    tttList[3]+'|'+tttList[4]+'|'+tttList[5],  #row 2
    '-+-+-',                                   #grid
    tttList[6]+'|'+tttList[7]+'|'+tttList[8]  #row 3
    ]

def print_ultimate_board(ultimateBoard):
    smallBoards = [print_board(b) for b in ultimateBoard]

    for i in (0, 3, 6):
        for j in range(5):
            print(smallBoards[i][j], '||', smallBoards[i+1][j], '||', smallBoards[i+2][j])
        if i < 6:
            print('======||=======||======')

def find_winner(tttList):
    '''find_winner(tttList) -> str
    returns the winner of the tic-tac-toe game in tttList
    return 'No winner' if neither player has won'''
    # list of winning lines
    winningLines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    # check all the winning lines
    for line in winningLines:
        if tttList[line[0]]==tttList[line[1]]==tttList[line[2]] and tttList[line[0]] in ['X','O']:
            # found a winner; return it
            return tttList[line[0]]
    # no winner found; return no winner
    return "No winner"

# Play the game
boardIndex1 = int(input('Player 1, please input a board number from 0-8: '))
placementIndex1 = int(input('Player 1, please input a placement number from 0-8: '))
ultimateBoard[boardIndex1][placementIndex1] = 'X'

placementIndex2 = int(input('Player 2, please input a placement number from 0-8: '))
ultimateBoard[placementIndex1][placementIndex2] = 'O'

isWinnerX = False
isWinnerO = False


while isWinnerX == False and isWinnerO == False:
# Player One moves
    if ultimateBoard[placementIndex2] == ['X']*9 or ultimateBoard[placementIndex2] == ['O']*9:
        while True:
            boardForP1 = int(input('Player 1, board already taken – choose any board 0-8: '))
            if not (ultimateBoard[boardForP1] == ['X']*9 or ultimateBoard[boardForP1] == ['O']*9):
                break
            print('Uhhh... that board is already taken too...')
    else:
        boardForP1 = placementIndex2
        print('Player 1 must play on board ' + str(boardForP1))

    while True:
        placementIndex1 = int(input('Player 1, choose a cell 0-8: '))
        if ultimateBoard[boardForP1][placementIndex1] == ' ':
            ultimateBoard[boardForP1][placementIndex1] = 'X'
            break
        else:
            print('Hey, are you cheating? Try again!')

    print_ultimate_board(ultimateBoard)
# Player Two moves
    if ultimateBoard[placementIndex1] == ['X']*9 or ultimateBoard[placementIndex1] == ['O']*9:
        while True:
            boardForP1 = int(input('Player 2, board already taken – choose any board 0-8: '))
            if not (ultimateBoard[boardForP1] == ['X']*9 or ultimateBoard[boardForP1] == ['O']*9):
                break
            print('Uhhh... that board is already taken too...')
    else:
        boardForP2 = placementIndex1
        print('Player 2 must play on board ' + str(boardForP2))

    while True:
        placementIndex2 = int(input('Player 2, choose a cell 0-8: '))
        if ultimateBoard[boardForP2][placementIndex2] == ' ':
            ultimateBoard[boardForP2][placementIndex2] = 'O'
            break
        else:
            print('Hey, are you cheating? Try again!')

    print_ultimate_board(ultimateBoard)
# Check if anybody won anything
    for i in range(9):
        if find_winner(ultimateBoard[i]) == 'X':
            for j in range(9):
                ultimateBoard[i][j] = 'X'
        if find_winner(ultimateBoard[i]) == 'O':
            for j in range(9):
                ultimateBoard[i][j] = 'O'

    ultimateTracker = []
    for b in ultimateBoard:
        w = find_winner(b)
        ultimateTracker.append(w if w in ('X','O') else ' ')
    didTheyWin = find_winner(ultimateTracker)

    if didTheyWin == 'X':
        print('Congratulations to X!')
        isWinnerX = True
    if didTheyWin == 'O':
        print('Congratulations to O!')
        isWinnerO = True
    else:
        print('No winner yet. If the board is full, that is a tie!')

    print('Board confirmation:')
    print_ultimate_board(ultimateBoard)
        
    print('Board confirmation:')
    print_ultimate_board(ultimateBoard)