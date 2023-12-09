with open('9/data.txt') as f:
    lines = f.readlines()

def get_delta(digit1: int, digit2: int) -> int:
    return digit2 - digit1

def get_under_line(line: str):
    if "\n" in line:
        line = line.replace("\n", "")
    digit_strings = line.split(" ")
    digits = [int(digit_string) for digit_string in digit_strings]
    delta_digits = []
    for i in range(len(digits) - 1):
        delta_digits.append(get_delta(digits[i], digits[i + 1]))
    return " ".join(list(map(str, delta_digits)))

def line_is_zeros(line:str) -> bool:
    if "\n" in line:
        line = line.replace("\n", "")
    digit_strings = line.split(" ")
    digits = [int(digit_string) for digit_string in digit_strings]
    return all(digit == 0 for digit in digits)

def extrapolate_line(line: str, line_below:str) -> str:
    if "\n" in line:
        line = line.replace("\n", "")
    if "\n" in line_below:
        line_below = line_below.replace("\n", "")
    if line_is_zeros(line_below):
        line_below = line_below + " 0"
    digit_strings = line.split(" ")
    digits = [int(digit_string) for digit_string in digit_strings]
    digit_strings_below = line_below.split(" ")
    digits_below = [int(digit_string) for digit_string in digit_strings_below]
    extrapolated_value = digits_below[-1] + digits[-1]
    return " ".join(list(map(str, digits + [extrapolated_value])))

def history_extrapolated_value(line: str)->int:
    base_line = line
    sub_lines = [base_line]
    under_line = get_under_line(base_line)
    while not line_is_zeros(under_line):
        sub_lines.append(under_line)
        under_line = get_under_line(under_line)
    sub_lines.append(under_line)
    for i in range(len(sub_lines)-2, -1, -1):
        sub_lines[i] = extrapolate_line(sub_lines[i], sub_lines[i + 1])

    return int(sub_lines[0].split(" ")[-1])

def part_1():
    sum_extrapolated_values = 0
    for line in lines:
        sum_extrapolated_values += history_extrapolated_value(line)
    print(sum_extrapolated_values)

# Part 2

def extrapolate_line_backwards(line: str, line_below:str) -> str:
    if "\n" in line:
        line = line.replace("\n", "")
    if "\n" in line_below:
        line_below = line_below.replace("\n", "")
    if line_is_zeros(line_below):
        line_below = line_below + " 0"
    digit_strings = line.split(" ")
    digits = [int(digit_string) for digit_string in digit_strings]
    digit_strings_below = line_below.split(" ")
    digits_below = [int(digit_string) for digit_string in digit_strings_below]
    extrapolated_value = digits[0] - digits_below[0]
    return " ".join(list(map(str, [extrapolated_value] + digits)))

def history_extrapolated_value_backwards(line: str)->int:
    base_line = line
    sub_lines = [base_line]
    under_line = get_under_line(base_line)
    while not line_is_zeros(under_line):
        sub_lines.append(under_line)
        under_line = get_under_line(under_line)
    sub_lines.append(under_line)
    for i in range(len(sub_lines)-2, -1, -1):
        sub_lines[i] = extrapolate_line_backwards(sub_lines[i], sub_lines[i + 1])

    return int(sub_lines[0].split(" ")[0])

def part_2():
    sum_extrapolated_values = 0
    for line in lines:
        sum_extrapolated_values += history_extrapolated_value_backwards(line)
    print(sum_extrapolated_values)

part_2()