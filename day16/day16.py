walls = []

def bfs(start, end):
    queue = [start] # Tuples of ((row, col), cur_direction, cur_score)

    visited = {} # of type (pos, d)

    while len(queue) > 0:
        pos, d, score = queue.pop(0)
        if (pos, d) in visited and score > visited[(pos, d)]: # if we revisit a position with a higher score, continue
            continue
        
        visited[(pos, d)] = score # note that we can update a previous position with a lowered score
        pos_x, pos_y = pos

        if d == 'U':
            if (pos_x-1, pos_y) not in walls:
                queue.append(((pos_x-1, pos_y), 'U', score+1))
            
            queue.append(((pos_x, pos_y), 'R', score+1000))
            queue.append(((pos_x, pos_y), 'L', score+1000))
        
        elif d == 'D':
            if (pos_x+1, pos_y) not in walls:
                queue.append(((pos_x+1, pos_y), 'D', score+1))
                
            queue.append(((pos_x, pos_y), 'R', score+1000))
            queue.append(((pos_x, pos_y), 'L', score+1000))
    
        elif d == 'L':
            if (pos_x, pos_y-1) not in walls:
                queue.append(((pos_x, pos_y-1), 'L', score+1))

            queue.append(((pos_x, pos_y), 'U', score+1000))
            queue.append(((pos_x, pos_y), 'D', score+1000))
        
        else:
            if (pos_x, pos_y+1) not in walls:
                queue.append(((pos_x, pos_y+1), 'R', score+1))
            
            queue.append(((pos_x, pos_y), 'U', score+1000))
            queue.append(((pos_x, pos_y), 'D', score+1000))
    
    candidates = []
    for k, score in visited.items():
        if k[0] == end:
            candidates.append(score)
    return min(candidates)
             
def main():
    row = 0
    start = None
    end = None
    with open("day16.txt", "r") as f:
        for l in f:
            tokens = list(l)
            for col,t in enumerate(tokens):
                if t == '#':
                    walls.append((row,col))
                if t == 'S':
                    start = ((row, col), 'E', 0)
                if t == 'E':
                    end = (row, col)
            row += 1
    print(bfs(start, end)) # Part 1: 98416

if __name__ == "__main__":
    main()