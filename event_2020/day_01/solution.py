import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        nums = [int(line.strip()) for line in f.readlines()]
    
    return nums


def get_two_sum(nums, total, seen=set()):
    for num in nums:
        target = total - num
        if target in seen:
            return (num, target)
        seen.add(num)
    
    return (None, None)


def get_three_sum(nums, total, seen=set()):
    for num in nums:
        target = total - num
        x, y = get_two_sum(nums, target, seen)
        if x and y:
            return (x, y, num)
        seen.add(num)
    
    return (None, None, None)


def main():
    nums = read_input()
    print(f'Total numbers: {len(nums)}')
    
    # Part one
    total = 2020
    x, y = get_two_sum(nums, total)
    print(f"Numbers that add upto {total}: {x} and {y}")
    print(f"x * y = {x * y}")
    
    print("\n<=============>\n")
    # Part two
    x, y, z = get_three_sum(nums, total)
    print(f"Numbers that add upto {total}: {x}, {y} and {z}")
    print(f"x * y * z = {x * y * z}")


if __name__ == '__main__':
    main() 
    