import os


def parse(rule_string: str, rules: dict):
    rule = rule_string.strip('.').split(' bags contain ')
    if rule[1] == 'no other bags':
        if "None" not in rules:
            rules["None"] = dict()
        rules["None"][rule[0]] = None
    else:
        target = rule[1].split(', ')
        for content in target:
            temp = content.split()
            limit = int(temp[0])
            color = ' '.join(temp[1:-1])
            if color not in rules:
                rules[color] = dict()
            rules[color][rule[0]] = limit
            

def parse_new(rule_string: str, rules: dict):
    rule = rule_string.strip('.').split(' bags contain ')
    if rule[1] == 'no other bags':
        rules[rule[0]] = None
    else:
        target = rule[1].split(', ')
        for content in target:
            temp = content.split()
            limit = int(temp[0])
            color = ' '.join(temp[1:-1])
            if rule[0] not in rules:
                rules[rule[0]] = dict()
            rules[rule[0]][color] = limit
    

def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    rules, rules_new = dict(), dict()
    for rule_string in lines:
        parse(rule_string, rules)
        parse_new(rule_string, rules_new)
    
    return rules, rules_new


def visit(rules, node, visited):
    if not rules[node]:
        return 0
    visited[node] = True
    total = 0
    for neighbour, value in rules[node].items():
        temp = visit(rules, neighbour, visited)
        if temp == 0:
            total += value
        else:
            total += (value * temp)
    print(f"Total for node: {node} is {total}")
    return total
    
    

def find_valid_contianers(rules, bag_color, visited):
    if bag_color in visited or bag_color not in rules:
        return
    for color in rules[bag_color].keys():
        find_valid_contianers(rules, color, visited)
        visited.add(color)
    return
        
        
def main():
    rules, rules_new = read_input('input.txt')
    print(f"Total rules(and hence bag colors): {len(rules)}")
    for k, v in rules.items():
        print(f"{k}: {v}")
    print('-=-=-=-=--==-=-=-==-')
    for k, v in rules_new.items():
        print(f"{k}: {v}")
        
    # print(f"Root node: {find_root_node(rules)}")
    # Part one
    bag_color = "shiny gold"
    visited = set()
    find_valid_contianers(rules, bag_color, visited)
    print(f"Valid containers for [{bag_color}] bag: {len(visited)}")
    
    # Part two
    visited = {color: False for color in rules_new.keys()}
    count = visit(rules_new, bag_color, visited) + sum(rules_new[bag_color].values())
    print(f"Total contained bags for [{bag_color}] bag: {count}")
    print(f"Total rules(and hence bag colors): {len(rules_new)}")
    

if __name__ == '__main__':
    main()