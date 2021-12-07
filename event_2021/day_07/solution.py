import os
import statistics


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        positions = [int(x) for x in f.readlines()[0].strip().split(',')]
        
    return positions


def get_fuel_spent(positions, target_position):
    fuel = 0
    for p in positions:
        fuel += abs(p - target_position)
        
    return fuel


def get_fuel_spent_new(positions, target_position):
    fuel = 0
    for p in positions:
        n = abs(p - target_position)
        fuel += (n * (n + 1) // 2)
        
    return fuel


def main():
    positions = read_input('input.txt')
    print(f"Total crabs: {len(positions)}")
    
    # Part one
    target_position = int(statistics.median(positions))
    fuel_spent = get_fuel_spent(positions, target_position)
    print(f"Target position: {target_position}. Fuel spent to realign: {fuel_spent}")
    
    print("\n<=============>\n")
    # Part two
    target_position = int(statistics.mean(positions))
    target_position_b = round(statistics.mean(positions))
    fuel_spent = get_fuel_spent_new(positions, target_position)
    if target_position_b != target_position:
        fuel_spent_b = get_fuel_spent_new(positions, target_position_b)
        if fuel_spent > fuel_spent_b:
            target_position = target_position_b
            fuel_spent = fuel_spent_b
    
    print(f"Target position: {target_position}. Fuel spent to realign: {fuel_spent}")


if __name__ == '__main__':
    main() 
