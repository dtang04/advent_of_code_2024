def main():
    num_safe = 0
    with open("day2.txt", "r") as f:
        for line in f:
            row = line.strip().split(" ")
            isDecr = False
            isIncr = False
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
                    num_safe += 1
                
        #print(num_safe) # Part 1: 246

    # Part 2
    num_safe_p2 = 0
    with open("day2.txt", "r") as s:
        for line in s:
            row = line.strip().split(" ")
            isDecr = False
            isIncr = False
            i = 0
            idx_to_delete = -1
            found = False
            while i in range(len(row)-1):
                current_num = int(row[i])
                next_num = int(row[i+1])
                if i == 0 and current_num > next_num:
                    dist = abs(current_num - next_num)
                    if (dist < 1 or dist > 3):
                        if idx_to_delete == -1:
                            idx_to_delete = i
                            found = True
                        else:
                            break
                    isDecr = True
                elif i == 0:
                    dist = abs(current_num - next_num)
                    if (dist < 1 or dist > 3):
                        if idx_to_delete == -1:
                            idx_to_delete = i
                            found = True
                        else:
                            break
                    isIncr = True
                elif ((isIncr and current_num > next_num) or (isDecr and current_num < next_num)
                    or (abs(current_num - next_num) < 1 or abs(current_num - next_num) > 3)):
                    if idx_to_delete == -1:
                        idx_to_delete = i
                        found = True
                    else:
                        break
                if idx_to_delete != -1 and idx_to_delete == i and found:
                    found = False
                    del row[i]
                    i -= 1
                    continue
                if i == len(row) - 2:
                    print(row)
                    num_safe_p2 += 1
                i += 1
        print(num_safe_p2)

if __name__ == "__main__":
    main()