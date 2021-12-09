import os


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    
    height_map = []
    for line in lines:
        height_map.append([int(x) for x in line])
        
    return height_map


def is_low_point(height_map, x, y, r_max, c_max):
    adjacents = []
    if x == 0:
        adjacents.append(DOWN)
    elif x == r_max:
        adjacents.append(UP)
    else:
        adjacents.append(UP)
        adjacents.append(DOWN)
    if y == 0:
        adjacents.append(RIGHT)
    elif y == c_max:
        adjacents.append(LEFT)
    else:
        adjacents.append(RIGHT)
        adjacents.append(LEFT)
    return all([height_map[x][y] < height_map[x+a][y+b] for a, b in adjacents ])


def traverse_basin(height_map, x, y, r_max, c_max, seen):
    if (x, y) in seen or x < 0 or y < 0 or x > r_max or y > c_max or height_map[x][y] == 9:
        return 0
    seen.add((x, y))
    basin_size = 1
    for a, b in [UP, DOWN, LEFT, RIGHT]:
        basin_size += traverse_basin(height_map, x+a, y+b, r_max, c_max, seen)
    return basin_size
    

def get_low_points_and_basin_sizes(height_map):
    r_max, c_max = len(height_map) - 1, len(height_map[0]) - 1
    low_points = []
    basin_sizes = []
    seen = set()
    for r, row in enumerate(height_map):
        for c, col in enumerate(row):
            if is_low_point(height_map, r, c, r_max, c_max):
                low_points.append(col)
                basin_sizes.append(traverse_basin(height_map, r, c, r_max, c_max, seen))
    
    return low_points, basin_sizes


def main():
    height_map = read_input('input.txt')
    print(f"Height Map area: {len(height_map)} x {len(height_map[0])}")
    
    # Part one
    low_points, basin_sizes = get_low_points_and_basin_sizes(height_map)
    print(f"Total low points in this area: {len(low_points)}")
    print(f"Low points in this area: {low_points}")
    print(f"Sum of risk levels: {sum(low_points) + len(low_points)}")

    # Part two
    print(f"Total basins in this area: {len(basin_sizes)}")
    print(f"Basins in this area: {basin_sizes}")
    basin_sizes.sort()
    print(f"Product of 3 largest basin sizes = {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}")

    
if __name__ == '__main__':
    main()
