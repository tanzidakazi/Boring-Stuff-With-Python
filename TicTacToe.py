theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(b):
    print(b['top-L'] + '|' + b['top-M'] + '|' + b['top-R'])
    print('-+-+-')
    print(b['mid-L'] + '|' + b['mid-M'] + '|' + b['mid-R'])
    print('-+-+-')
    print(b['low-L'] + '|' + b['low-M'] + '|' + b['low-R'])

turn='X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + ' .Postion?')
    move = input()
    theBoard[move]=turn
    if turn == 'X':
        turn = 'O]'
    else:
        turn='X'
printBoard(theBoard)
