import os


ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        energy_levels = [[int(x) for x in line.strip()] for line in f.readlines()]

    return energy_levels


def is_valid_index(x, y, x_max, y_max):
    return x in range(0, x_max+1) and y in range(0, y_max+1)


def update_energy(energy_levels, x, y):
    flashes = 0
    x_max, y_max = len(energy_levels) - 1 , len(energy_levels[0]) - 1 
    for a, b in ADJACENTS:
        p, q = x+a, y+b
        # We don't want to update already flashed octopus or its neighbours
        if is_valid_index(p, q, x_max, y_max) and energy_levels[p][q] > 0:
            energy_levels[p][q] += 1
            if energy_levels[p][q] > 9:
                energy_levels[p][q] = 0
                flashes += (update_energy(energy_levels, p, q) + 1)
    return flashes


def get_flash_count(energy_levels, step_start, step_end):
    flashes = 0
    flashy_step = 0
    rows, cols = len(energy_levels), len(energy_levels[0])
    for step in range(step_start, step_end+1):
        # First, increase energy levels of all octopuses by 1
        for x in range(rows):
            for y in range(cols):
                energy_levels[x][y] += 1
        
        # Now, check for the flash spread and update energy levels
        for x in range(rows):
            for y in range(cols):
                if energy_levels[x][y] > 9:
                    energy_levels[x][y] = 0
                    flashes += (update_energy(energy_levels, x, y) + 1)

        if flashy_step == 0:
            total = 0
            for x in range(rows):
                total += sum(energy_levels[x])
            if total == 0:
                flashy_step = step
    return flashes, flashy_step


def main():
    energy_levels = read_input('input.txt')
    print(f"Octopuses grid size: {len(energy_levels)} X {len(energy_levels[0])}")
    
    # Part one
    steps = 100
    flashes, flashy_step = get_flash_count(energy_levels, 1, steps)
    print(f"Flashes after {steps} steps: {flashes}")
    
    # Part two
    while flashy_step == 0:
        flashes, flashy_step = get_flash_count(energy_levels, steps+1, steps+100)
        steps += 100
    print(f"First step with synchronised flashes: {flashy_step}. Oh my eyes, my eyes!!!")


if __name__ == '__main__':
    main()
