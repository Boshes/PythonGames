import random

def drawBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def playerLetter():
    letter = ''
    while not(letter=='X' or letter=='O'):
        print('X or O?')
        letter = raw_input().upper()
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def first():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def makeMove(board,letter,move):
    board[move] = letter

def freeSpace(board,move):
    return board[move] == ' '

def fullBoard(board):
    for i in range(1,10):
        if freeSpace(board,i):
            return False
    return True

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
        print('What is your next move?')
        move = raw_input()
    return int(move)

def randomMoveFromList(board,moves):
    possibleMoves = []
    for i in moves:
        if freeSpace(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

def isWinner(board,letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[7] == letter and board[4] == letter and board[1] == letter) or
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        (board[9] == letter and board[6] == letter and board[3] == letter) or
        (board[7] == letter and board[5] == letter and board[3] == letter) or
        (board[9] == letter and board[5] == letter and board[1] == letter))


def getBoard(board):
    copyBoard = []
    for i in board:
        copyBoard.append(i)
    return copyBoard

def computerMove(board,cLetter):
    if cLetter =='X':
        pLetter = 'O'
    else:
        pLetter = 'X'

    for i in range(1,10):
        copy = getBoard(board)
        if freeSpace(copy,i):
            makeMove(copy,cLetter,i)
            if isWinner(copy,cLetter):
                return i

    for i in range(1,10):
        copy = getBoard(board)
        if freeSpace(copy,i):
            makeMove(copy,pLetter,i)
            if isWinner(copy,pLetter):
                return i

    move = randomMoveFromList(board,[1,3,7,9])
    if move !=None:
        return move
    if freeSpace(board,5):
        return 5
    return randomMoveFromList(board, [2,4,6,8])

while True:
    board = [' ']*10
    pLetter, cLetter = playerLetter()
    turn = first()
    print('It\'s ' + turn +'\'s turn')
    isPlaying = True
    while isPlaying:
        if turn == 'player':
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board,pLetter,move)
            if isWinner(board,pLetter):
                drawBoard(board)
                print('Player wins')
                isPlaying = False
            else:
                if fullBoard(board):
                    drawBoard(board)
                    print('Tie')
                    break
                else:
                    turn = 'computer'
        else:
            move = computerMove(board,cLetter)
            makeMove(board,cLetter,move)
            if isWinner(board,cLetter):
                drawBoard(board)
                print('Computer wins')
                isPlaying = False
            else:
                if fullBoard(board):
                    drawBoard(board)
                    print('Tie')
                    break
                else:
                    turn = 'player'
