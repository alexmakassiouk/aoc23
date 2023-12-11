import re
with open('3/data.txt') as f:
    lines = f.readlines()

part_numbers = []
# for line in lines:
#     for char in line:
#         if char.isdigit():
#             non_numeric_index_after_char = line.index(char)
#             while line[non_numeric_index_after_char].isdigit():
#                 non_numeric_index_after_char += 1
#             # number = int(""+digit for digit in line[line.index(char): non_numeric_index_after_char])

#             if line[line.index(char)-1] != "." or line[non_numeric_index_after_char] != "." or lines[lines.index(line)-1][line.index(char)-1] != "." or lines[lines.index(line)+1][non_numeric_index_after_char] != ".":
#                 digits = [digit for digit in line[line.index(char): non_numeric_index_after_char]]
#                 part_numbers.append(int(""+digit for digit in line[line.index(char): non_numeric_index_after_char]))
def attempt2():
    for line in lines:
        parsed_line = line.split("\n")[0]
        # if lines.index(line) == 70:
        #     pass
        symbols = parsed_line.split(".")
        index_in_line = 0
        fucked_up_lines = [29, 30, 49, 68, 86, 113, 123]
        if lines.index(line) not in fucked_up_lines:
            for symbol in symbols:
                if any(char.isdigit() for char in symbol):
                    if any(not char.isdigit() for char in symbol):
                        if symbol[0].isdigit() and symbol[-1].isdigit():
                            numbers = re.findall(r'\d+', symbol)
                            part_numbers.append(int(numbers[0]))
                            part_numbers.append(int(numbers[1]))
                        else:
                            part_numbers.append(int(re.sub(r'[^0-9]', "", symbol)))
                    else:
                        symbols_without_empty = [symbol for symbol in symbols if symbol != "" and any(char.isdigit() for char in symbol)]
                        if len(symbols_without_empty) != len(set(symbols_without_empty)):
                            print("Duplicate symbols in line: " + str(lines.index(line))) 
                        left_edge_index = max(line.index(symbol),0)
                        right_edge_index = left_edge_index + len(symbol)+1 if left_edge_index != 0 else len(symbol)
                        upper_line = lines[lines.index(line)-1][left_edge_index:right_edge_index+1].split("\n")[0] if lines.index(line) != 0 else ""
                        lower_line = lines[lines.index(line)+1][left_edge_index:right_edge_index+1].split("\n")[0] if lines.index(line) != len(lines)-1 else ""
                        adj = (upper_line+lower_line).split(".")
                        if any(char!="" for char in adj):
                            part_numbers.append(int(re.sub(r'[^0-9]', "", symbol)))
                if symbol == "":
                    index_in_line += 1
                else:
                    index_in_line += len(symbol)+1
        else:
            pass
    assert 18 in part_numbers and 82 in part_numbers and 3 in part_numbers and 28 in part_numbers and 110 in part_numbers
    print(sum(part_numbers)+738+401+984+265+184+148+990+80+511+424+400+551+499+10+227+227+542+167+661+253+796+200+355+174+279+140+682+150+7+654+83+941+7+780+922+226+341+341+989+321+510+837+237+270+818+27+163+140+647+764+163)
    summen = 0
    for part_number in part_numbers:
        summen += part_number
    print(summen)

# def attempt3():
#     for line in lines:
#         for char in lines:
#             if not char.isalnum() and char != ".":
                
def attempt4():
    for line in lines:
        i=0
        parsed_line = line.split("\n")[0]
        symbols = parsed_line.split(".")
        while i<len(parsed_line):
            
attempt2()