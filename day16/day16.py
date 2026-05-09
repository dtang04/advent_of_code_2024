import heapq

walls = []

# Part 2 globals
min_score = None
min_score_trails = []
epoch = 0

def bfs(start, end):
    """
    Part 1

    A working but inefficient solutiokn to part 1. Appends to the queue in an arbitrary order, meaning
    that expensive paths can be processed before cheaper paths, wasting compute.

    Must explore all possible paths that end at 'E' without early returning.
    """
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
             
def bfs_heapq(start, end):
    """
    Part 1

    An optimization to the above bfs function, using priority queue (via min-heap)
    rather than just appending naively to the queue.

    Since the first element of the min queue is guaranteed to be the current path with the lowest score,
    heapq ensures orderly processing of paths from lowest score to highest, rather than wasting compute on
    processing paths with high scores.

    Because heapq maintains a global ordering by score, we can also early return the moment when pos == end (here
    we are assuming non-negative score increments, which is the case).
    """
    pq = [start] # Tuples of (cur_score, (row, col), current_direction) since heapq sorts by first tuple element
                 # pq is a min heap

    visited = {}
    while len(pq) > 0:
        score, pos, d = heapq.heappop(pq)

        if pos == end: # the min element in the heap has bubbled up to the front, and its at the end 'E'
            return score

        if (pos, d) in visited: # min-heap guarantees that the first element is the path with the lowest score
            continue
        
        visited[(pos, d)] = score
        pos_x, pos_y = pos

        if d == 'U':
            if (pos_x-1, pos_y) not in walls:
               heapq.heappush(pq, (score+1, (pos_x-1, pos_y), 'U'))
            
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'R'))
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'L'))
        
        elif d == 'D':
            if (pos_x+1, pos_y) not in walls:
                heapq.heappush(pq, (score+1, (pos_x+1, pos_y), 'D'))
                
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'R'))
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'L'))
    
        elif d == 'L':
            if (pos_x, pos_y-1) not in walls:
                heapq.heappush(pq, (score+1, (pos_x, pos_y-1), 'L'))

            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'U'))
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'D'))
        
        else:
            if (pos_x, pos_y+1) not in walls:
                heapq.heappush(pq, (score+1, (pos_x, pos_y+1), 'R'))
            
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'U'))
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'D'))

    return -1

def find_best_paths(start, end):
    """
    Part 2
    
    For each heapq push, append the next destination of the path onto the trail set.

    Then, for all paths that reach pos == end with the same min_score, add it to the candidate trails list.

    Lastly, aggregate elements with union.
    """
    global min_score
    global epoch

    pq = [start] 

    visited = {}
    while len(pq) > 0:
        score, pos, d, _, trail = heapq.heappop(pq) # monotonically increasing epoch is to prevent the corner case where score, pos, d are the same
                                                        # and heapq tries to compare trail, which returns TypeError

        if min_score is not None and score > min_score:
            continue

        if pos == end and min_score is None: # the first shortest path, may be more shortest paths
            min_score = score
            min_score_trails.append(trail)
            continue
        elif pos == end and min_score == score:
            min_score_trails.append(trail)
            continue

        if (pos, d) in visited and score > visited[(pos, d)]:
            continue
        
        visited[(pos, d)] = score
        pos_x, pos_y = pos

        if d == 'U':
            if (pos_x-1, pos_y) not in walls:
                _trail = trail | {(pos_x-1, pos_y)} # need to create a new copy to pass into func args
                epoch += 1
                heapq.heappush(pq, (score+1, (pos_x-1, pos_y), 'U', epoch, _trail))
            
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'R', epoch, trail))
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'L', epoch, trail))
        
        elif d == 'D':
            if (pos_x+1, pos_y) not in walls:
                _trail = trail | {(pos_x+1, pos_y)}
                epoch += 1
                heapq.heappush(pq, (score+1, (pos_x+1, pos_y), 'D', epoch, _trail))
                
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'R', epoch, trail))
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'L', epoch, trail))
    
        elif d == 'L':
            if (pos_x, pos_y-1) not in walls:
                _trail = trail | {(pos_x, pos_y-1)}
                epoch += 1
                heapq.heappush(pq, (score+1, (pos_x, pos_y-1), 'L', epoch, _trail))

            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'U', epoch, trail))
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'D', epoch, trail))
        
        else:
            if (pos_x, pos_y+1) not in walls:
                _trail = trail | {(pos_x, pos_y+1)}
                epoch += 1
                heapq.heappush(pq, (score+1, (pos_x, pos_y+1), 'R', epoch, _trail))
            
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'U', epoch, trail))
            trail = trail.copy()
            epoch += 1
            heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'D', epoch, trail))

    final_nodes = set()
    for trail_path in min_score_trails:
        final_nodes = final_nodes.union(trail_path)
    
    return len(final_nodes)

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
                    start = ((row, col), 'R', 0)
                    start_pq = (0, (row, col), 'R')
                    start_p2 = (0, (row, col), 'R', epoch, {(row, col)})
                if t == 'E':
                    end = (row, col)
            row += 1

    print(bfs_heapq(start_pq, end)) # Part 1: 98416
    print(find_best_paths(start_p2, end)) # Part 2: 471

if __name__ == "__main__":
    main()