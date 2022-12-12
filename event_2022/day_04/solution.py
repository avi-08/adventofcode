import argparse
import os
import logging
from typing import List


class RangePair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"(Range: [{self.x}, {self.y}])"

    def is_contained(self, pair) -> bool:
        return self.x >= pair.x and self.y <= pair.y
    
    def has_overlap(self, pair) -> bool:
        return self.x <= pair.x <= self.y or self.x <= pair.y <= self.y


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines

def convert_to_pairs(lines) -> List[RangePair]:
    range_pairs = []
    for line in lines:
        r1, r2 = line.split(",")
        a, b = r1.split("-")
        c, d = r2.split("-")
        range_pairs.append((RangePair(int(a), int(b)), RangePair(int(c), int(d))))
    return range_pairs
    

def main(args):
    lines = read_input('sample.txt' if args.run_sample else 'input.txt')
    logging.debug(f"Input: {lines}")
    
    pairs = convert_to_pairs(lines)
    logging.debug(f"Pairs: {pairs}")
    
    # Part one
    duplicate_ranges = 0
    for p1, p2 in pairs:
        if p1.is_contained(p2) or p2.is_contained(p1):
            logging.debug(f"Identified redundant range pairs: {p1}, {p2}")
            duplicate_ranges += 1
    
    logging.info(f"Total redundant range pairs: {duplicate_ranges}")
    
    # Part two
    overlapping_ranges = 0
    for p1, p2 in pairs:
        if p1.has_overlap(p2) or p2.has_overlap(p1):
            logging.debug(f"Identified overlapping range pairs: {p1}, {p2}")
            overlapping_ranges += 1

    logging.info(f"Total overlapping range pairs: {overlapping_ranges}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-s', '--run-sample', action='store_true', help='Run with sample.txt; if omitted, runs with input.txt')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG if args.verbose else logging.INFO)
    main(args)
