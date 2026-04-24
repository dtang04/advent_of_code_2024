board = []

def getTypes():
    ret = set()
    for row in board:
        ret = ret.union(set(row))
    return ret

def findAll(t):
    ctr = 0
    for row in board:
        for c in row:
            if c == t:
                ctr += 1
    return ctr

def computePrice(t):
    """
    Use BFS to calculate total area and perimeter of node islands.
    """
    tot = 0
    visited = set()
    total_nodes = findAll(t) # Find all nodes of type t
    queue = []
    area = 0
    per = 0
    while len(visited) < total_nodes:
        # Find the next island of same type
        islandFound = False
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                if c == t and (i,j) not in visited: # We found a new unvisited node (new island)
                    queue.append((i,j))
                    visited.add((i,j))
                    islandFound = True
                    break
            if islandFound:
                break

        area_island = 0
        per_island = 0

        # Explore all nodes of the island
        while len(queue) > 0:
            current = queue.pop(0)
        
            cur_x, cur_y = current
            
            # Process the neighbors, calculate perimeter

            if cur_x > 0: # Up
                if board[cur_x-1][cur_y] == t:
                    if (cur_x-1, cur_y) not in visited:
                        queue.append((cur_x-1, cur_y))
                        visited.add((cur_x-1, cur_y))
                else:
                    per_island += 1 # A side to the island has been found
            else:
                per_island += 1 # Touching the edge of the board

            if cur_x < len(board) - 1: #Down
                if board[cur_x+1][cur_y] == t:
                    if (cur_x+1, cur_y) not in visited:
                        queue.append((cur_x+1, cur_y))
                        visited.add((cur_x+1, cur_y))
                else:
                    per_island += 1
            else:
                per_island += 1
            
            if cur_y > 0: # Left
                if board[cur_x][cur_y-1] == t:
                    if (cur_x, cur_y-1) not in visited:
                        queue.append((cur_x, cur_y-1))
                        visited.add((cur_x, cur_y-1))
                else:
                    per_island += 1
            else:
                per_island += 1

            if cur_y < len(board[cur_x]) - 1: # Right
                if board[cur_x][cur_y+1] == t:
                    if (cur_x, cur_y+1) not in visited:
                        queue.append((cur_x, cur_y+1))
                        visited.add((cur_x, cur_y+1))
                else:
                    per_island += 1
            else:
                per_island += 1
                
            area_island += 1
        tot += area_island * per_island
    return tot

                

def main():
    with open("day12.txt") as f:
        for l in f:
            board.append(list(l.strip()))
    types = getTypes()
    tot = 0
    for t in types:
        tot += computePrice(t)
    print(tot)

if __name__ == "__main__":
    main()