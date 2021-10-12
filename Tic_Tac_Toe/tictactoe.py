global board, player
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "O"


'''
Main method
'''
def main():
    tictac()


'''
Print the board in a visually pleasing way
'''
def printBoard():
    for line in board:
        print(line)


'''
Take in user input and replace the appropriate space
'''
def makeMove():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

    x = int(input(f"Player {player} what is the X coordinate? "))
    y = int(input(f"Player {player} what is the Y coordinate? "))

    while board[y-1][x-1] != " ":
        print("You must choose an empty spot!")
        x = int(input(f"Player {player} what is the X coordinate? "))
        y = int(input(f"Player {player} what is the Y coordinate? "))

    if player == "X":
        board[y - 1][x - 1] = "X"
    else:
        board[y - 1][x - 1] = "O"


'''
Did the player that just go win?
'''
def isWin():
    # Rows
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                break
        if win:
            return True

    # Column
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                break
        if win:
            return True

    # Top left to bottom right diagonal
    win = True
    for i in range(3):
        if board[i][i] != player:
            win = False
            break
    if win:
        return True

    # Bottom left to top right diagonal
    win = True
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] != player:
            win = False
            break
    if win:
        return True

    return False


'''
Determine if game is a stalemate
'''
def isCat():
    for line in board:
        if " " in line:
            return False

    if not isWin():
        return True

'''
Game controller
'''
def tictac():
    while not isWin() and not isCat():
        printBoard()
        makeMove()
    printBoard()
    print("GAMEOVER")
    if not isCat():
        print(f"{player} WINS!!!")
    else:
        print("CAT")


if __name__ == '__main__':
    main()