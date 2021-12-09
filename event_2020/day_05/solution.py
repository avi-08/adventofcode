import os
from enum import Enum


class Partition(str, Enum):
    F = "F"
    B = "B"
    L = "L"
    R = "R"


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        boarding_passes = [x.strip() for x in f.readlines()]

    return boarding_passes


def get_beg_end(partition: Partition, beg, end):
    if partition in (Partition.F, Partition.L):
        end = beg + (end - beg) // 2
    else:
        beg = beg + 1 + (end - beg) // 2
    return beg, end


def get_seat_id(boarding_pass: str):
    row_beg, row_end  = 0, 127
    for ch in boarding_pass[:7]:
        row_beg, row_end = get_beg_end(ch, row_beg, row_end)
    
    col_beg, col_end = 0, 7
    for ch in boarding_pass[7:]:
        col_beg, col_end = get_beg_end(ch, col_beg, col_end)
    
    seat_id = row_end * 8 + col_end
    return seat_id


def main():
    boarding_passes = read_input()
    print(f"Total boarding passes: {len(boarding_passes)}")

    highest_seat = 0
    occupied_seats = []
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass)
        highest_seat = max(highest_seat, seat_id)
        occupied_seats.append(seat_id)
    print(f"Hishest seat ID yet: {highest_seat}")
    
    occupied_seats.sort()
    for index, _ in enumerate(occupied_seats):
        if occupied_seats[index] - occupied_seats[index-1] == 2:
            my_seat =  occupied_seats[index] - 1
            break
    
    print(f"Your seat ID [{my_seat}]. Buckle up fast!!")
    
  
if __name__ == '__main__':
    main()
