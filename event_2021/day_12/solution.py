import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    cave_map = dict()
    for line in lines:
        a, b = line.split('-')
        if a not in cave_map:
            cave_map[a] = []
        if b not in cave_map:
            cave_map[b] = []
        cave_map[a].append(b)
        cave_map[b].append(a)
    
    return cave_map


def traverse(cave_map, src, dest, visited, path):
    paths = 0
    visited[src] = True
    path.append(src)
    if src == dest:
        paths += 1
        print(path)
    else:
        for next_cave in cave_map[src]:
            if not visited[next_cave] or next_cave.isupper():
                paths += traverse(cave_map, next_cave, dest, visited, path)
    
    path.pop()
    visited[src] = False
    return paths


def get_all_paths(cave_map, src, dest):
    visited = {k: False for k in cave_map.keys()}
    path = []
    return traverse(cave_map, src, dest, visited, path)


def check(visited, node):
    if node == 'start':
        return False
    max_found = True
    for k, v in visited.items():
        if k.islower():
            if max_found and v == 2:
                return False
            if v == 2:
                max_found = True
    return True


def traverse2(cave_map, src, dest, visited, path):
    paths = 0
    visited[src] += 1
    print(visited)
    path.append(src)
    if src == dest:
        paths += 1
        print(path)
    else:
        for next_cave in cave_map[src]:
            if visited[next_cave] == 0 or next_cave.isupper() or check(visited, next_cave):
                paths += traverse2(cave_map, next_cave, dest, visited, path)
    
    path.pop()
    visited[src] -= 1
    return paths


def get_all_paths2(cave_map, src, dest):
    visited = {k: 0 for k in cave_map.keys()}
    path = []
    return traverse2(cave_map, src, dest, visited, path)


def main():
    cave_map = read_input('input.txt')
    print(f"Total caves: {len(cave_map)}")
    
    for k, v in cave_map.items():
        print(k, v, sep=' --> ')
    
    # Part one
    valid_paths = get_all_paths(cave_map, 'start', 'end')
    print(f'Valid paths: {valid_paths}')
    
    # Part two
    valid_paths = get_all_paths2(cave_map, 'start', 'end')
    print(f'Valid paths: {valid_paths}')


if __name__ == '__main__':
    main()