def buildFileSys(p_input):
    ctr = 0
    isEmpty = False
    out = []
    num_digs = 0
    for p in p_input:
        if isEmpty:
            out += "." * int(p)
            isEmpty = False
        else:
            for i in range(int(p)): # for loop to handle case where id >= 10
                out.append(str(ctr))
            isEmpty = True
            ctr += 1
            num_digs += int(p)
    return (out, num_digs)

def organize(files, num_digs):
    end = False
    current_i = len(files) - 1
    while not(end):
        if files[current_i] == '.':
            current_i -= 1
        else:
            # current_i is a digit, so move the digit to the first '.', replace current_i loc with '.'
            firstEmpty = files.index('.')
            files[firstEmpty] = files[current_i]
            files[current_i] = '.'
            current_i -= 1

        if '.' not in files[0:num_digs]: # num_dig len block of numbers
            end = True
    return files

def checksum(sorted_files, num_digs):
    chk = 0
    digs = sorted_files[0:num_digs]
    for i,c_num in enumerate(digs):
        chk += int(c_num) * i
    return chk


def main():
    p_input = []
    with open("day9.txt", "r") as f:
        for line in f:
            p_input += list(line.strip())
        files, num_digs = buildFileSys(p_input)
        largest = int(files[-1])
        sorted_files = organize(files, num_digs)
        print(checksum(sorted_files, num_digs)) #Part 1: 6258319840548


if __name__ == "__main__":
    main()