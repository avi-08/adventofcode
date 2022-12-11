import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    index = 0
    scanned_beacons = []
    while index < len(lines):
        scanned_beacons.append([])
        index += 1
        while index < len(lines) and lines[index] != '':
            scanned_beacons[-1].append([int(x) for x in lines[index].split(',')])
            index += 1
        index += 1
    return lines


def main():
    lines = read_input('sample.txt')
    
    # Part one
    
    # Part two
    pass


if __name__ == '__main__':
    main()