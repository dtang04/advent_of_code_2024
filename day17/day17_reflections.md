## Day 16 (AoC 2024)

## Part 1

Part 1 was straightforward, just making sure to read the operation functionalities carefully.

For a given initial value in register A, the `out` list would be built via `process()`.

## Part 2

Part 2 was definitely more difficult, having to find the initial register A value that would
result in the `out` list being identical to the instructions list.

The first realization was that instead of having to reverse-engineer instruction by instruction,
there was a core invariant in the structure of the instructions: that is, some `jnz` that checked if
`reg_A == 0`, and some way of shrinking `reg_A` via every iteration (typically by some call to `adv`).

So, the general structure of every sequence instructions must take on the following pattern:

```
init reg_A = val
// sequence of instructions...
adv j
jnz k
```

However, this alone isnt enough to narrow down the invariant, as j is a *combo operand*. If `j == 5` (register B),
for example, that would be problematic because then we'd have to check how B changes.

Luckily, looking closely at the instructions, we have that one of the instructions is `0 3`. This is `adv 8`.
That means that in the loop, `reg_A = reg_A // 2`.

This is good, but it would again be problematic if there were also instructions changing `reg_A`.

Again, however, looking at the test case we have the sequence of instructions:

2,4,1,7,7,5,1,7,*0,3*,4,1,5,5,3,0

Decoding these instructions we have:

```
2,4 -> bst A      # B = A % 8
1,7 -> bxl 7      # B = B ^ 7
7,5 -> cdv B      # C = A // 2^B
1,7 -> bxl 7      # B = B ^ 7
0,3 -> adv 3      # A = A // 8
4,1 -> bxc        # B = B ^ C
5,5 -> out B      # output B % 8
3,0 -> jnz 0      # jump to 0 if A != 0
```

So, the only time A is modified is 0,3. This simplifies things a lot, because we now know the loop condition.

But even better, the output line `5,5` is `B % 8`. This means that every entry in out represents on octal bit, and can only be from 0-7.
    * This makes sense, because recall that operands also must be from 0-7. If we want out to match the instrucitons, then each element in out also must be 0-7.

So, we can simplify the instructions further to the following:
```
init reg_A
while reg_A != 0:
    # run ops here...
    out.append(octal_bit)
    reg_A // 8
```
So, this leads us to two observations:
1. For every loop, we strip off an octal bit from reg_A. Since `out == inst`, each element in `inst` must be responsible for a loop of the instruction.
2. In every loop, we output a value from 0-7 into out. We combine this with (1), where it follows that each element in
`inst` must correspond to an output. 

We could then brute-force the right answer by building a `candidates` list, and at some index `k` in the instructions list, the intermediate out log we want to match is (`inst[k:]`). Then, for the candidates from the previous iteration, we consider all possible octal bit values to append to the candidate (0-8). If `process(candidate + digit_i)`matches the log from `inst[k:]`, onwards, we keep it in the candidate list. Otherwise, discard.

So, we have the following:

```
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
```

### Focus Points
* Octal representations
* Finding invariants
* Simplifying the problem (in this case, based on the input)


