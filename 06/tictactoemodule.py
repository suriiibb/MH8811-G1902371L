


def temp(i):
    if i == 0:
        return "o"
    elif i == 1:
        return "X"
    elif i == 2:
        return " "

        


def drawBoard(board):
    
    size = len(board)
    result = ''
    counter1 = 0
    
    for i in board:
        counter1 += 1
        counter = 0
        for j in i:
            if counter < size -1:
                result += " " + temp(j) + " |"
                counter+=1

            else:
                result += " "+ temp(j)
                counter += 1
                result +="\n"
                if counter1 < size:

                    result += "--- " * size
        result +="\n"
    return result


board = [[0,1,2],[2,0,0],[1,1,2]]
print (drawBoard(board))



