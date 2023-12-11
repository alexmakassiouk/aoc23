import re

lines = open('3/data.txt','r').read().split('\n')


def get_next_symbol(y, x):
    for i in range(x+1, len(lines[y])):
        if lines[y][i] != '.' and not lines[y][i].isalnum():
            return y, i
    for i in range(y+1, len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.' and not lines[i][j].isalnum():
                return i, j
    return None
            
def get_left_number(y, x):
    evaluated_string = lines[y][0:x]
    if evaluated_string == "":
        return None
    if not evaluated_string[-1].isdigit():
        return None
    else:
        return [int(evaluated_string.split(".")[-1])]

def get_right_number(y, x):
    evaluated_string = lines[y][x+1:]
    if evaluated_string == "":
        return None
    if not evaluated_string[0].isdigit():
        return None
    else:
        return [int(evaluated_string.split(".")[0])]

def string_contains_number(string):
    result = ""
    if not bool(re.search(r'\d', string)):
        return None
    else:
        if string[0].isdigit():
            result+="L"
        if string[1].isdigit():
            result+="U"
        if string[-1].isdigit():
            result+="R"
        if string.isdigit():
            result = "ALL"
        return result


def get_up_numbers(y, x):
    if y == 0:
        return None
    if x == 0:
        evaluated_string = lines[y-1][x:x+2]
    else:
        evaluated_string = lines[y-1][x-1:x+2]
    numbers = []
    if not string_contains_number(evaluated_string):
        return None
    else:
        if string_contains_number(evaluated_string) == "ALL":
            return [int(evaluated_string)]
        else:
            if "U" in string_contains_number(evaluated_string) and "L" in string_contains_number(evaluated_string):
                numbers.extend(get_left_number(y-1, x+1))
            elif "L" in string_contains_number(evaluated_string):
                numbers.extend(get_left_number(y-1, x))
            if "U" in string_contains_number(evaluated_string) and "R" in string_contains_number(evaluated_string):
                numbers.extend(get_right_number(y-1, x-1))
            elif "R" in string_contains_number(evaluated_string):
                numbers.extend(get_right_number(y-1, x))
            # elif "U" in string_contains_number(evaluated_string):
            #     numbers.extend(get_right_number(y-1, x-1))
    return numbers

def get_down_numbers(y,x):
    if y == len(lines)-1:
        return None
    evaluated_string = lines[y+1][x-1:x+2]
    numbers = []
    if not string_contains_number(evaluated_string):
        return None
    else:
        if string_contains_number(evaluated_string) == "ALL":
            return [int(evaluated_string)]
        else:
            if "U" in string_contains_number(evaluated_string) and "L" in string_contains_number(evaluated_string):
                numbers.extend(get_left_number(y+1, x+1))
            elif "L" in string_contains_number(evaluated_string):
                numbers.extend(get_left_number(y+1, x))
            if "U" in string_contains_number(evaluated_string) and "R" in string_contains_number(evaluated_string):
                numbers.extend(get_right_number(y+1, x-1))
            elif "R" in string_contains_number(evaluated_string):
                numbers.extend(get_right_number(y+1, x))
            # elif "U" in string_contains_number(evaluated_string):
            #     numbers.extend(get_right_number(y+1, x-1))
    return numbers


y = 0
x = 0
part_numbers = []
while get_next_symbol(y,x) is not None:
    if y == 130:
        pass
    symbol = get_next_symbol(y,x)
    if get_up_numbers(symbol[0], symbol[1]) is not None:
        part_numbers.extend(get_up_numbers(symbol[0], symbol[1]))
    if get_down_numbers(symbol[0], symbol[1]) is not None:
        part_numbers.extend(get_down_numbers(symbol[0], symbol[1]))
    if get_left_number(symbol[0], symbol[1]) is not None:
        part_numbers.extend(get_left_number(symbol[0], symbol[1]))
    if get_right_number(symbol[0], symbol[1]) is not None:
        part_numbers.extend(get_right_number(symbol[0], symbol[1]))
    y, x = symbol[0], symbol[1]

print(sum(part_numbers))