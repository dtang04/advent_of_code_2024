def blink(seq):
    ret = []
    for i,st in enumerate(seq):
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
        
def main():
    with open("day11.txt") as f:
        seq = f.readline().strip().split(" ")
    print(len(blink25(seq)))

if __name__ == "__main__":
    main()