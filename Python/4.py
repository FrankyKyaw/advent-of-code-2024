def part1():
    matrix = []
    
    with open('../inputs/4.txt', "r") as f:
        lines = f.readlines()
        for line in lines:
            text = list(line.strip())
            matrix.append(text)
            
    directions = [(-1,0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    def check_if_valid(x, y, dx, dy):
        sequence = ['M', 'A', 'S']
        for i in range(len(sequence)):
            nx, ny = x + (i + 1) * dx, y + (i + 1) * dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (matrix[nx][ny] != sequence[i]):
                    return False
            else:
                return False
        return True
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "X":
                for dx, dy in directions:
                    if check_if_valid(r, c, dx, dy):
                        count += 1
    
    return count

def part2():
    matrix = []
    
    with open('../inputs/4.txt', "r") as f:
        lines = f.readlines()
        for line in lines:
            text = list(line.strip())
            matrix.append(text)
            
    directions = [[(-1,1), (1,-1)], [(-1,-1), (1,1)]]
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    
    def check_if_valid(x, y, directions):
        for direction in directions:
            nx, ny = x + direction[0][0], y + direction[0][1]
            mx, my = x + direction[1][0], y + direction[1][1]

            if 0 <= nx < rows and 0 <= ny < cols and 0 <= mx < rows and 0 <= my < cols:
                if ((matrix[nx][ny] == 'M' and matrix[mx][my] == 'S') or (matrix[nx][ny] == 'S' and matrix[mx][my] == 'M')):
                    continue  
                else:
                    return False
            else:
                return False
        return True
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "A":               
                if check_if_valid(r, c, directions):
                    count += 1
    
    return count

if __name__ == '__main__':
    print(part2())
    