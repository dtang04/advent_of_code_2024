
#------------Registers------------
reg_A = 0
reg_B = 0
reg_C = 0

inst_ptr = 0

#------------Globals------------
insts = []

outputs = [] # Outputs produced by out inst

def process(num_to_try=None):
    global inst_ptr, reg_A, reg_B, reg_C

    if num_to_try != None:
        reg_A = num_to_try
        reg_B = 0
        reg_C = 0

    while inst_ptr < len(insts):
        isJump = False

        opcode = insts[inst_ptr]
        operand = insts[inst_ptr+1]

        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3:
            inst_ptr_loc = inst_ptr
            jnz(operand)
            if inst_ptr_loc != inst_ptr:
                isJump = True
        elif opcode == 4:
            bxc(operand)
        elif opcode == 5:
            out(operand)
        elif opcode == 6:
            bdv(operand)
        else:
            cdv(operand)

        if not isJump: # if jnz produced a jump, don't increment the inst_ptr
            inst_ptr += 2

    inst_ptr = 0 # for part 2, reset the inst_ptr for next candidate process

def findSmallestCandidate():
    global outputs
    candidates = [0]
    for next_ind in range(len(insts)-1, -1, -1): # next digit to parse in output (high -> low)
        next_candidates = []
        to_match = insts[next_ind:]
        for i,c in enumerate(candidates):
            for next_dig in range(8): # try all 8 possibilities for the next digit
                num_to_try = (c << 3) + next_dig
                process(num_to_try)
                if outputs == to_match:
                    next_candidates.append(num_to_try)
                outputs = [] # reset output for the next candidate process
        candidates = next_candidates
    return min(candidates)


def writeTo(operand):
    if operand == 7:
        return
    if operand <= 3:
        return operand
    if operand == 4:
        return 'A'
    elif operand == 5:
        return 'B'
    else:
        return 'C'

#------------Instructions------------

# Opcode 0
def adv(operand):
    global reg_A

    num = reg_A
    denom = writeTo(operand)

    if denom is None:
        return

    if denom == 'A':
        denom = reg_A
    elif denom == 'B':
        denom = reg_B
    elif denom == 'C':
        denom = reg_C 

    denom = 2 ** denom

    reg_A = num // denom

# Opcode 1
def bxl(operand):
    global reg_B
    
    reg_B = reg_B ^ operand

# Opcode 2
def bst(operand):
    global reg_B

    val = writeTo(operand)

    if val is None:
        return
    if val == 'A':
        val = reg_A
    elif val == 'B':
        val = reg_B
    elif val == 'C':
        val = reg_C
    
    reg_B = val % 8

# Opcode 3
def jnz(operand):
    global inst_ptr

    if reg_A == 0:
        return
    
    inst_ptr = operand

# Opcode 4
def bxc(operand):
    global reg_B

    reg_B = reg_B ^ reg_C

# Opcode 5
def out(operand):
    val = writeTo(operand)

    if val is None:
        return
    if val == 'A':
        val = reg_A
    elif val == 'B':
        val = reg_B
    elif val == 'C':
        val = reg_C
    
    outputs.append(val % 8)

# Opcode 6
def bdv(operand):
    global reg_B

    num = reg_A
    denom = writeTo(operand)

    if denom is None:
        return

    if denom == 'A':
        denom = reg_A
    elif denom == 'B':
        denom = reg_B
    elif denom == 'C':
        denom = reg_C 

    denom = 2 ** denom

    reg_B = num // denom

# Opcode 7
def cdv(operand):
    global reg_C

    num = reg_A
    denom = writeTo(operand)

    if denom is None:
        return

    if denom == 'A':
        denom = reg_A
    elif denom == 'B':
        denom = reg_B
    elif denom == 'C':
        denom = reg_C 

    denom = 2 ** denom

    reg_C = num // denom

def recreate():
    candidates = []

    
def main():
    global reg_A, reg_B, reg_C, outputs
    line_br = False
    with open("day17.txt", 'r') as f:
        for l in f:
            if l == '\n':
                line_br = True
                continue
            l = l.strip()
            if not line_br: # Reading initial state of registers to mem
                col_pos = l.index(':')
                reg = l[col_pos-1]
                reg_val = int(l[col_pos+2:])
                if reg == 'A':
                    reg_A = reg_val
                elif reg == 'B':
                    reg_B = reg_val
                else:
                    reg_C = reg_val
            else:
                col_pos = l.index(':')
                raw_insts = l[col_pos+2:].split(",")
                for r in raw_insts:
                    insts.append(int(r)) 
    
    process()

    outputs_str = []
    for out in outputs:
        outputs_str.append(str(out))

    print(",".join(outputs_str)) # Part 1: 2,0,4,2,7,0,1,0,3

    outputs = []

    print(findSmallestCandidate()) # Part 2: 265601188299675

if __name__ == "__main__":
    main()