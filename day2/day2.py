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
                
        print(num_safe) # Part 1: 246

if __name__ == "__main__":
    main()