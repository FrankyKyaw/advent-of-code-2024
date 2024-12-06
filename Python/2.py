def main1():
    with open('../inputs/2.txt', "r") as f:
        reports = [list(map(int, line.strip().split())) for line in f]
    
    safe_reports = 0
    for level in reports:
        ascending = level[0] < level[1]
        safe_report = all(
            1 <= level[i+1] - level[i] <= 3 if ascending
            else 1 <= level[i] - level[i+1] <= 3
            for i in range(len(level) - 1)
        )
        if safe_report:
            safe_reports += 1
    return safe_reports
                     
def main():
    with open('../inputs/2.txt', "r") as f:
        reports = [list(map(int, line.strip().split())) for line in f]
    
    def is_safe(level):
        ascending = level[0] < level[1]
        return all(
            1 <= (level[i+1] - level[i] if ascending else level[i] - level[i+1]) <= 3
            for i in range(len(level) - 1)
    )
    safe_reports = 0
    for level in reports:
        if is_safe(level):
            safe_reports += 1
        else:
            for i in range(len(level)):
                new_level = level[:i] + level[i+1:]
                if is_safe(new_level):
                    safe_reports += 1
                    break

    return safe_reports
            
            
if __name__ == '__main__':
    print(main())