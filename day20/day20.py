# Globals
walls = []
START = None
END = None

BOARD_LENGTH = 0
BOARD_WIDTH = 0

def trace():
    """
    Trace the default path.
    """
    visited = set()
    cur = START
    time_elapsed = 0
    while cur != END:

        cur_x, cur_y = cur

        candidate = (cur_x, cur_y-1)
        if cur_y-1 >= 0 and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate # There's only one path, so greedily take the next unvisited path
            time_elapsed += 1
            continue
        
        candidate = (cur_x, cur_y+1)
        if cur_y+1 < BOARD_LENGTH and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate
            time_elapsed += 1
            continue

        candidate = (cur_x-1, cur_y)
        if cur_x-1 >= 0 and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate
            time_elapsed += 1
            continue
        
        candidate = (cur_x+1, cur_y)
        if cur_x+1 < BOARD_WIDTH and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate
            time_elapsed += 1
            continue
    
    return time_elapsed

        
def main():
    global START, END, BOARD_LENGTH, BOARD_WIDTH

    width_set = False

    with open("day20.txt", 'r') as f:
        for y,l in enumerate(f):
            row = list(l.strip())
            for x, token in enumerate(row): # top left is (0,0)
                if row[x] == '#':
                    walls.append((x, y))
                elif row[x] == 'S':
                    START = (x,y)
                elif row[x] == 'E':
                    END = (x,y)
                
                if not(width_set):
                    BOARD_WIDTH = len(row)
                    width_set = True

            BOARD_LENGTH += 1

    print(trace())


if __name__ == "__main__":
    main()