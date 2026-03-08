def findStart(board):
    y = 0
    for i,lst in enumerate(board):
        if '^' in lst:
            y = lst.index('^')
            return (i,y)
    return (-1, -1)

def iterate(board, pos, d):
    visited = set()
    while not(exit_game(board, pos, d)):
        visited.add(pos)
        # Pound-sign case
        x, y = pos
        if d == 'u':
            if x - 1 >= 0 and board[x-1][y] != '#': #Empty space
                pos = (x-1, y)
            else: # Change direction
                d = changeDir(d)
        elif d == 'r':
            if y + 1 <= len(board[x]) - 1 and board[x][y+1] != '#':
                pos = (x, y+1)
            else:
                d = changeDir(d)
        elif d == 'd':
            if x + 1 <= len(board) - 1 and board[x+1][y] != '#':
                pos = (x+1, y)
            else:
                d = changeDir(d)
        else:
            if y - 1 >= 0 and board[x][y-1] != '#':
                pos = (x, y-1)
            else:
                d = changeDir(d)
    visited.add(pos)
    return len(visited)

def changeDir(d):
    if d == 'u':
        return 'r'
    if d == 'r':
        return 'd'
    if d == 'd':
        return 'l'
    return 'u'

def exit_game(board, pos, d):
    x, y = pos
    if d == 'u' and x <= 0:
        return True
    if d == 'r' and y >= len(board[x]) - 1:
        return True
    if d == 'd' and x >= len(board) - 1:
        return True
    if d == 'l' and y <= 0:
        return True
    return False

def main():
    board = []
    with open("day6.txt", "r") as f:
        for l in f:
            board.append(list(l.strip()))
        start = findStart(board)
        print(iterate(board, start, 'u'))


if __name__ == "__main__":
    main()