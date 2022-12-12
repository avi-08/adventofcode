import argparse
import os
import logging


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines


def get_priority(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    elif ord(item) >= ord('A') and ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27


def get_badge(priority):
    if priority >= 1 and priority <= 26:
        return chr(ord('a') + priority - 1)
    elif priority >= 27 and priority <= 52:
        return chr(ord('A') + priority - 27)


def get_intersection(bag_items):
    n = len(bag_items)
    set_a = set(bag_items[:n // 2])
    for ch in  bag_items[n // 2:]:
        if ch in set_a:
            return ch


def identify_badge(group):
    logging.debug(f"Group: {group}")
    mat = [[0] * 52 for _ in range(len(group))]
    for i in range(len(group)):
        for ch in group[i]:
            mat[i][get_priority(ch) - 1] = 1
    
    for row in mat:
        logging.debug(row)
    
    for col in range(len(mat[0])):
        val = 1
        for row in range(len(mat)):
            val = val & mat[row][col]
        if val == 1:
            logging.debug(f"Found all 3 at col: {col}")
            return get_badge(col + 1) 
    

def main(args):
    lines = read_input('sample.txt' if args.run_sample else 'input.txt')
    
    # Part one
    total_priority = 0
    for line in lines:
        ch = get_intersection(line)
        logging.debug(f"Common item: {ch}")
        total_priority += get_priority(ch)
    
    logging.info(f"Total priority: {total_priority}")
    
    # Part two
    total_group_priority = 0
    for i in range(0, len(lines) - 2, 3):
        badge = identify_badge(lines[i:i+3])
        logging.debug(f"Common item in the group: {badge}")
        total_group_priority += get_priority(badge)
    
    logging.info(f"Total group priority: {total_group_priority}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-s', '--run-sample', action='store_true', help='Run with sample.txt; if omitted, runs with input.txt')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG if args.verbose else logging.INFO)
    main(args)
