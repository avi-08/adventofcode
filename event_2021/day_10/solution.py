import os
import statistics


VALID_PAIRS = {
    "}": "{",
    ")": "(",
    "]": "[",
    ">": "<"
}

SYNTAX_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

VALID_COMPLETIONS = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

AUTOCOMPLETE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines


def find_invalid(line):
    stack = []
    for ch in line:
        if ch in VALID_PAIRS.values():
            stack.append(ch)
        else:
            if len(stack) > 0 and stack[-1] != VALID_PAIRS[ch]:
                return ch
            else:
                stack.pop(-1)
    return None
            

def get_syntax_score(lines):
    score, invalid_lines = 0, []
    for line in lines:
        invalid_char = find_invalid(line)
        if invalid_char:
            score += SYNTAX_SCORE[invalid_char]
            invalid_lines.append(line)
    return score, invalid_lines


def find_completions(line):
    stack = []
    completion = ''
    for ch in line:
        if ch in VALID_COMPLETIONS.keys():
            stack.append(ch)
        else:
            stack.pop(-1)
    for ch in stack[::-1]:
        completion += VALID_COMPLETIONS[ch]
    return completion


def get_autocomplete_score(lines):
    scores, completions = [], []
    for line in lines:
        score = 0
        completion = find_completions(line)
        for ch in completion:
            score *= 5
            score += AUTOCOMPLETE_SCORE[ch]
        completions.append(completion)
        scores.append(score)
    return scores, completions


def main():
    lines = read_input('input.txt')
    print(f"Total lines: {len(lines)}")
    
    # Part one
    score, invalid_lines = get_syntax_score(lines)
    print(f"Syntax score: {score}")
    print("Invalid lines:")
    for line in invalid_lines:
        lines.remove(line)
        print(f"==> {line}")
    
    print('\n<------------------->\n')
    # Part two
    print(f"Remaining incomplete lines: {len(lines)}")
    scores, completions = get_autocomplete_score(lines)
    for i in range(len(scores)):
        print(f"Completion: [{completions[i]}] Auto-complete score: [{scores[i]}]")
    print(f"Winning score: {statistics.median(scores)}")


if __name__ == '__main__':
    main()
