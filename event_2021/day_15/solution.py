import os
import sys
import heapq


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        
    matrix = [[int(x) for x in line] for line in lines]

    return matrix


def save_matrix(matrix, file_name='matrix.txt'):
    op = ''
    for row in matrix:
        for col in row:
            op += str(col)
        op += '\n'
    
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'w') as f:
        f.write(op)
    return file_path
    

def get_next(r, c, max_r, max_c):
    return [(r + a, c + b) for a, b in [LEFT, RIGHT, UP, DOWN] if (r + a) in range(max_r) and (c + b) in range(max_c)]


def get_shortest_path(matrix, max_r, max_c):
    dist = [[sys.maxsize for _ in range(max_c)] for _ in range(max_r)]
    dist[0][0] = matrix[0][0]
    
    pq = []
    heapq.heappush(pq, (dist[0][0], (0, 0)))
    while len(pq) > 0:
        curr = heapq.heappop(pq)
        curr_x, curr_y = curr[1]
        for x, y in get_next(curr_x, curr_y, max_r, max_c):
            if dist[x][y] > dist[curr_x][curr_y] + matrix[x][y]:
                if dist[x][y] != sys.maxsize:
                    adj = (dist[x][y], (x, y))
                    try:
                        pq.remove(adj)
                    except ValueError as ex:
                        print(f"Failed to remove {adj} from pq. {ex}")
                dist[x][y] = dist[curr_x][curr_y] + matrix[x][y]
                heapq.heappush(pq, (dist[x][y], (x, y)))    
    return dist[max_r-1][max_c-1]
    

def main():
    matrix = read_input('input.txt')
    max_r, max_c = len(matrix), len(matrix[0])
    print(f"Matrix size: {max_r} X {max_c}")
    
    # Part one
    shortest_path = get_shortest_path(matrix, max_r, max_c)
    print(f"Minimum risk: {shortest_path - matrix[0][0]}")
    
    # Part two
    for i in range(4):
        for row in range(0, max_r):
            c_start, c_end = i * max_c, (i+1) * max_c
            for col in range(c_start, c_end):
                temp = (matrix[row][col] % 9) + 1
                matrix[row].append(temp)
    
    for i in range(4):
        r_start, r_end = i * max_r, (i+1) * max_r
        for row in range(r_start, r_end):
            matrix.append([])
            for col in range(len(matrix[0])):
                temp = (matrix[row][col] % 9) + 1
                matrix[-1].append(temp)
    
    max_r, max_c = len(matrix), len(matrix[0])
    print(f"Updated Matrix size: {max_r} X {max_c}")
    save_matrix(matrix, 'updated_matrix.txt')
    
    shortest_path = get_shortest_path(matrix, max_r, max_c)
    print(f"Minimum risk: {shortest_path - matrix[0][0]}")


if __name__ == '__main__':
    main()
