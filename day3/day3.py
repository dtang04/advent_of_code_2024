def find_valid_muls(line):
    muls_sum = 0
    for i,_ in enumerate(line):
        if (line[i:i+4]) == "mul(": #Python list slicing out of bounds gracefully
            comma_pos = -1
            end_brace_pos = -1
            for j in range(i, len(line)):
                if line[j] == "," and comma_pos == -1:
                    comma_pos = j
                elif line[j] == ")" and end_brace_pos == -1:
                    end_brace_pos = j
                    break
            if comma_pos == -1 or end_brace_pos == -1:
                continue
            num1 = 0
            num2 = 0
            try:
                num1 = int(line[i+4:comma_pos])
                num2 = int(line[comma_pos+1:end_brace_pos])
                muls_sum += num1 * num2
            except ValueError:
                continue
    return muls_sum

def main():
    part1 = 0
    with open("day3.txt", "r") as f:
        for l in f:
            l = l.strip()
            part1 += find_valid_muls(l)
        print(part1) #Part 1: 170068701


if __name__ == "__main__":
    main()