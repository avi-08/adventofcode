import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.curdir, file_name)

    with open(file_path, 'r') as f:
        depths = f.readlines()

    depths = [int(depth) for depth in depths]
    return depths


def find_increased_depths(depths):
    increased = 0
    pre = depths[0]

    for depth in depths[1:]:
        if depth > pre:
            increased += 1
        pre = depth
    
    return increased


def find_increased_window_depths(depths, window_size=1):
    window_end = len(depths) - window_size
    pre = sum(depths[:window_size])
    increased = 0
    for index in range(0, window_end):
        curr = pre - depths[index] + depths[index+window_size]
        if curr > pre:
            increased += 1
        pre = curr
    
    return increased


def main():
    depths = read_input()
    total_depths = len(depths)
    print(f"Input Depths: {total_depths}")

    # Part one
    increased = find_increased_depths(depths)
    print(f"Depth increased {increased} times out of {total_depths}")

    print("\n<=============>\n")
    # Part two
    window = 3
    increased_window = find_increased_window_depths(depths, window)
    print(f"Depth increased within window of {window} readings: {increased_window} times out of {total_depths-window+1}")


if __name__ == '__main__':
    main()
