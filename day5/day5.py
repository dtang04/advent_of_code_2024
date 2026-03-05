def checkUpdates(updates, left, right):
    for i in range(len(updates)):
        if i >= len(updates) - 1:
            return True
        for j in range(i+1, len(updates)):
            (c1, c2) = findUpdateLog(updates[i], updates[j], left, right)
            if updates[i] == c1 and updates[j] == c2: #Match
                continue
            elif updates[i] == c2 and updates[j] == c1: #Flipped, invalid ordering
                return False
            # continue if (-1, -1)
            

def findUpdateLog(e_1, e_2, left, right):
    for i,l in enumerate(left):
        if (l == e_1 and right[i] == e_2):
            return (e_1, e_2)
        if (l == e_2 and right[i] == e_1):
            return (e_2, e_1)
    return (-1,-1)

def main():
    part1 = 0
    left = []
    right = []
    updates = []
    with open("day5.txt", "r") as f:
        for entry in f:
            if entry == "\n":
                break
            entry = entry.strip().split("|")
            left.append(entry[0])
            right.append(entry[1])
        for update_row in f:
            updates = update_row.strip().split(",")
            status = checkUpdates(updates, left, right)
            if status:
                part1 += int(updates[len(updates)//2])
    print(part1) #Part 1: 4281
            

if __name__ == "__main__":
    main()