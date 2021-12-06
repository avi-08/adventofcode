import math
import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        input_lines = f.readlines()
    
    vent_lines = []
    grid_max_x, grid_max_y = 0, 0
    for line in input_lines:
        xy1, xy2 = line.strip().split(' -> ')
        vent_lines.append([[int(p) for p in xy1.split(',')], [int(q) for q in xy2.split(',')]])
        grid_max_x = max(grid_max_x, max(vent_lines[-1][0][0], vent_lines[-1][1][0]))
        grid_max_y = max(grid_max_y, max(vent_lines[-1][0][1], vent_lines[-1][1][1]))
    
    return vent_lines, (grid_max_x, grid_max_y)


def get_slope(line):
    x2_x1 = line[1][0] - line[0][0]
    y2_y1 = line[1][1] - line[0][1]
    return x2_x1 // y2_y1 if y2_y1 != 0 else math.inf


def check_angle_is_45(line):
    return abs(get_slope(line)) == 1


def get_overlaps(vent_lines, grid_max, include_diagonal = False):
    grid = [[0 for j in range(grid_max[1]+1)] for i in range(grid_max[0]+1)]
    print(f"{len(grid) } X {len(grid[0])} grid")
    overlap_count = 0
    for line in vent_lines:
        if include_diagonal and check_angle_is_45(line):
            beg_x, beg_y = line[0] if line[0][0] <= line[1][0] else line[1]
            end_x, end_y = line[1] if line[0][0] <= line[1][0] else line[0]
            slope = get_slope(line)
            while beg_x <= end_x:
                grid[beg_x][beg_y] += 1
                if grid[beg_x][beg_y] == 2:
                    overlap_count += 1
                beg_x += 1
                beg_y += slope
            pass
        elif line[0][0] == line[1][0]:
            # Vertical
            beg, end = (line[0][1], line[1][1]) if line[0][1] < line[1][1] else (line[1][1], line[0][1])
            for col in range(beg, end + 1):
                grid[line[0][0]][col] += 1
                if grid[line[0][0]][col] == 2:
                    overlap_count += 1
        elif line[0][1] == line[1][1]:
            # Horizontal
            beg, end = (line[0][0], line[1][0]) if line[0][0] < line[1][0] else (line[1][0], line[0][0])
            for row in range(beg, end + 1):
                grid[row][line[0][1]] += 1
                if grid[row][line[0][1]] == 2:
                    overlap_count += 1
    
    return overlap_count

def main():
    vent_lines, grid_max = read_input()
    print(f'Total vents: {len(vent_lines)}')
    print(f'Extreme ends of grid: {grid_max}')

    # Part one
    overlaps_1 = get_overlaps(vent_lines, grid_max)
    print(f"Points with atleast 2 vent intersections(only horizontal and vertical): {overlaps_1}")

    print("\n<=============>\n")
    # Part two
    overlaps_2 = get_overlaps(vent_lines, grid_max, True)
    print(f"Points with atleast 2 vent intersections(horizontal, vertical and 45 degreee daigonal): {overlaps_2}")


if __name__ == '__main__':
    main()
