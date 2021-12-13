import os
from termcolor import colored


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    max_x, max_y = 0, 0
    index = 0
    dots = dict()
    count = len(lines)
    while index < count and lines[index] != '':
        x, y = [int(a) for a in lines[index].split(',')]
        if x not in dots:
            dots[x] = []
        dots[x].append(y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        index += 1
    index += 1
    folds = []
    while index < count:
        p, q = lines[index].strip('fold along ').split('=')
        folds.append((p, int(q)))
        index += 1
    
    return dots, max_x, max_y, folds


def fold(dots, max_x, max_y, fold):
    if fold[0] == 'x':
        for col in range(0, fold[1]):
            p, p1 = col, max_x - col
            for row in range(0, max_y + 1):
                if (p not in dots or row not in dots[p]) and (p1 in dots and row in dots[p1]):
                    dots[p] = dots.get(p, [])
                    dots[p].append(row)
                if p1 in dots and row in dots[p1]:
                    dots[p1].remove(row)
                    if len(dots[p1]) == 0:
                        dots.pop(p1)
        if fold[1] in dots:
            dots.pop(fold[1])
        return fold[1] - 1, max_y
    elif fold[0] == 'y':
        for col in range(0, max_x + 1):
            for row in range(0, fold[1]):
                p, p1 = row, max_y - row
                if (col not in dots or p not in dots[col]) and (col in dots and p1 in dots[col]):
                    dots[col] = dots.get(col, [])
                    dots[col].append(p)
                if col in dots:
                    if fold[1] in dots[col]:
                        dots[col].remove(fold[1])
                    if p1 in dots[col]:
                        dots[col].remove(p1)
                        if len(dots[col]) == 0:
                            dots.pop(col)
        return max_x, fold[1] - 1


def count_dots(dots):
    count = 0
    for v in dots.values():
        count += len(v)
    return count


def print_dots(dots, max_x, max_y):
    for i in range(max_y+1):
        for j in range(max_x+1):
            if j in dots and i in dots[j]:
                print(colored('#', 'green', 'on_green'), end='')
            else:
                print("\033[98m \033[00m", end='')
        print()


def main():
    dots, max_x, max_y, folds = read_input('input.txt')
    print(f"Total dots on paper: {sum([len(x) for x in dots.values()])}")
    print(f"Last x-coordinate: {max_x}; Last y-coordinate: {max_y}")
    print(f"Folds to do: {len(folds)}")
    # print_dots(dots, max_x, max_y)
    
    # Part one
    max_x, max_y = fold(dots, max_x, max_y, folds[0])
    # print_dots(dots, max_x, max_y)
    print(f"Updated: Last x-coordinate: {max_x}; Last y-coordinate: {max_y}")
    print(f"Dots remaining: {count_dots(dots)}")
    
    # Part two
    for f in folds[1:]:
        max_x, max_y = fold(dots, max_x, max_y, f)
    print(f"Updated: Last x-coordinate: {max_x}; Last y-coordinate: {max_y}")
    print(f"Dots remaining: {count_dots(dots)}")
    print_dots(dots, max_x, max_y)    


if __name__ == '__main__':
    main()
