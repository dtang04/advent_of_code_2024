from functools import lru_cache

# Globals
patterns = []

@lru_cache(maxsize=None)
def isFeasible(c_pattern):
    out = False

    if len(c_pattern) == 0:
        return True

    for p in patterns:
        if c_pattern[:len(p)] == p:
            out = isFeasible(c_pattern[len(p):])

        if out: # valid combination exists for remaining towels
            return True

    return False

@lru_cache(maxsize=None)
def isFeasibleCount(c_pattern):
    
    if len(c_pattern) == 0:
        return 1
    
    possible = 0

    for p in patterns:
        if c_pattern[:len(p)] == p:
            possible += isFeasibleCount(c_pattern[len(p):])
    
    return possible
            
def main():
    global patterns

    ctr = 0
    is_patterns = True

    all_possible = 0

    with open("day19.txt", 'r') as f:
        patterns = f.readline().strip().split(", ")
        f.readline()
        for l in f:
            pattern = l.strip()
            status = isFeasible(pattern)

            all_possible += isFeasibleCount(pattern)

            if status:
                ctr += 1
    
    print(ctr) # Part 1: 327
    print(all_possible) # Part 2: 772696486795255

if __name__ == "__main__":
    main()