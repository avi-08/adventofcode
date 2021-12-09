import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    groups = []
    index = 0
    while index < len(lines):
        groups.append([])
        while index < len(lines) and lines[index] != '':
            groups[-1].append(lines[index])
            index += 1
        index += 1
    return groups


def get_distinct_answered_questions(group):
    return len({x for x in ''.join(group)})


def get_common_answered_questions(group):
    common = None
    for answer in group:
        if common is None:
            common = {x for x in answer}
        else:
            common = common.intersection(x for x in answer)
    return len(common)


def main():
    groups = read_input('input.txt')
    print(f"Total groups: {len(groups)}")

    # Part one
    distinct_ans = 0
    for group in groups:
        distinct_ans += get_distinct_answered_questions(group)
    print(f"Total distinct answered questions: {distinct_ans}")
    
    # Part two
    common_ans = 0
    for group in groups:
        common_ans += get_common_answered_questions(group)
    print(f"Total common answered questions: {common_ans}")
        

if __name__ == '__main__':
    main()
