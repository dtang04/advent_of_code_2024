# Globals
l_x = 101
l_y = 103
NUM_SIMULATIONS = l_x * l_y

def simulate_move(robots_st, l_x, l_y):
    """
    Simulate one unit of time. Takes in a dict of lists (pos_x, pos_y) : [(v_x, v_y)]
    and outputs the a new dict of lists where the robots have moved.
    """
    robots_end = {}
    for pos in robots_st:
        for d in robots_st[pos]:
            pos_x, pos_y = pos
            d_x, d_y = d

            # Apply the move
            new_pos = apply_and_wrap(pos_x, pos_y, d_x, d_y, l_x, l_y)

            # Updates end position dict
            if new_pos not in robots_end:
                robots_end[new_pos] = [d]
            else:
                robots_end[new_pos].append(d)
    return robots_end

def apply_and_wrap(pos_x, pos_y, d_x, d_y, l_x, l_y):
    """
    Wrapping logic using modulo
    """
    pos_x = (pos_x + d_x) % l_x
    pos_y = (pos_y + d_y) % l_y
    return (pos_x, pos_y)

def simulate_n(n, robots, l_x, l_y):
    """
    Simulates n moves, returns final positions of robots
    """
    for _ in range(n):
        robots = simulate_move(robots, l_x, l_y)
    return robots

def sum_robots_quad(robots, l_x, l_y):
    """
    Given robots' positions, finds the product of (# of robots beloning in each quadrant)
    """
    mid_x = l_x // 2
    mid_y = l_y // 2

    # Q1
    sum_q1 = 0
    for x in range(mid_x):
        for y in range(mid_y):
            if (x,y) in robots:
                sum_q1 += len(robots[(x,y)]) # Get all robots at the particular position
    
    # Q2
    sum_q2 = 0
    for x in range(mid_x+1, l_x):
        for y in range(mid_y):
            if (x,y) in robots:
                sum_q2 += len(robots[(x,y)])
    
    # Q3
    sum_q3 = 0
    for x in range(mid_x):
        for y in range(mid_y+1, l_y):
            if (x,y) in robots:
                sum_q3 += len(robots[(x,y)])
    
    sum_q4 = 0
    for x in range(mid_x+1, l_x):
        for y in range(mid_y+1, l_y):
            if (x,y) in robots:
                sum_q4 += len(robots[(x,y)])

    return sum_q1 * sum_q2 * sum_q3 * sum_q4

def determine_long_row(robots):
    """
    Tries to find the Christmas tree easter egg by checking whether a given row has
    a large amount of robots
    """
    row_threshold = 10
   
    # Search for a long row > row_threshold
    for y in range(l_y):
        count_cons_row = 0
        for x in range(l_x):
            if (x,y) in robots:
                count_cons_row += 1
            else:
                count_cons_row = 0
            if count_cons_row > row_threshold:
                return True
    return False

def display(robots):
    """
    Displays the robot positions ("#") so that we can verify the easter egg.
    """
    ret = []
    for x in range(l_x):
        loc = []
        for y in range(l_y):
            if (x,y) not in robots:
                loc.append(".")
            else:
                loc.append("#")
        ret.append(loc)

    for j in range(l_y):
        for i in range(l_x):
            print(ret[i][j], end = "")
        print()

def find_egg(robots, l_x, l_y):
    """
    Simulates moves and checks if there is a long row. If true, prints robot positions for
    manual verification.
    """
    for i in range(1,NUM_SIMULATIONS+1):
        robots = simulate_move(robots, l_x, l_y)
        if determine_long_row(robots):
            print("________________")
            display(robots)
            print("Simulation # ", i)
    return robots

def main():
    robots_pos = {}
    with open("day14.txt", "r") as f:
        for l in f:
            # Input Markers
            l = l.strip()
            eq1_pos = l.index("=")
            eq2_pos = l.index("=", eq1_pos+1)
            div = l.index(" ")

            pos_str = l[eq1_pos+1:div]
            v_str = l[eq2_pos+1:len(l)]

            pos = pos_str.split(",")
            pos_t = tuple([int(p) for p in pos])

            v = v_str.split(",")
            v_t = tuple([int(ve) for ve in v])

            if pos_t not in robots_pos:
                robots_pos[pos_t] = [v_t]
            else:
                robots_pos[pos_t].append(v_t)
        
    end_pos = simulate_n(100, robots_pos, l_x, l_y)
    print(sum_robots_quad(end_pos, l_x, l_y)) # Part 1: 219512160
    
    find_egg(robots_pos, l_x, l_y) # Part 2: 6398

if __name__ == "__main__":
    main()