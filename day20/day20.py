# Globals
START = None
END = None

BOARD_LENGTH = 0
BOARD_WIDTH = 0
TIME_DUR = 20

walls = []

cheats = {}
cheats_p2 = {}

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

def findCheats_20ps():
    for p1,elapsed_1 in path.items():
        for p2,elapsed_2 in path.items():
            if p1 == p2:
                continue
            p1_x, p1_y = p1
            p2_x, p2_y = p2
            m_dist = abs(p1_x - p2_x) + abs(p1_y - p2_y) # calculate the manhattan distance
            if m_dist <= 20:
                time_saved = path[p2] - (elapsed_1 + m_dist)
                cheats_p2[(p1, p2)] = time_saved
            
def filterCheats():
    ctr = 0
    for cheat, time_saved in cheats.items():
        if time_saved >= 100:
            ctr += 1
    return ctr

def filterCheats_p2():
    ctr = 0
    for cheat, time_saved in cheats_p2.items():
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
    findCheats_20ps()
    print(filterCheats_p2()) # Part 2: 1007335



if __name__ == "__main__":
    main()