BOARD_WIDTH = 0
BOARD_HEIGHT = 0
walls = []
boxes = []
dirs = []

def process_inst(start):
    new_pos = None
    for d in dirs:
        if not new_pos:
            new_pos = update_board(d, start)
        else:
            new_pos = update_board(d, new_pos)
    return new_pos

def update_board(move, cur_pos):
    if move == "^":
        cur_x, cur_y = cur_pos   
        if cur_y - 1 < 0:
            return cur_pos

        if (cur_x, cur_y-1) in walls:
            return cur_pos

        if (cur_x, cur_y-1) in boxes:
            loc_x, loc_y = cur_x, cur_y - 1

            while (loc_x, loc_y-1) in boxes: # loc_y stores the last position of the box chain
                loc_y -= 1
            
            if (loc_x, loc_y-1) in walls: # Box chain hit a wall, can't move
                return cur_pos
            else: # End of the box chain is empty space
                while loc_y <= cur_y - 1:
                    boxes[boxes.index((loc_x, loc_y))] = (loc_x, loc_y-1)
                    loc_y += 1
        return (cur_x, cur_y-1)

    elif move == "v":
        cur_x, cur_y = cur_pos   
        if cur_y + 1 >= BOARD_HEIGHT:
            return cur_pos

        if (cur_x, cur_y+1) in walls:
            return cur_pos

        if (cur_x, cur_y+1) in boxes:
            loc_x, loc_y = cur_x, cur_y + 1

            while (loc_x, loc_y+1) in boxes:
                loc_y += 1
            
            if (loc_x, loc_y+1) in walls:
                return cur_pos
            else:
                while loc_y >= cur_y + 1:
                    boxes[boxes.index((loc_x, loc_y))] = (loc_x, loc_y+1)
                    loc_y -= 1
        return (cur_x, cur_y+1)

    elif move == "<":
        cur_x, cur_y = cur_pos   
        if cur_x - 1 < 0:
            return cur_pos

        if (cur_x-1, cur_y) in walls:
            return cur_pos

        if (cur_x-1, cur_y) in boxes:
            loc_x, loc_y = cur_x - 1, cur_y

            while (loc_x-1, loc_y) in boxes:
                loc_x -= 1
            
            if (loc_x-1, loc_y) in walls:
                return cur_pos
            else:
                while loc_x <= cur_x - 1:
                    boxes[boxes.index((loc_x, loc_y))] = (loc_x-1, loc_y)
                    loc_x += 1
        return (cur_x-1, cur_y)

    else:
        cur_x, cur_y = cur_pos   
        if cur_x + 1 >= BOARD_WIDTH:
            return cur_pos

        if (cur_x + 1, cur_y) in walls:
            return cur_pos

        if (cur_x + 1, cur_y) in boxes:
            loc_x, loc_y = cur_x + 1, cur_y

            while (loc_x+1, loc_y) in boxes: 
                loc_x += 1
            
            if (loc_x+1, loc_y) in walls:
                return cur_pos
            else:
                while loc_x >= cur_x + 1:
                    boxes[boxes.index((loc_x, loc_y))] = (loc_x+1, loc_y)
                    loc_x -= 1
        return (cur_x+1, cur_y)

def compute_res():
    res = 0
    for box in boxes:
        box_x, box_y = box
        res += 100 * box_y + box_x
    return res

def main():
    """
    Parses the input, inserting into board[][] and dirs
    """

    global dirs
    global BOARD_WIDTH
    global BOARD_HEIGHT

    dirsStart = False
    j = 0
    start = None
    with open("day15.txt", "r") as f:
        for l in f:
            if l == "\n":
                dirsStart = True
                continue
            if not dirsStart:
                l = l.strip()
                row = list(l)
                for i, s in enumerate(l):
                    if s == '#':
                        walls.append((i,j))
                    if s == 'O':
                        boxes.append((i,j))
                    if s == '@':
                        start = (i,j)

                if j == 0:
                    BOARD_WIDTH = len(row)

                j += 1
            else:
                l = l.strip()
                dirs += list(l)

        BOARD_HEIGHT = j

    process_inst(start)
    print(compute_res())

if __name__ == "__main__":
    main()