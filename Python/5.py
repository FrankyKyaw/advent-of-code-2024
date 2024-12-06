from collections import defaultdict

def part1():
    with open('../inputs/5.txt', "r") as f:
        lines = f.readlines()
        data = [line.strip() for line in lines]
    index = data.index('')
    data1 = data[:index]
    data2 = data[index+1:]
    hashset = defaultdict(list)
    for i in data1:
        first, second = i.split('|')
        hashset[second].append(first)
    data2 = [line.split(',') for line in data2]
    count = 0
    
    def check_valid_update(update):
        for i in range(len(update)-1):
            if update[i] in hashset[update[i+1]]:
                continue
            else:
                return False
        return True
    
    total = 0
    for update in data2:
        if check_valid_update(update):
            total += int(update[len(update)//2])
    return total

def part2():
    with open('../inputs/5.txt', "r") as f:
        lines = f.readlines()
        data = [line.strip() for line in lines]
    index = data.index('')
    data1 = data[:index]
    data2 = data[index+1:]
    hashset = defaultdict(list)
    for i in data1:
        first, second = i.split('|')
        hashset[second].append(first)
    data2 = [line.split(',') for line in data2]
    count = 0
    
    def check_valid_update(update):
        for i in range(len(update)-1):
            if update[i] in hashset[update[i+1]]:
                continue
            else:
                return False
        return True
    
    unsorted = []
    for update in data2:
        if not check_valid_update(update):
            unsorted.append(update)
            
    def custom_sort_key(item, i): 
        return sum(item in hashset.get(key) for key in i)
                                                      
    res = []
    for i in unsorted:
        sorted_items = sorted(i, key=lambda item: custom_sort_key(item, i), reverse=True)
        res.append(sorted_items)
    
    total = sum([int(i[len(i)//2]) for i in res])
    
    return total
if __name__ == '__main__':
    print(part2())