def isSafe(row):
    isDecr = False
    isIncr = False
    bad_idx_1 = 0
    bad_idx_2 = 0
    for i in range(1, len(row)):
        current = int(row[i])
        last = int(row[i-1])
        if i == 1 and current > last:
            isIncr = True
        elif i == 1:
            isDecr = True
        elif (isIncr and current < last) or (isDecr and current > last):
            break
        dist = abs(current - last)
        if dist < 1 or dist > 3:
            break
        if i == len(row) - 1:
            return True
    return False

def main():
    num_safe = 0
    with open("day2.txt", "r") as f:
        for line in f:
            row = line.strip().split(" ")
            status = isSafe(row)
            if status:
                num_safe += 1
        print(num_safe) # Part 1: 246

    num_safe_p2 = 0
    with open("day2.txt", "r") as s:
        for line in s:
            row = line.strip().split(" ")
            status = isSafe(row)
            if status:
                num_safe_p2 += 1
            else:
                for i,_ in enumerate(row):
                    row_c = row[:]
                    del row_c[i]
                    if isSafe(row_c):
                        num_safe_p2 += 1
                        break
        print(num_safe_p2) #Part 2: 318

if __name__ == "__main__":
    main()