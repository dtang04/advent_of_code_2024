BOARD_WIDTH = 0
BOARD_HEIGHT = 0

walls = []
boxes = []
dirs = []

walls_p2 = []
boxes_p2 = []

def process_inst(start):
    new_pos = None
    for d in dirs:
        if not new_pos:
            new_pos = update_board(d, start)
        else:
            new_pos = update_board(d, new_pos)
    return new_pos
    
def process_inst_p2(start):
    new_pos = None
    for d in dirs:
        if not new_pos:
            new_pos = update_board_p2(d, start)
        else:
            new_pos = update_board_p2(d, new_pos)
    return new_pos

def update_board(move, cur_pos):
    if move == '^':
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

    elif move == 'v':
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

    elif move == '<':
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

def update_board_p2(move, cur_pos):
    global boxes_p2
    if move == '^':
        cur_x, cur_y = cur_pos
        if cur_y - 1 < 0:
            return cur_pos
        
        if (cur_x, cur_y-1) in walls_p2:
            return cur_pos
        
        box = findBox((cur_x, cur_y-1)) # Find adjacent box going up

        if box is None:
            return (cur_x, cur_y-1)
        
        status, boxes_to_move = checkMove('^', box)

        if not status:
            return (cur_x, cur_y)

        # Create a copy of the board before copying to prevent duplicates
        boxes_p2_cpy = boxes_p2[:]
        for box in boxes_to_move:
            idx = boxes_p2.index(box)
            box_l_x, box_l_y = box[0]
            box_r_x, box_r_y = box[1]
            boxes_p2_cpy[idx] = ((box_l_x, box_l_y-1), (box_r_x, box_r_y-1))

        boxes_p2 = boxes_p2_cpy
        return (cur_x, cur_y - 1)

    elif move == 'v':
        cur_x, cur_y = cur_pos
        if cur_y + 1 >= BOARD_HEIGHT:
            return cur_pos
        
        if (cur_x, cur_y+1) in walls_p2:
            return cur_pos
        
        box = findBox((cur_x, cur_y+1)) # Find adjacent box going down

        if box is None:
            return (cur_x, cur_y+1)
        
        status, boxes_to_move = checkMove('v', box)

        if not status:
            return (cur_x, cur_y)

        boxes_p2_cpy = boxes_p2[:]
        for box in boxes_to_move:
            idx = boxes_p2.index(box)
            box_l_x, box_l_y = box[0]
            box_r_x, box_r_y = box[1]
            boxes_p2_cpy[idx] = ((box_l_x, box_l_y+1), (box_r_x, box_r_y+1))

        boxes_p2 = boxes_p2_cpy
        return (cur_x, cur_y + 1)

    elif move == '<':
        cur_x, cur_y = cur_pos
        if cur_x - 1 < 0:
            return cur_pos
        
        if (cur_x-1, cur_y) in walls_p2:
            return cur_pos
        
        box = findBox((cur_x-1, cur_y)) # Find adjacent box going left

        if box is None:
            return (cur_x-1, cur_y)
        
        status, boxes_to_move = checkMove('<', box)

        if not status:
            return (cur_x, cur_y)

        boxes_p2_cpy = boxes_p2[:]
        for box in boxes_to_move:
            idx = boxes_p2.index(box)
            box_l_x, box_l_y = box[0]
            box_r_x, box_r_y = box[1]
            boxes_p2_cpy[idx] = ((box_l_x-1, box_l_y), (box_r_x-1, box_r_y))
       
        boxes_p2 = boxes_p2_cpy
        return (cur_x - 1, cur_y)

    elif move == '>':
        cur_x, cur_y = cur_pos
        if cur_x + 1 >= BOARD_WIDTH:
            return cur_pos
        
        if (cur_x+1, cur_y) in walls_p2:
            return cur_pos
        
        box = findBox((cur_x+1, cur_y)) # Find adjacent box going right

        if box is None:
            return (cur_x+1, cur_y)
        
        status, boxes_to_move = checkMove('>', box)

        if not status:
            return (cur_x, cur_y)

        boxes_p2_cpy = boxes_p2[:]
        for box in boxes_to_move:
            idx = boxes_p2.index(box)
            box_l_x, box_l_y = box[0]
            box_r_x, box_r_y = box[1]
            boxes_p2_cpy[idx] = ((box_l_x+1, box_l_y), (box_r_x+1, box_r_y))
        
        boxes_p2 = boxes_p2_cpy
        return (cur_x + 1, cur_y)

def findBox(cur_pos):
    for box in boxes_p2:
        l_pos, r_pos = box
        if cur_pos == l_pos or cur_pos == r_pos:
            return box
    return None

def checkMove(move, box, boxes_to_move = None):
    if boxes_to_move is None:
        boxes_to_move = set()

    box_l, box_r = box
    
    box_lx, box_ly = box_l
    box_rx, box_ry = box_r

    if box in boxes_to_move:
        return (True, boxes_to_move)
    
    boxes_to_move.add(box) # Add the current box to boxes_to_move

    if move == "^":
        if (box_lx, box_ly-1) in walls_p2 or (box_rx, box_ry-1) in walls_p2: # one of the box's edges hit a wall
            return (False, None)
        else:
            candidateBox = ((box_lx, box_ly-1), (box_rx, box_ry-1))
            if candidateBox in boxes_p2:
                # there is an aligned box directly on top
                #       []      <- Current Level
                #       []      
                status, boxes_to_move = checkMove(move, candidateBox, boxes_to_move)
                if status:
                    return (True, boxes_to_move)
                return (False, None)
            else:
                # two upper boxes straddle the edges of the current box
                #  1.  [][]  2. []  3.   []     <- Current Level
                #       []       []     []
                leftCandidate = ((box_lx-1, box_ly-1), (box_lx, box_ly-1))
                rightCandidate = ((box_rx, box_ry-1), (box_rx+1, box_ry-1))
                status = True
                # Case 1
                if leftCandidate in boxes_p2 and rightCandidate in boxes_p2:
                    l_status, boxes_to_move_l = checkMove(move, leftCandidate, boxes_to_move) 
                    r_status, boxes_to_move_r = checkMove(move, rightCandidate, boxes_to_move)
                    if l_status and r_status:
                        return (True, boxes_to_move_l.union(boxes_to_move_r))
                    return (False, None)
                # Case 2
                elif leftCandidate in boxes_p2:
                    status, boxes_to_move = checkMove(move, leftCandidate, boxes_to_move)
                # Case 3
                elif rightCandidate in boxes_p2:
                    status, boxes_to_move = checkMove(move, rightCandidate, boxes_to_move)
                else:
                    # Nothing exists in upward direction, can move
                    return (True, boxes_to_move)

                if status:
                    return (status, boxes_to_move)
                else:
                    return (False, None)

    elif move == "v":
        if (box_lx, box_ly+1) in walls_p2 or (box_rx, box_ry+1) in walls_p2: # one of the box's edges hit a wall
            return (False, None)
        else:
            candidateBox = ((box_lx, box_ly+1), (box_rx, box_ry+1))
            if candidateBox in boxes_p2:
                # there is an aligned box directly on bottok
                #       []      <- Current Level
                #       []
                status, boxes_to_move = checkMove(move, candidateBox, boxes_to_move)
                if status:
                    return (True, boxes_to_move)
                return (False, None)
            else:
                # two lower boxes straddle the edges of the current box
                #  1.  [] 2.   []  3.    []         <- Current Level
                #     [][]    []          []
                leftCandidate = ((box_lx-1, box_ly+1), (box_lx, box_ly+1))
                rightCandidate = ((box_rx, box_ry+1), (box_rx+1, box_ry+1))
                status = True
                # Case 1
                if leftCandidate in boxes_p2 and rightCandidate in boxes_p2:
                    l_status, boxes_to_move_l = checkMove(move, leftCandidate, boxes_to_move) 
                    r_status, boxes_to_move_r = checkMove(move, rightCandidate, boxes_to_move)
                    if l_status and r_status:
                        return (True, boxes_to_move_l.union(boxes_to_move_r))
                    return (False, None)
                # Case 2
                elif leftCandidate in boxes_p2:
                    status, boxes_to_move = checkMove(move, leftCandidate, boxes_to_move)
                # Case 3
                elif rightCandidate in boxes_p2:
                    status, boxes_to_move = checkMove(move, rightCandidate, boxes_to_move)
                else:
                    # Nothing exists in upward direction, can move
                    return (True, boxes_to_move)

                if status:
                    return (status, boxes_to_move)
                else:
                    return (False, None)

    elif move == "<":
        candidateBox = ((box_lx-2, box_ly), (box_lx-1, box_ly))
        if (box_lx-1, box_ly) in walls_p2: # left box edge hit a wall
            return (False, None)
        if candidateBox in boxes_p2:
            #   there is a box directly to the left
            #   [][]
            #      ^ Current Level
            status, boxes_to_move = checkMove(move, candidateBox, boxes_to_move)

            if status:
                return (True, boxes_to_move)
            else:
                return (False, None)
        return (True, boxes_to_move)
    
    elif move == ">":
        candidateBox = ((box_rx+1, box_ry), (box_rx+2, box_ry))
        if (box_rx+1, box_ry) in walls_p2: # right box edge hit a wall
            return (False, None)
        if candidateBox in boxes_p2:
            #   there is a box directly to the right
            #     []][]
            #      ^ Current Level
            status, boxes_to_move = checkMove(move, candidateBox, boxes_to_move)

            if status:
                return (True, boxes_to_move)
            else:
                return (False, None)
        return (True, boxes_to_move)

def compute_res():
    res = 0
    for box in boxes:
        box_x, box_y = box
        res += 100 * box_y + box_x
    return res

def compute_res_p2():
    res = 0
    for box in boxes_p2:
        box_l, box_r = box
        box_l_x, box_l_y = box_l
        res += 100 * box_l_y + box_l_x
    return res

def resize(boxes, walls):
    for wall_pos in walls:
        wall_x, wall_y = wall_pos
        walls_p2.append((2*wall_x, wall_y))
        walls_p2.append((2*wall_x+1, wall_y))
    
    for box in boxes:
        box_x, box_y = box
        boxes_p2.append(((2*box_x, box_y), (2*box_x+1, box_y))) # Now each box contains (L_pos, R_pos)

def main():

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

    # Save original state for part 2
    boxes_loc = boxes[:]
    walls_loc = walls[:]

    process_inst(start)
    print(compute_res()) # Part 1: 1414416

    prev_start_x, prev_start_y = start
    start_p2 = (2*prev_start_x, prev_start_y)
    
    resize(boxes_loc, walls_loc)
    BOARD_WIDTH *= 2

    process_inst_p2(start_p2)
    print(compute_res_p2()) # Part 2: 1386070



if __name__ == "__main__":
    main()