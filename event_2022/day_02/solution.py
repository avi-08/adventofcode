import os
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines



RPS_MAP = {
    "X": "B",
    "Y": "C",
    "Z": "A",
    "A": "Y",
    "B": "Z",
    "C": "X"
}

RPS_MAP_WIN = {
    "A": "B",
    "B": "C",
    "C": "A"
}

RPS_MAP_LOSS = {
    "A": "C",
    "B": "A",
    "C": "B"
}


RPS_VALUES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}


def calculate_score_p1(lines):
    score = 0
    for l in lines:
        p1, p2 = l.split(" ")
        logging.debug(f"{p1}, {p2}")
        if RPS_VALUES[p1] == RPS_VALUES[p2]:
            score += 3
            logging.debug(f"{p1}, {p2}, Draw")
        elif RPS_MAP[p1] == p2:
            score += 6
            logging.debug(f"{p1}, {p2}, Win")
        else:
            logging.debug(f"{p1}, {p2}, Loss")
        score += RPS_VALUES[p2]
        logging.debug(f"Curr: {score}")
    return score


def calculate_score_p2(lines):
    score = 0
    for l in lines:
        p1, p2 = l.split(" ")
        logging.debug(f"{p1}, {p2}")
        if p2 == "Y":
            score += 3
            score += RPS_VALUES[p1]
            logging.debug(f"{p1}, {p1}, Draw")
        elif p2 == "Z":
            score += 6
            score += RPS_VALUES[RPS_MAP_WIN[p1]]
            logging.debug(f"{p1}, {RPS_MAP_WIN[p1]}, Win")
        else:
            score += RPS_VALUES[RPS_MAP_LOSS[p1]]
            logging.debug(f"{p1}, {RPS_MAP_LOSS[p1]}, Loss")
        logging.debug(f"Curr: {score}")
    return score
            

def main():
    lines = read_input('input.txt')
    
    # Part one
    p1_score = calculate_score_p1(lines)
    logging.info(f"Part1 Score: {p1_score}")
    
    # Part two
    p2_score = calculate_score_p2(lines)
    logging.info(f"Part2 Score: {p2_score}")

if __name__ == '__main__':
    main()