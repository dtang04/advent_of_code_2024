
# Globals
GRID_WIDTH = 71
GRID_LENGTH = 71
NUM_SIM = 1024

grid = []


def populateGrid():
    for _ in range(GRID_WIDTH):
        row = ['.'] * GRID_LENGTH
        grid.append(row)
    return grid

def bfs():
    """
    Maintain a queue of ((pos_x, pos_y), trail)
    """
    queue = [(0,0,[])]
    visited = {(0,0)}

    while len(queue) != 0:
        current = queue.pop(0)
        cur_x, cur_y, trail = current

        if cur_x == GRID_LENGTH-1 and cur_y == GRID_WIDTH-1:
            return current

        # Process neighbors
        if cur_y > 0: # Left
            left_n = (cur_x, cur_y-1)
            if left_n not in visited and grid[cur_x][cur_y-1] != '#':
                visited.add(left_n)

                trail_loc = trail[:]
                trail_loc.append(left_n)

                queue.append((cur_x, cur_y-1, trail_loc))

        if cur_y < GRID_WIDTH-1: # Right
            right_n = (cur_x, cur_y+1)
            if right_n not in visited and grid[cur_x][cur_y+1] != '#':
                visited.add(right_n)

                trail_loc = trail[:]
                trail_loc.append(right_n)

                queue.append((cur_x, cur_y+1, trail_loc))
        
        if cur_x > 0: # Up
            up_n = (cur_x-1, cur_y)
            if up_n not in visited and grid[cur_x-1][cur_y] != '#':
                visited.add(up_n)

                trail_loc = trail[:]
                trail_loc.append(up_n)

                queue.append((cur_x-1, cur_y, trail_loc))
        
        if cur_x < GRID_LENGTH-1: # Down
            d_n = (cur_x+1, cur_y)
            if d_n not in visited and grid[cur_x+1][cur_y] != '#':
                visited.add(d_n)

                trail_loc = trail[:]
                trail_loc.append(d_n)

                queue.append((cur_x+1, cur_y, trail_loc))

def main():
    global grid
    populateGrid()
    fallen = 0
    with open("day18.txt", 'r') as f:
        for l in f:
            if fallen >= NUM_SIM:
                break
            l = l.strip().split(',')
            x = int(l[1])
            y = int(l[0])
            grid[x][y] = '#'
            fallen += 1

    pos_x, pos_y, trail = bfs()
    drawTrail(trail)
    displayGrid()
    print(len(trail))

def drawTrail(trail):
    for x,y in trail:
        grid[x][y] = 'O'

    grid[0][0] = 'O'

def displayGrid():
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[i]):
            print(grid[i][j], end = "")
        print()

if __name__ == "__main__":
    main()