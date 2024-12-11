import time 
from collections import defaultdict

def part1(blink_times): 
    with open('../inputs/11.txt') as f: 
        data = f.read().strip() 
        data = [int(i) for i in data.split(' ')] 
        
        counter = defaultdict(int)
        for num in data:
            counter[num] += 1
        
        
        for _ in range(blink_times): 
            new_counter = defaultdict(int)
            for num, count in counter.items():
                if num == 0:
                    new_counter[1] += count
                elif len(str(num)) % 2 == 0:
                    mid = len(str(num)) // 2
                    new_counter[int(str(num)[:mid])] += count
                    new_counter[int(str(num)[mid:])] += count
                else:
                    new_counter[num * 2024] += count
            print(new_counter)
            counter = new_counter 
            print('Blink', _ + 1, 'times') 
    
    return sum(counter.values())




if __name__ == '__main__':
    start_time = time.time()
    print(part1(10))
    print("--- %s seconds ---" % (time.time() - start_time))