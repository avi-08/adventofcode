import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines


def main():
    lines = read_input('sample.txt')
    
    # Part one
    
    # Part two
    pass


if __name__ == '__main__':
    main()