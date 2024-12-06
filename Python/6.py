def part1():
    matrix = []
    
    with open('../inputs/6.txt', "r") as f:
        lines = f.readlines()
        for line in lines:
            text = list(line.strip())
            matrix.append(text)
    rows, cols = len(matrix), len(matrix[0])
    
    cur_point = None
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '^':
                cur_point = (i, j)
                break
    starting_point = cur_point
    directions = {'up': ['right', (-1,0)], 'right': ['down', (0, 1)], 'down': ['left', (1, 0)], 'left': ['up', (0, -1)]}
    visited = set()
    current_direction = 'up'
    next_r, next_c = cur_point[0] + directions[current_direction][1][0], cur_point[1] + directions[current_direction][1][1]
    cur_r, cur_c = cur_point
    while 0 <= next_r < rows and 0 <= next_c < cols:

        visited.add((cur_r, cur_c))
        if matrix[next_r][next_c] == "#":
            current_direction = directions[current_direction][0]
            next_r, next_c = cur_r + directions[current_direction][1][0], cur_c + directions[current_direction][1][1]
        else:
            cur_r, cur_c = next_r, next_c
            next_r, next_c = cur_r + directions[current_direction][1][0], cur_c + directions[current_direction][1][1]
            
    visited.add((cur_r, cur_c))
    return matrix, visited, starting_point, len(visited) + 1


def part2():
    matrix, visited, starting_point, visited_len = part1()
    rows, cols = len(matrix), len(matrix[0])
    directions = {'up': ['right', (-1,0)], 'right': ['down', (0, 1)], 'down': ['left', (1, 0)], 'left': ['up', (0, -1)]}
    
    def check_if_loop(matrix):
        local_visited = set()
        current_direction = 'up'
        next_r, next_c = starting_point[0] + directions[current_direction][1][0], starting_point[1] + directions[current_direction][1][1]
        cur_r, cur_c = starting_point
        
        while 0 <= next_r < rows and 0 <= next_c < cols:
            current_state = (cur_r, cur_c, current_direction)
            if current_state in local_visited:
                return True
            
            local_visited.add(current_state)
            
            if matrix[next_r][next_c] == "#":
                current_direction = directions[current_direction][0]
                next_r, next_c = cur_r + directions[current_direction][1][0], cur_c + directions[current_direction][1][1]
            else:
                cur_r, cur_c = next_r, next_c
                next_r, next_c = cur_r + directions[current_direction][1][0], cur_c + directions[current_direction][1][1]
            
        return False
    count = 0
    for i in visited:
        if i == starting_point:
            continue
        new_matrix = [row.copy() for row in matrix]
        new_matrix[i[0]][i[1]] = "#"
        if check_if_loop(new_matrix):
            count += 1
    return count
            
if __name__ == '__main__':
    print(part2())
    
    