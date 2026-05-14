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
            
def main():
    global patterns

    ctr = 0
    is_patterns = True

    with open("day19.txt", 'r') as f:
        patterns = f.readline().strip().split(", ")
        f.readline()
        for l in f:
            pattern = l.strip()
            status = isFeasible(pattern)
    
            if status:
                ctr += 1
    
    print(ctr) # Part 1: 327

if __name__ == "__main__":
    main()