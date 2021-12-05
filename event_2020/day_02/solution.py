import os
import dataclasses

@dataclasses.dataclass
class Policy:
    min_occurrence: int = 0
    max_occurrence: int = 0
    character: str = ""
    
    def __str__(self):
        return f'{{"{self.character}" should occur atleast {self.min_occurrence} times and atmost {self.max_occurrence} times}}'
    

@dataclasses.dataclass
class NewPolicy:
    positions: list = dataclasses.field(default_factory=list)
    character: str = ""
    
    def __str__(self):
        return f'{{"{self.character}" should occur at exactly one of these positions {self.positions}}}'


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    passwords = []
    for line in lines:
        a, b, c = line.strip().split()
        policy = Policy()
        new_policy = NewPolicy()
        policy.min_occurrence, policy.max_occurrence = [int(x) for x in a.split('-')]
        new_policy.positions = [int(x) for x in a.split('-')]
        policy.character = b[:-1]
        new_policy.character = b[:-1]
        passwords.append((policy, new_policy, c))
        
    return passwords


def is_password_valid(password, policy):
    if type(policy) == Policy:
        count = 0
        for ch in password:
            if ch == policy.character:
                count += 1
        return count in range(policy.min_occurrence, policy.max_occurrence + 1)
    elif type(policy) == NewPolicy:
        return (password[policy.positions[0] - 1] == policy.character) ^ (password[policy.positions[1] - 1] == policy.character)


def main():
    passwords = read_input()
    print(f'Total inputs: {len(passwords)}')
    
    # Part one
    valid_count = 0
    for policy, _, password in passwords:
        if is_password_valid(password=password, policy=policy):
            valid_count += 1
    print(f"Valid passwords found: {valid_count}")    
    
    print("\n<=============>\n")
    # Part two
    valid_count = 0
    for _, policy, password in passwords:
        if is_password_valid(password=password, policy=policy):
            valid_count += 1
    print(f"Valid passwords found: {valid_count}") 


if __name__ == '__main__':
    main() 
    