from collections import deque
from tabnanny import check

def process_data(input_file):
    with open(input_file, "r") as f:
        data = f.read().strip()  # Remove any whitespace
        disk = []
        cur_id = 0
        # Process pairs of characters
        for i in range(0, len(data), 2):
            file_size = int(data[i])
            if i + 1 < len(data):
                free_space = int(data[i+1])
            else:
                free_space = 0
            disk.extend([str(cur_id)] * file_size)
            disk.extend(['.'] * free_space)
            cur_id += 1
    return disk
def part1():
    disk = process_data('../inputs/9.txt')
    for i in range(len(disk)-1, -1, -1):
        if disk[i] != '.':
            for j in range(i):
                if disk[j] == '.':
                    disk[j] = disk[i]
                    disk[i] = '.'
                    break
    check_sum = 0
    for i in range(len(disk)):
        if disk[i] != '.' and disk[i] != '0':
            check_sum += i * int(disk[i])
    return check_sum


def part2():
    disk = process_data('../inputs/9.txt')
    l = 0
    starting = disk[0]
    array = []

    for r in range(1, len(disk)):
        if disk[r] == starting:
            continue
        else:
            length = r-l
            array.append((l, r, length, starting))
            l = r
            starting = disk[r]
    array.append((l, len(disk), len(disk) - l, starting))
    
    print(array, end='\n\n')
    files = [seg for seg in array if seg[3].isdigit()]
    free_spaces = [seg for seg in array if seg[3] == '.']
    files.sort(key=lambda x: int(x[3]), reverse=True)
    free_spaces.sort(key=lambda x: x[0])
    array = files + free_spaces
    print('after sorting:', array)
    
    for i in range(len(array)):
        if array[i][3] != '.':
            file_start, file_end, file_size, file_id = array[i]
            for j in range(len(array)):
                if j == i:
                    continue
                free_start, free_end, free_size, free_id = array[j]
                
                if free_id == '.' and free_size >= file_size and free_start < file_start:
                    new_file_start = free_start
                    new_file_end = free_start + file_size
                    
                    array[i] = (file_start, file_end, file_size, '.')
                    array[j] = (new_file_start, new_file_end, file_size, file_id)

                    remaining_free_size = free_size - file_size
                    if remaining_free_size > 0:
                        leftover_start = new_file_end
                        leftover_end = leftover_start + remaining_free_size
                        array.insert(j+1, (leftover_start, leftover_end, remaining_free_size, '.'))
                    break
    print(array)
    check_sum = 0
    array.sort(key=lambda x: x[0])
    for start, end, size, id in array:
        if id != '.':
            for i in range(start, end):
                check_sum += i * int(id)
    return check_sum


if __name__ == "__main__":
    print(part2())