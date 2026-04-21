freqMap = {}

def buildFileSys(p_input):
    """
    Converts the input into the file system.
    """
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
            freqMap[ctr] = int(p) # build the freqMap for part 2
            isEmpty = True
            ctr += 1
            num_digs += int(p)
    return (out, num_digs)

def organize(files, num_digs):
    """
    Part 1
    """
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

def organize_block(files):
    current_key = max(freqMap.keys())
    while current_key >= 0:
        next_empty = files.index('.')
        file_loc = files.index(str(current_key)) #find location of beginning of the file
        flag = False
        while next_empty < file_loc:
            ct_contig_empty = 0 #begin counting the contiguous subsequence of empty slots
            while next_empty + ct_contig_empty < len(files) and files[next_empty + ct_contig_empty] == ".":
                if ct_contig_empty + 1 == freqMap[current_key]: # if the block is large enough for the given key     
                    files[next_empty : next_empty + freqMap[current_key]] = [str(current_key)] * freqMap[current_key] # insert the key to fill the contiguous block
                    files[file_loc : file_loc + freqMap[current_key]] = ['.'] * freqMap[current_key] #replace the old file pos with '.'
                    flag = True
                    break
                ct_contig_empty += 1
            if flag:
                break
            next_empty = files.index('.', next_empty + ct_contig_empty + 1) #jump to the next gap
        current_key -= 1 
    return files

def checksum(sorted_files, num_digs):
    chk = 0
    digs = sorted_files[0:num_digs]
    for i,c_num in enumerate(digs):
        chk += int(c_num) * i
    return chk

def checksum_block(sorted_files):
    chk = 0
    for i,c in enumerate(sorted_files):
        if c == ".":
            continue
        chk += int(c) * i
    return chk

def main():
    p_input = []
    with open("day9.txt", "r") as f:
        for line in f:
            p_input += list(line.strip())
        files, num_digs = buildFileSys(p_input)
        sorted_files = organize(files[:], num_digs)
        print(checksum(sorted_files, num_digs)) #Part 1: 6258319840548
        sorted_block_files = organize_block(files)
        print(checksum_block(sorted_block_files))


if __name__ == "__main__":
    main()