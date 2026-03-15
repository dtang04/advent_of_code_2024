def canReachTarget(nums, target, current):
    if len(nums) == 0 and current == target:
        return True
    elif len(nums) == 0:
        return False
    elif current > target:
        return False
    loc = nums[0]
    mult_s = canReachTarget(nums[1:], target, current * loc)
    add_s = canReachTarget(nums[1:], target, current + loc)
    if mult_s or add_s:
        return True
    return False

def main():
    part1_count = 0
    with open("day7.txt", "r") as f:
        for line in f:
            c_pos = line.find(":")
            target = int(line[:c_pos])
            nums = list(map(int, line[c_pos+1:].strip().split(" ")))
            status = canReachTarget(nums[1:], target, nums[0])
            if status:
                part1_count += target
    print(part1_count)



if __name__ == "__main__":
    main()