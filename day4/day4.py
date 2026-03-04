def findXs(board):
    X_pos = []
    for i,row in enumerate(board):
        for j,c in enumerate(row):
            if c == "X":
                X_pos.append((i,j))
    return X_pos

def main():
    board = []
    with open("day4.txt", "r") as f:
        for line in f:
            board.append(list(line.strip()))
        print(board)
        print(findXs(board))

if __name__ == "__main__":
    main()