import os


NEW_RESET_DAYS = 8
OLD_RESET_DAYS = 6


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        fishes = [int(x) for x in f.readlines()[0].strip().split(',')]
    
    timers = [0] * (NEW_RESET_DAYS + 1)
    for fish in fishes:
        timers[fish] += 1
    return timers, len(fishes)


def simulate_fishes(timers, initial_count, days):
    fishes = initial_count
    for _ in range(days):
        temp1, temp2 = 0, timers[NEW_RESET_DAYS]
        for i in range(NEW_RESET_DAYS, 0, -1):
            temp1 = timers[i-1]
            timers[i-1] = temp2
            temp2 = temp1
        timers[NEW_RESET_DAYS] = temp2
        timers[OLD_RESET_DAYS] += temp2
        fishes += temp2
    return fishes


def main():
    timers, initial_count = read_input('input.txt')
    print(f"Number of fishes initially: {initial_count}")
    print(f"Timer -> fish count initially: {timers}")

    # Part one
    days = 80
    n_day_count = simulate_fishes(timers, initial_count, days)
    print(f"Something's fishy! {n_day_count} fishes after {days} days")
    
    # Part two
    next_days = 256 - days
    n_day_count = simulate_fishes(timers, n_day_count, next_days)
    print(f"Bazinga!!! {n_day_count} fishes after {next_days + days} days")


if __name__ == '__main__':
    main() 
    