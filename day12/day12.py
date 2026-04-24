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

def computePrice_Perimeter(t):
    """
    Use BFS to calculate total price of node islands, given a type, by summing area * perimeter of each island.
    """
    tot = 0
    visited = set()
    total_nodes = findAll(t) # Find all nodes of type t
    queue = []
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

def computePrice_Sides(t):
    """
    Use BFS to calculate total price of node islands, given a type, by summing area * sides of each island.
    """
    tot = 0
    visited = set()
    total_nodes = findAll(t) # Find all nodes of type t
    queue = []
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
        outward_dirs = []

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
                    outward_dirs.append((cur_x, cur_y, "U")) # Store which direction we found the exposed edge at
            else:
                outward_dirs.append((cur_x, cur_y, "U"))

            if cur_x < len(board) - 1: #Down
                if board[cur_x+1][cur_y] == t:
                    if (cur_x+1, cur_y) not in visited:
                        queue.append((cur_x+1, cur_y))
                        visited.add((cur_x+1, cur_y))
                else:
                    outward_dirs.append((cur_x, cur_y, "D"))
            else:
                outward_dirs.append((cur_x, cur_y, "D"))
            
            if cur_y > 0: # Left
                if board[cur_x][cur_y-1] == t:
                    if (cur_x, cur_y-1) not in visited:
                        queue.append((cur_x, cur_y-1))
                        visited.add((cur_x, cur_y-1))
                else:
                    outward_dirs.append((cur_x, cur_y, "L"))
            else:
                outward_dirs.append((cur_x, cur_y, "L"))

            if cur_y < len(board[cur_x]) - 1: # Right
                if board[cur_x][cur_y+1] == t:
                    if (cur_x, cur_y+1) not in visited:
                        queue.append((cur_x, cur_y+1))
                        visited.add((cur_x, cur_y+1))
                else:
                    outward_dirs.append((cur_x, cur_y, "R"))
            else:
                outward_dirs.append((cur_x, cur_y, "R"))
                
            area_island += 1

        edges_island = consolidateEdges(outward_dirs)
        tot += area_island * edges_island
    return tot

def consolidateEdges(arr):
    """
    Given arr = [(pos_x, pos_y, orientation)], counts the edges.
    """
    num_edges = 0
    while len(arr) > 0:
        t = arr.pop(0)
        cur_x, cur_y, d = t
        if d == "U" or d == "D": 
            # If direction is up or down, walk left and walk right, deleting any tuples that share the same orientation
            walk_l = cur_y-1
            walk_r = cur_y+1
            while (cur_x, walk_l, d) in arr:
                arr.pop(arr.index((cur_x, walk_l, d)))
                walk_l -= 1
            while (cur_x, walk_r, d) in arr:
                arr.pop(arr.index((cur_x, walk_r, d)))
                walk_r += 1
            num_edges += 1
        elif d == "L" or d == "R":
            # If direction is left or right, walk up and walk down, deleting any tuples that share the same orientation
            walk_u = cur_x-1
            walk_d = cur_x+1
            while (walk_u, cur_y, d) in arr:
                arr.pop(arr.index((walk_u, cur_y, d)))
                walk_u -= 1
            while (walk_d, cur_y, d) in arr:
                arr.pop(arr.index((walk_d, cur_y, d)))
                walk_d += 1
            num_edges += 1
    return num_edges

def main():
    with open("day12.txt") as f:
        for l in f:
            board.append(list(l.strip()))
    types = getTypes()
    tot_1 = 0
    for t in types:
        tot_1 += computePrice_Perimeter(t)
    print(tot_1) # Part 1: 1344578

    tot_2 = 0
    for t in types:
        tot_2 += computePrice_Sides(t)
    print(tot_2) # Part 2: 814302

if __name__ == "__main__":
    main()