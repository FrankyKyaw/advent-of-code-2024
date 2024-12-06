import re

def part1():
    with open('../inputs/3.txt', "r") as f:
        corrupted_memory = f.read()
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, corrupted_memory)
    total = 0
    for match in matches:
        digi_pattern = r'\d+'
        nums = re.findall(digi_pattern, match)
        total += int(nums[0]) * int(nums[1])
    return total

def extract_nums(match):
    digi_pattern = r'\d+'
    nums = re.findall(digi_pattern, match)
    return int(nums[0]) * int(nums[1])

def part2():
    pattern = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'
    # corrupted_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    with open('../inputs/3.txt', "r") as f:
        corrupted_memory = f.read()
    matches = re.findall(pattern, corrupted_memory)
    
    total = extract_nums(matches[0])
    disabled = False
    for match in matches[1:]:
        if match == "do()":
            disabled = False
        elif match == "don't()":
            disabled = True
        else:
            if not disabled:
                total += extract_nums(match)
            
    return total

if __name__ == '__main__':
    print(part2())