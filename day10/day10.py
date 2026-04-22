h_map = []

trailhead_ends = {} # Map of trailhead start: ends

def findStarts():
    pos = []
    for i,row in enumerate(h_map):
        for j,e in enumerate(row):
            if e == 0:
                pos.append((i, j, (i,j), 0))
    return pos

def ascendBF():
    ctr = 0
    queue = findStarts()
    while len(queue) > 0:
        pos_x, pos_y, start, level = queue.pop(0)
        if level == 9:
            if start not in trailhead_ends: #New start location, add to dict
                ctr += 1
                trailhead_ends[start] = [(pos_x, pos_y)]
            elif (pos_x, pos_y) not in trailhead_ends[start]: # Start location exists, but end position is unique tracked
                ctr += 1
                trailhead_ends[start].append((pos_x, pos_y))
            continue
        if pos_y - 1 >= 0 and h_map[pos_x][pos_y-1] == level + 1: # Left
            queue.append((pos_x, pos_y-1, start, level+1))
        if pos_y + 1 < len(h_map[pos_x]) and h_map[pos_x][pos_y+1] == level + 1: # Right
            queue.append((pos_x, pos_y+1, start, level+1))
        if pos_x - 1 >= 0 and h_map[pos_x-1][pos_y] == level + 1: # Up
            queue.append((pos_x-1, pos_y, start, level+1))
        if pos_x + 1 < len(h_map) and h_map[pos_x+1][pos_y] == level + 1:
            queue.append((pos_x+1, pos_y, start, level+1))
    return ctr

def ascendBFRating():
    ctr = 0
    queue = findStarts()
    while len(queue) > 0:
        pos_x, pos_y, start, level = queue.pop(0)
        if level == 9:
            ctr += 1
            continue
        if pos_y - 1 >= 0 and h_map[pos_x][pos_y-1] == level + 1: # Left
            queue.append((pos_x, pos_y-1, start, level+1))
        if pos_y + 1 < len(h_map[pos_x]) and h_map[pos_x][pos_y+1] == level + 1: # Right
            queue.append((pos_x, pos_y+1, start, level+1))
        if pos_x - 1 >= 0 and h_map[pos_x-1][pos_y] == level + 1: # Up
            queue.append((pos_x-1, pos_y, start, level+1))
        if pos_x + 1 < len(h_map) and h_map[pos_x+1][pos_y] == level + 1:
            queue.append((pos_x+1, pos_y, start, level+1))
    return ctr
                
def main():
    with open("day10.txt", "r") as f:
        for l in f:
            row = list(l.strip())
            row_int = []
            for s in row:
                row_int.append(int(s))
            h_map.append(row_int)
    print(ascendBF()) # Part 1: 652
    print(ascendBFRating()) #Part 2: 1432


if __name__ == "__main__":
    main()