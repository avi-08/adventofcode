import os


class DIRECTIONS:
    UP = "up"
    DOWN = "down"
    FORWARD = "forward"


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        moves = f.readlines()

    moves = [(move.split(" ")[0], int(move.split(" ")[1])) for move in moves]
    return moves


def calculate_position(moves):
    x_loc, y_loc = 0, 0
    for move in moves:
        if move[0] == DIRECTIONS.FORWARD:
            x_loc += move[1]
        elif move[0] == DIRECTIONS.DOWN:
            y_loc += move[1]
        else:
            y_loc -= move[1]
    return x_loc, y_loc


def calculate_position_w_aim(moves):
    x_loc, y_loc, aim = 0, 0, 0
    for move in moves:
        if move[0] == DIRECTIONS.FORWARD:
            x_loc += move[1]
            y_loc += (aim * move[1])
        elif move[0] == DIRECTIONS.DOWN:
            aim += move[1]
        else:
            aim -= move[1]
    return x_loc, y_loc, aim


def main():
    moves = read_input()
    print(f"Total moves: {len(moves)}")

    # Part one
    pos, depth = calculate_position(moves)
    print(f"Moved long X-axis: {pos} units")
    print(f"Moved along Y-axis: {depth} units")
    print(f"Co-ordinate product: {pos * depth}")

    print("\n<=============>\n")
    # Part two
    pos, depth, aim = calculate_position_w_aim(moves)
    print(f"Moved long X-axis: {pos} units")
    print(f"Moved along Y-axis: {depth} units")
    print(f"Current aim setting: {aim} ")
    print(f"Co-ordinate product: {pos * depth}")


if __name__ == '__main__':
    main()
