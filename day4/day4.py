def findXs(board):
    X_pos = []
    for i,row in enumerate(board):
        for j,c in enumerate(row):
            if c == "X":
                X_pos.append((i,j))
    return X_pos

def findNeighboringXMAS(board, pos_X):
    ctr = 0
    pos_x, pos_y = pos_X

    #Check central axes
    if pos_y + 3 < len(board[pos_x]):
        right = ''.join(board[pos_x][pos_y:pos_y+4])
        if right == "XMAS":
            ctr += 1
    if pos_y - 3 >= 0:
        left = ''.join(board[pos_x][pos_y-3:pos_y+1])
        left = left[::-1]
        if left == "XMAS":
            ctr += 1
  
    if pos_x - 3 >= 0:
        #up = ''.join(board[pos_x-3:pos_x+1][pos_y])
        up = ""
        for i in range(pos_x-3, pos_x+1):
            up += board[i][pos_y]
        up = up[::-1]
        if up == "XMAS":
            ctr += 1

    if pos_x + 3 < len(board):
        down = ""
        for i in range(pos_x, pos_x+4):
            down += board[i][pos_y]
        if down == "XMAS":
            ctr += 1

    # Check Diagonals
    if pos_x - 3 >= 0 and pos_y - 3 >= 0:
        up_left = ""
        for i in range(0,4):
            up_left += board[pos_x-i][pos_y-i]
        if up_left == "XMAS":
            ctr += 1

    if pos_x - 3 >= 0 and pos_y + 3 < len(board[pos_x]):
        up_right = ""
        for i in range(0,4):
            up_right += board[pos_x-i][pos_y+i]
        if up_right == "XMAS":
            ctr += 1
    
    if pos_x + 3 < len(board) and pos_y - 3 >= 0:
        down_left = ""
        for i in range(0,4):
            down_left += board[pos_x+i][pos_y-i]
        if down_left == "XMAS":
            ctr += 1
    
    if pos_x + 3 < len(board) and pos_y + 3 < len(board[pos_x]):
        down_right = ""
        for i in range(0,4):
            down_right += board[pos_x+i][pos_y+i]
        if down_right == "XMAS":
            ctr += 1
    return ctr

def main():
    board = []
    part1_total = 0
    with open("day4.txt", "r") as f:
        for line in f:
            board.append(list(line.strip()))
        xs = findXs(board)
        for x in xs:
            part1_total += findNeighboringXMAS(board, x)
        print(part1_total) #Part 1: 2547

if __name__ == "__main__":
    main()