import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    input_split = lines[0].strip('target area: ').split(', ')
    x = [int(p) for p in input_split[0][2:].split('..')]
    y = [int(p) for p in input_split[1][2:].split('..')]
    return x, y


def is_target_acquired(xt, yt, x_range, y_range):
    return (x_range[0] <= xt<= x_range[1]) and (y_range[0]<= yt <= y_range[1])


def trace_path(x_range, y_range):
    y_max, count = 0, 0
    for y in range(y_range[0],1-y_range[0]):
        for x in range(x_range[1]+1):
            xt, yt, height = [0] * 3
            for t in range(999):
                yt += y - t
                xt += max(x - t, 0)
                height = max(height, yt)
                if is_target_acquired(xt, yt, x_range, y_range):
                    count += 1
                    y_max = max(height, y_max)
                    break
    return y_max, count


def main():
    x_range, y_range = read_input('input.txt')
    print(f"Target area bound between: {x_range[0]} to {x_range[1]} on the x-axis and {y_range[0]} to {y_range[1]} on the y-axis")
    
    y_max, count = trace_path(x_range, y_range)
    
    # Part one
    print(f"Maximum height attained: {y_max}")
    
    # Part two
    print(f"Total available launch velocities: {count}")


if __name__ == '__main__':
    main()
