import os

class Node:
    def __init__(self, index, readings):
        self.index = index
        self.ones = [x.strip() for x in readings if x[index] == "1"]
        self.zeroes = [x.strip() for x in readings if x[index] == "0"]
    
    def __str__(self):
        return f"{{Index: {self.index}, Zeroes: {self.zeroes}, Ones: {self.ones} }}"


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.curdir, file_name)

    with open(file_path, 'r') as f:
        readings = f.readlines()

    return readings


def binary_to_decimal(binary_string):
    return int(binary_string, 2)


def get_bit_diff(readings):
    bit_count = [0 for i in range(len(readings[0]) - 1)]
    for reading in readings:
        for index, bit in enumerate(reading.strip()):
            delta = 1 if bit == "1" else -1
            bit_count[index] += delta
    
    return bit_count
    

def get_gamma_epsilon_rate_binary(readings):
    bit_count = [0 for i in range(len(readings[0]) - 1)]
    for reading in readings:
        for index, bit in enumerate(reading.strip()):
            delta = 1 if bit == "1" else -1
            bit_count[index] += delta
    
    gamma = ''.join(['0' if x < 0 else '1' for x in bit_count])
    epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])

    return gamma, epsilon

def get_o2_generator_rating(readings):
    n = []
    temp = readings
    for i in range(len(readings[0]) - 1):
        n.append(Node(index=i, readings=temp))
        temp = n[-1].zeroes if (len(n[-1].zeroes) > len(n[-1].ones)) else n[-1].ones
        if (len(n[-1].zeroes) + len(n[-1].ones)) == 1:
            break
    print(n[-1])
    if (len(n[-1].zeroes) + len(n[-1].ones)) == 1:
        return n[-1].zeroes[0] if len(n[-1].zeroes) == 1 else n[-1].ones[0]
    return n[-1].ones[0]


def get_co2_scrubber_rating(readings):
    n = []
    temp = readings
    for i in range(len(readings[0]) - 1):
        n.append(Node(index=i, readings=temp))
        temp = n[-1].zeroes if (len(n[-1].zeroes) <= len(n[-1].ones)) else n[-1].ones
        if (len(n[-1].zeroes) + len(n[-1].ones)) == 1:
            break
    print(n[-1])
    if (len(n[-1].zeroes) + len(n[-1].ones)) == 1:
        return n[-1].zeroes[0] if len(n[-1].zeroes) == 1 else n[-1].ones[0]
    return n[-1].zeroes[0]


def get_power_consumption(gamma_rate, epsilon_rate):
    return gamma_rate * epsilon_rate


def get_life_support_rating(o2_generator_rating, co2_scrubber_rating):
    return o2_generator_rating * co2_scrubber_rating


def main():
    readings = read_input()
    print(f"Total readings: {len(readings)}")
    
    # Part one
    gamma, epsilon = get_gamma_epsilon_rate_binary(readings)
    gamma_rate, epsilon_rate = binary_to_decimal(gamma), binary_to_decimal(epsilon)
    print(f"Gamma Rate: binary [{gamma}] decimal [{gamma_rate}]")
    print(f"Epsilon Rate: binary [{epsilon}] decimal [{epsilon_rate}]")
    power = get_power_consumption(gamma_rate, epsilon_rate)
    print(f"Power consumption: {power} units")

    print("\n<=============>\n")
    # Part two
    o2, co2 = get_o2_generator_rating(readings), get_co2_scrubber_rating(readings)
    o2_generator_rating, co2_scrubber_rating = binary_to_decimal(o2), binary_to_decimal(co2)
    print(f"O2 generation rate: binary [{o2}] decimal [{o2_generator_rating}]")
    print(f"CO2 scrubbing rate: binary [{co2}] decimal [{co2_scrubber_rating}]")
    life_support_rating = get_life_support_rating(o2_generator_rating, co2_scrubber_rating)
    print(f"Life support rating: {life_support_rating}")


if __name__ == '__main__':
    main()
