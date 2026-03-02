def main():
    dists = []
    with open("day1.txt", "r") as f:
        left_lst = []
        right_lst = []
        for line in f:
            lst = line.strip().split(" ")
            left_lst.append(lst[0])
            right_lst.append(lst[-1])
        left_lst.sort()
        right_lst.sort()
        for i, r_e in enumerate(right_lst):
            r_e = int(r_e)
            l_e = int(left_lst[i])
            dists.append(abs(r_e - l_e))
        print(sum(dists)) #Part 1: 1222801

if __name__ == "__main__":
    main()