
def drawBoard():
    board = ""
    for i in range (dim+2):
        if i%2 == 0:
            board += "     |" * (dim-1)
        else :
            board += "- - - " * dim
        board += "\n"
    print(board) 


if __name__ == "__main__":
    dim = 3
    drawBoard()