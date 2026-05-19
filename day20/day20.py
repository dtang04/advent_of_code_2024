# Globals
START = None
END = None

BOARD_LENGTH = 0
BOARD_WIDTH = 0

walls = []
cheats = {}

path = {}

def trace_with_time():
    """
    Trace the default path, keeping a timestamp of the time.
    """
    cur = START
    visited = {START}
    time_elapsed = 0

    path[START] = 0

    while cur != END:

        cur_x, cur_y = cur

        candidate = (cur_x, cur_y-1)
        if cur_y-1 >= 0 and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate # There's only one path, so greedily take the next unvisited path
            time_elapsed += 1
            path[candidate] = time_elapsed
            continue
        
        candidate = (cur_x, cur_y+1)
        if cur_y+1 < BOARD_LENGTH and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate
            time_elapsed += 1
            path[candidate] = time_elapsed
            continue

        candidate = (cur_x-1, cur_y)
        if cur_x-1 >= 0 and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate
            time_elapsed += 1
            path[candidate] = time_elapsed
            continue
        
        candidate = (cur_x+1, cur_y)
        if cur_x+1 < BOARD_WIDTH and candidate not in visited and candidate not in walls:
            visited.add(candidate)
            cur = candidate
            time_elapsed += 1
            path[candidate] = time_elapsed
            continue

def findCheats():
    for p,elapsed in path.items():
        cur_x, cur_y = p
        candidates = [(cur_x, cur_y-2), (cur_x, cur_y+2), (cur_x-2, cur_y), (cur_x+2, cur_y)]
        for c in candidates:
            if c in path:
                time_saved = path[c] - (elapsed + 2)
                cheats[(p, c)] = time_saved

def filterCheats():
    ctr = 0
    for cheat, time_saved in cheats.items():
        if time_saved >= 100:
            ctr += 1
    return ctr
    
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

    trace_with_time()
    findCheats()
    print(filterCheats()) # Part 1: 1355

if __name__ == "__main__":
    main()