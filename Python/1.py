from collections import Counter
def main():
    col1, col2 = [], []
    try:
        with open('../1.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                num1, num2 = line.strip().split()
                col1.append(int(num1))
                col2.append(int(num2))
    except FileNotFoundError:
        print("File not found")
        return
    
    # Part 1
    # col1.sort()
    # col2.sort()
    # total = 0
    # for i, val in enumerate(col1):
    #     difference = abs(val - col2[i])
    #     total += difference
    # return total 
    total = 0
    col2_counts = Counter(col2)
    for i in col1:
        total += i * col2_counts[i]
    
    return total
if __name__ == '__main__':
    print("Total difference:", main())