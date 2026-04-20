def findUniquePieces(board):
    pieces = set()
    for row in board:
        pieces = pieces.union(set(row))
    pieces.remove(".") # remove empty
    return pieces

def determineAntinodes(board):
    pieces = findUniquePieces(board)
    antinodes = set()
    for p in pieces:
        antinodes = antinodes.union(_determineAntinodes(board, p))
    return antinodes

def determineAntinodesTFreq(board):
    pieces = findUniquePieces(board)
    antinodes = set()
    for p in pieces:
        antinodes = antinodes.union(_determineAntinodesTFreq(board, p))
    return antinodes

def _determineAntinodes(board, piece):
    antinodes = set()
    pos = getPosPieces(board, piece)
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            pos_x1, pos_y1 = pos[i] # A
            pos_x2, pos_y2 = pos[j] # B
            dx = pos_x2 - pos_x1 # difference vector (dx, dy)
            dy = pos_y2 - pos_y1
            a_1 = (pos_x1 - dx, pos_y1 - dy) # A - d
            a_2 = (pos_x2 + dx, pos_y2 + dy) # B + d
            for a in [a_1, a_2]:
                if a[0] < 0 or a[0] >= len(board) or a[1] < 0 or a[1] >= len(board[0]):
                    continue
                antinodes.add(a)
    return antinodes

def _determineAntinodesTFreq(board, piece):
    antinodes = set()
    pos = getPosPieces(board, piece)
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            pos_x1, pos_y1 = pos[i] # A
            pos_x2, pos_y2 = pos[j] # B
            dx = pos_x2 - pos_x1 # difference vector (dx, dy)
            dy = pos_y2 - pos_y1

            current_a = pos[i]
            antinodes.add(current_a)

            while current_a[0] - dx >= 0 and current_a[0] - dx < len(board) and current_a[1] - dy >= 0 and current_a[1] - dy < len(board[0]):
                current_a = (current_a[0] - dx, current_a[1] - dy)
                antinodes.add(current_a)

            current_a = pos[i]

            while current_a[0] + dx >= 0 and current_a[0] + dx < len(board) and current_a[1] + dy >= 0 and current_a[1] + dy < len(board[0]):
                current_a = (current_a[0] + dx, current_a[1] + dy)
                antinodes.add(current_a)
    return antinodes

def getPosPieces(board, piece):
    pos = []
    for i,row in enumerate(board):
        for j,col in enumerate(board[0]):
            if board[i][j] == piece:
                pos.append((i,j))
    return pos

def main():
    board = []
    with open("day8.txt", "r") as f:
        for l in f:
            board.append(list(l.strip()))
    print(len(determineAntinodes(board))) # Part 1
    print(len(determineAntinodesTFreq(board))) # Part 2

if __name__ == "__main__":
    main()