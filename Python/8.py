def part1():
    with open('../inputs/8.txt', "r") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            data.append(list(line.strip()))
    
    def get_antinodes(ant1, ant2):
        r1, c1 = ant1
        r2, c2 = ant2
        dif_r, dif_c = r1-r2, c1-c2
        new1 = r1+dif_r, c1+dif_c
        new2 = r2-dif_r, c2-dif_c
        return new1, new2
    
    rows, cols = len(data), len(data[0])
    new_matrix = [rows.copy() for rows in data]
    print(f'rows: {rows}, cols: {cols}')
    res = set()
    for r in range(rows):
        for c in range(cols):
            initial_element = data[r][c]
            if initial_element != '.':
                for r1 in range(r, rows):
                    start_col = c+1 if r1 == r else 0
                    for c1 in range(start_col, cols):
                        if data[r1][c1] == initial_element:
                            new1, new2 = get_antinodes((r,c), (r1,c1))
                            if 0 <= new1[0] < rows and 0 <= new1[1] < cols:
                                new_matrix[new1[0]][new1[1]] = '#'
                                res.add(new1)
                            if 0 <= new2[0] < rows and 0 <= new2[1] < cols:
                                new_matrix[new2[0]][new2[1]] = '#'
                                res.add(new2)
    return len(res)


def part2():
    with open('../inputs/8.txt', "r") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            data.append(list(line.strip()))
    
    
    
    rows, cols = len(data), len(data[0])
    
    def get_antinodes(ant1, ant2, rows=rows, cols=cols):
        antinodes = []
        r1, c1 = ant1
        r2, c2 = ant2
        dif_r, dif_c = r1-r2, c1-c2
        while True:
            r1, c1 = r1+dif_r, c1+dif_c
            if 0 <= r1 < rows and 0 <= c1 < cols:
                antinodes.append((r1, c1))
            else:
                break
        while True:
            r2, c2 = r2-dif_r, c2-dif_c
            if 0 <= r2 < rows and 0 <= c2 < cols:
                antinodes.append((r2, c2))
            else:
                break
        
        return antinodes
    
    
    new_matrix = [rows.copy() for rows in data]
    res = set()
    for r in range(rows):
        for c in range(cols):
            initial_element = data[r][c]
            if initial_element != '.':
                res.add((r, c))
                for r1 in range(r, rows):
                    start_col = c+1 if r1 == r else 0
                    for c1 in range(start_col, cols):
                        if data[r1][c1] == initial_element:
                            antinodes = get_antinodes((r,c), (r1,c1))
                            res.add((r1, c1))
                            # print(f'for {r,c} and {r1,c1} antinodes are {antinodes}')
                            for i in antinodes:
                                new_matrix[i[0]][i[1]] = '#'
                                res.add(i)
    # for i in new_matrix:
    #     print(i)
    return len(res)
if __name__ == "__main__":
    print(part2())
    

"""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""