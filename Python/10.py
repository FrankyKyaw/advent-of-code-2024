def process():
    with open('../inputs/10.txt') as f:
        lines = f.readlines()
        data = [list(map(int, line.strip())) for line in lines]
        return data
    
def dfs(grid, r, c, current_height, end_reached):
    if current_height == 9:
        end_reached.append((r, c))
        return
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for (dx, dy) in directions:
        new_r, new_c = r+dx, c+dy
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == grid[r][c]+1:
            dfs(grid, new_r, new_c, current_height+1, end_reached)
    
def part1():
    data = process()
    trailheads = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == 0:
                trailheads.append((r, c))
    # print(trailheads)
    total = 0
    for (start_r, start_c) in trailheads:
        end_reached = []
        dfs(data, start_r, start_c, 0, end_reached)
        total += len(end_reached)
    return total
if __name__ == '__main__':
    print(part1())
    # print(part2())