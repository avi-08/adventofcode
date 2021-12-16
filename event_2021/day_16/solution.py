import os


HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return lines


def get_bin_from_hex(hex_num):
    b_num = ''
    for ch in hex_num:
        b_num += HEX_TO_BIN[ch]
    return b_num


def split_header_content(packet):
    version, type_id, content = packet[:3], packet[3:6], packet[6:]
    return int(version, 2), int(type_id, 2), content


def read_literal(content):
    splits = []
    index = 0
    last_group = False
    while not last_group:
        if content[index] == '0':
            last_group = True
        splits.append(content[index+1:index+5])
        index += 5
    return splits


def split_operator_content(content):
    i = content[0]
    bit_start = 0
    total_bit_length = None
    total_sub_packets = None
    if i == '0':
        bit_start = 16
        total_bit_length = int(content[1:bit_start], 2)
    elif i == '1':
        bit_start = 12
        total_sub_packets = int(content[1:bit_start], 2)
    
    assert (total_bit_length is None) ^ (total_sub_packets is None)
    return total_bit_length, total_sub_packets, content[bit_start:]


def packet_operation(type_id, values):
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        prod = 1
        for x in values:
            prod *= x
        return prod
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    elif type_id == 5:
        return 1 if values[0] > values[1] else 0
    elif type_id == 6:
        return  1 if values[0] < values[1] else 0
    elif type_id == 7:
        return  1 if values[0] == values[1] else 0


def decode_packet(packet):
    version_sum = 0
    version, type_id, content = split_header_content(packet)
    type_str = "LITERAL" if type_id == 4 else "OPERATOR"
    # print(f"Version: {version}; Type ID: {type_id}({type_str})")
    version_sum += version
    
    if type_str == "LITERAL":
        splits = read_literal(content)
        # print(f"Splits found: {len(splits)}")
        literal_value = int(''.join(splits), 2)
        # print(f"Literal value: {literal_value}")
        bits_seen = (len(splits) * 5)  + 6
        return version_sum, literal_value, bits_seen
    
    total_bit_length, total_sub_packets, sub_content = split_operator_content(content)
    # print(f"Total bit length: {total_bit_length}")
    # print(f"Total sub packets: {total_sub_packets}")
    # print(f"Sub content: {sub_content}")
    bits_seen, packets_seen = 0, 0
    values = []
    if total_bit_length:
        while bits_seen != total_bit_length:
            ver, literal_value, bits = decode_packet(sub_content[bits_seen:])
            bits_seen += bits
            version_sum += ver
            values.append(literal_value)
            # print(f"Bits seen: {bits_seen}")
        bits_seen += 22
    elif total_sub_packets:
        while packets_seen != total_sub_packets:
            ver, literal_value, bits = decode_packet(sub_content[bits_seen:])
            packets_seen += 1
            bits_seen += bits
            version_sum += ver
            values.append(literal_value)
            # print(f"Packets seen: {packets_seen}")
        bits_seen += 18
    return version_sum, packet_operation(type_id, values), bits_seen
    

def main():
    hex_num = read_input('input.txt')[0]
    print(f"Length of input hexadecimal: {len(hex_num)}")
    
    packet = get_bin_from_hex(hex_num)
    print(f"Length of binary equivalent: {len(packet)}")
    assert len(packet) == len(hex_num) * 4
    
    # Part one
    data = decode_packet(packet)
    print("============================")
    print(f"Version sum: {data[0]}")
    # Part two
    print(f"Expression Value: {data[1]}")
    print(f"Bits seen: {data[2]}")
    assert len(packet) >= data[2]


if __name__ == '__main__':
    main()