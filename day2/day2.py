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
            bad_idx_1 = i - 1
            bad_idx_2 = i
            break
        dist = abs(current - last)
        if dist < 1 or dist > 3:
            bad_idx_1 = i - 1
            bad_idx_2 = i
            break
        if i == len(row) - 1:
            return (True, -1, -1)
    return (False, bad_idx_1, bad_idx_2)

def main():
    num_safe = 0
    with open("day2.txt", "r") as f:
        for line in f:
            row = line.strip().split(" ")
            status, _, _ = isSafe(row)
            if status:
                num_safe += 1
        print(num_safe) # Part 1: 246

    num_safe_p2 = 0
    with open("day2.txt", "r") as s:
        for line in s:
            row = line.strip().split(" ")
            status, bad_idx_1, bad_idx_2 = isSafe(row)
            if status:
                num_safe_p2 += 1
            else:
                row_1 = row[:]
                del row_1[bad_idx_1] #Try deleting first candidate
                status_1, _, _ = isSafe(row_1)
                if status_1:
                    num_safe_p2 += 1
                    continue
                row_2 = row[:]
                del row_2[bad_idx_2] #Try deleting second candidate
                status_2, _, _ = isSafe(row_2)
                if status_2:
                    num_safe_p2 += 1
        print(num_safe_p2)

if __name__ == "__main__":
    main()