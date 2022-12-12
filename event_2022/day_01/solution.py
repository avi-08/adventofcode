import argparse
import os
import logging


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines


def parse_by_elves(lines):
    calories_by_elves = [[]]
    for l in lines:
        if l == '':
            calories_by_elves.append([])
        else:
            calories_by_elves[-1].append(int(l.strip()))
    return calories_by_elves
        

def main(args):
    lines = read_input('sample.txt' if args.run_sample else 'input.txt')
    
    # Part one
    calories_by_elves = parse_by_elves(lines)
    logging.debug(f"Calories grouped by elves: {calories_by_elves}")
    
    total_calories_by_elves = [sum(cals) for cals in calories_by_elves]
    
    total_calories_by_elves.sort()
    logging.debug(f"Total calories sorted: {total_calories_by_elves}")
        
    logging.info(f"Maximum calories: {total_calories_by_elves[-1]}")
    
    # Part two
    logging.info(f"Top 3 calorie count: {total_calories_by_elves[-3:]}")
    logging.info(f"Total of top 3 calories: {sum(total_calories_by_elves[-3:])}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-s', '--run-sample', action='store_true', help='Run with sample.txt; if omitted, runs with input.txt')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG if args.verbose else logging.INFO)
    main(args)
