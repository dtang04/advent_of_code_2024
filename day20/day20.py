# Globals
START = None
END = None

BOARD_LENGTH = 0
BOARD_WIDTH = 0

walls = []
cheats = []

def trace():
    """
    Trace the default path.
    """
    cur = START
    visited = {START}
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

def traverse():
    """
    Solve the race, with cheats.
    """
    queue = [(START, 0, 2, False, False, {START})] # cur_pos, time_elapsed, cheat_active_duration, cheat_activated, cheat_used, trail
                                   # we separate cheat_active_duration and cheat-used
                                   # cheat of 2 picoseconds means A -> W -> B is allowed

    while len(queue) != 0:
        current = queue.pop()

        cur_pos, time_elapsed, cheat_active_duration, cheat_activated, cheat_used, trail = current

        print(cur_pos, cheat_activated)

        if cur_pos == END:
            cheats.append(time_elapsed)
            continue

        if cur_pos in walls and cheat_active_duration <= 0 and cheat_activated: # no cheat duration left, cheat previously activated, and we're in a wall
            continue
        elif cheat_active_duration <= 0 and cheat_activated: # mark the cheat as used when we go back on valid ground
            cheat_used = True
            cheat_activated = False

        cur_x, cur_y = cur_pos

        candidate = (cur_x, cur_y-1)
        if candidate not in walls or not cheat_used:
            if cur_y-1 >= 0 and candidate not in trail:
                loc_trail = trail.copy()
                loc_trail.add(candidate)

                if candidate in walls or cheat_activated: # cheat_activated = True can be set if the next move is a wall, or activated in a previous cycle
                    queue.append((candidate, time_elapsed+1, cheat_active_duration-1, True, cheat_used, loc_trail))
                else:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration, cheat_activated, cheat_used, loc_trail))
        
        candidate = (cur_x, cur_y+1)
        if candidate not in walls or not cheat_used:
            if cur_y+1 < BOARD_LENGTH and candidate not in trail:
                loc_trail = trail.copy()
                loc_trail.add(candidate)

                if candidate in walls or cheat_activated:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration-1, True, cheat_used, loc_trail))
                else:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration, cheat_activated, cheat_used, loc_trail))
        
        candidate = (cur_x-1, cur_y)
        if candidate not in walls or not cheat_used:
            if cur_x-1 >= 0 and candidate not in trail:
                loc_trail = trail.copy()
                loc_trail.add(candidate)
            
                if candidate in walls or cheat_activated:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration-1, True, cheat_used, loc_trail))
                else:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration, cheat_activated, cheat_used, loc_trail))

        candidate = (cur_x+1, cur_y)
        if candidate not in walls or not cheat_used:
            if cur_x+1 < BOARD_WIDTH and candidate not in trail:
                loc_trail = trail.copy()
                loc_trail.add(candidate)

                if candidate in walls or cheat_activated:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration-1, True, cheat_used, loc_trail))
                else:
                    queue.append((candidate, time_elapsed+1, cheat_active_duration, cheat_activated, cheat_used, loc_trail))

def part1():
    ctr = 0
    traverse()
    d_time = trace()

    for ch_time in cheats:
        if d_time - ch_time >= 100:
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

    print(part1())


if __name__ == "__main__":
    main()