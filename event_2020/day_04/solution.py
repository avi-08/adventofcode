import os
from typing import List


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    passports = []
    index = 0
    while index  < len(lines):
        details = dict()
        while index < len(lines) and lines[index] != '\n':
            for pair in lines[index].strip().split():
                k, v = pair.split(":")
                details[k] = v
            index += 1
        passports.append(details)
        index += 1
    
    return passports


def validate_byr(byr):
    try:
        result = byr and int(byr) in range(1920, 2003)
    except Exception:
        result = False
    return result


def validate_iyr(iyr):
    try:
        result = iyr and int(iyr) in range(2010, 2021)
    except Exception:
        result = False
    return result


def validate_eyr(eyr):
    try:
        result = eyr and int(eyr) in range(2020, 2031)
    except Exception:
        result = False
    return result


def validate_hgt(hgt):
    try:
        unit = hgt[-2:]
        if unit == "cm":
            result = int(hgt[:-2]) in range(150, 194)
        elif unit == "in":
            result = int(hgt[:-2]) in range(59, 77)
        else:
            result = False
    except Exception:
        result = False
    return result


def validate_hcl(hcl):
    try:
        if hcl and hcl[0] == "#" and len(hcl) == 7:
            int(hcl[1:], 16)
            result = True
        else:
            result = False  
    except Exception:
        result = False
    return result


def validate_ecl(ecl):
    valid_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return ecl and ecl in valid_colors


def validate_pid(pid):
    try:
        if pid and len(pid) == 9:
            int(pid)
            result = True
        else:
            result = False
    except Exception:
        result = False
    return result


def validate_cid(cid):
    return True


def find_valid_passports(passports: List[dict]) -> int:
    REQUIRED_FIELDS = ("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt")
    valid_passports = len(passports)
    for passport in passports:
        p_keys = passport.keys()
        for field in REQUIRED_FIELDS:
            if field not in p_keys:
                valid_passports -= 1
                break
    
    return valid_passports


def find_valid_passports_new(passports: List[dict]) -> int:
    VALIDATORS = {
        "ecl": validate_ecl,
        "pid": validate_pid,
        "eyr": validate_eyr,
        "hcl": validate_hcl,
        "byr": validate_byr,
        "iyr": validate_iyr,
        "hgt": validate_hgt,
        "cid": validate_cid
        }
    count = 0
    valid_passports = len(passports)
    for passport in passports:
        for key in  VALIDATORS.keys():
            if not VALIDATORS[key](passport.get(key, None)):
                valid_passports -= 1
                break
    return valid_passports


def main():
    passports = read_input('input.txt')
    print(f"Total passports in batch: {len(passports)}") 
    
    # Part one
    valid_passports = find_valid_passports(passports)
    print(f"Found {valid_passports} valid passports out of {len(passports)}.")
    
    # Part two
    valid_passports = find_valid_passports_new(passports)
    print(f"Upon stricter checking, found {valid_passports} valid passports out of {len(passports)}.")


if __name__ == '__main__':
    main() 
    