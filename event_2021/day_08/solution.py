import os
import dataclasses
from typing import List


@dataclasses.dataclass
class IOPattern:
    ip: List[str]
    op: List[str]
    
    def __str__(self):
        return f"input: {self.ip}; Output: {self.op}"


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        display_patterns = f.readlines()
        
    patterns = []
    for pattern in display_patterns:
        ip, op = pattern.strip().split(' | ')
        io = IOPattern(ip=ip.split(), op=op.split())
        patterns.append(io)

    return patterns


def get_digit_appearances(patterns: List[IOPattern], accepted_patterns: List[int]):
    count = 0
    for pattern in patterns:
        for op in pattern.op:
            if len(op) in accepted_patterns:
                count += 1

    return count


def decode_segment_wirings(pattern: IOPattern):
    """Decode the segment wiring and return the identifiers of each segment of the seven-segment display

    Args:
        pattern (IOPattern): [description]

    Returns:
        segments (list[str]) : A list of identifiers of the segment indicating
        
               ____
              |  0 |
            5 |    | 1
               ----         => ["a", "b", "c", "d", "e", "f", "g"]
              |  6 |    index:   0    1    2    3    4    5    6
            4 |    | 2
               ----
                 3
    """
    segment_counts = dict()
    for p in pattern.ip:
        if len(p) not in segment_counts:
            segment_counts[len(p)] = []
        segment_counts[len(p)].append({x for x in p})
    
    
    segments = [None] * 7
    temp = ["a", "b", "c", "d", "e", "f", "g"]
        
    # 2 segments can only represent 1; Correct order will be decided later
    segments[1], segments[2] = segment_counts[2][0]
    temp.remove(segments[1])
    temp.remove(segments[2])
    # 3 segments can only represent 7; Only other segment than the ones representing '1'
    segments[0] = (segment_counts[3][0] - segment_counts[2][0]).pop()
    temp.remove(segments[0])
    
    # 6 segments can represent either 0, 9 or 6; Only '0' has all segments of '1' and missing segment #6 that is available in '4'
    # Here we identify 2 segment identifiers: #5 and #6
    for p in segment_counts[6]:
        diff = segment_counts[4][0] - segment_counts[2][0] - p
        if len(diff) == 1:
            segments[6] = diff.pop()
            temp.remove(segments[6])
            segment_counts[6].remove(p)
            break
    segments[5] = (segment_counts[4][0] - {segments[6], segments[1], segments[2]}).pop()
    temp.remove(segments[5])
    
    # 5 segments can represent either 2, 3 or 5; Out if these, only '5' has the active segment #5
    # We use this to identify the correct ordering of segments for displying '1'
    for p in segment_counts[5]:
        diff =  p - {segments[5]}
        if len(diff) == 4:
            diff2 = segment_counts[2][0] - p
            if segments[1] != diff2.pop():
                segments[1], segments[2] = segments[2], segments[1]
            break            
    
    # 6 segments can represent either 0, 9 or 6 (here we only consider 6 and 9); '9' has all the segments of '1'
    # Here we identify 2 segment identifiers: #4 and #3
    for p in segment_counts[6]:
        diff = segment_counts[2][0] - p
        if len(diff) == 0:
            segments[4] = (segment_counts[7][0] - p).pop()
            temp.remove(segments[4])
            segments[3] = temp[0]
            break
    
    return segments


def decode_segment_value(string, segments):
    on = len(string)
    if on == 2:
        return 1
    elif on == 3:
        return 7
    elif on == 4:
        return 4
    elif on == 7:
        return 8
    elif on == 6:
        if segments[1] not in string:
            return 6
        elif segments[6] not in string:
            return 0
        return 9
    else:
        if segments[2] not in string:
            return 2
        elif segments[1] not in string:
            return 5
        return 3


def decode_display_number(pattern: IOPattern):
    segments = decode_segment_wirings(pattern=pattern)
    num = 0
    for i, x in enumerate(pattern.op[::-1]):
        num += (decode_segment_value(x, segments) * (10 ** i))
    print(pattern.op, num)
    return num


def main():
    patterns = read_input()
    print(f"Total patterns noted: {len(patterns)}")
    
    # Part one
    accepted_patterns = [2, 4, 3, 7]
    digit_appearances = get_digit_appearances(patterns, accepted_patterns)
    print(f"Found {digit_appearances} digit appearances of [1, 4, 7, 8] in given output patterns.")
    
    print("\n<=============>\n")
    # Part two
    total_value = 0
    for pattern in patterns:
        total_value += decode_display_number(pattern)
    
    print(f"Sum of all output values: {total_value}")
    
    
if __name__ == '__main__':
    main() 
