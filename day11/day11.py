from functools import lru_cache

def blink(seq):
    """
    Simulate each the list state after each blink
    """
    ret = []
    for st in seq:
        if st == "0":
            ret.append("1")
        elif len(st) % 2 == 0:
            loc = [str(int(st[0:len(st)//2])), str(int(st[len(st)//2:]))] # cast to int and back to str to get rid of leading 0s
            ret += loc
        else:
            ret.append(str(int(st) * 2024))
    return ret

def blink25(seq):
    for i in range(25):
        seq = blink(seq)
    return seq

@lru_cache(maxsize=None)
def blink_p2(num, blinks):
    """
    Use memoization and calculate the number the number of stones with k blinks remaining.
    """
    num_stones = 0
    if blinks == 0:
        return 1
    if num == "0":
        num_stones += blink_p2("1", blinks - 1)
    elif len(num) % 2 == 0:
        num_stones += blink_p2(str(int(num[0:len(num)//2])), blinks - 1)
        num_stones += blink_p2(str(int(num[len(num)//2:])), blinks - 1)
    else:
        num_stones += blink_p2(str(int(num) * 2024), blinks - 1)
    return num_stones
    
def blink75(seq):
    tot = 0
    for st in seq:
        tot += blink_p2(st, 75)
    return tot

def main():
    with open("day11.txt") as f:
        seq = f.readline().strip().split(" ")
    print(len(blink25(seq))) # Day 1: 188902
    print(blink75(seq)) # Day 2: 223894720281135

if __name__ == "__main__":
    main()