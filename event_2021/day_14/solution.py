import os
from collections import Counter


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    template = lines[0]
    rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in lines[2:]}

    return template, rules


def insert(template, rules):
    temp = ''
    for i in range(len(template) - 1):
        mid = rules[template[i:i+2]]
        temp += f"{template[i]}{mid}"
    temp += template[-1]
    return temp


def count_pairs(template, rules, steps):
    count = {}
    for i in range(len(template) - 1):
        count[template[i:i+2]] = count.get(template[i:i+2], 0) + 1
    
    for _ in range(steps):
        temp = dict()
        for pair in count.keys():
            x, y = (pair[0] + rules[pair]), (rules[pair] + pair[1])
            temp[x] = temp.get(x, 0) + count[pair]
            temp[y] = temp.get(y, 0) + count[pair]
        
        count = temp
    
    chars = {}
    for pair in count.keys():
        x, y = pair[0], pair[1]
        chars[x] = chars.get(x, 0) + count[pair]
        chars[y] = chars.get(y, 0) + count[pair]
    
    chars[template[0]] += 1
    chars[template[-1]] += 1
    
    return {k: v // 2 for k, v in chars.items()}


def main():
    template, rules = read_input('input.txt')
    print(f"Polymer template: {template}")
    print(f"Total rules: {len(rules)}")
    temp = template
    
    # Part one
    for i in range(10):
        temp = insert(temp, rules)
    print(f"After step{i} len{len(temp)}: {temp}")
    
    count = Counter(temp)
    print(count)
    min_e = min(count.values())
    max_e = max(count.values())
    print(f"Diff: {max_e - min_e}")
    
    # Part two
    pair_counts = count_pairs(template, rules, 40)
    print(pair_counts)
    min_e = min(pair_counts.values())
    max_e = max(pair_counts.values())
    print(f"Diff: {max_e - min_e}")


if __name__ == '__main__':
    main()
