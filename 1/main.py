with open('1/data.txt') as f:
    lines = f.readlines()

def get_number(line):
    all_numbers = [int(character) for character in line if character.isdigit()]
    two_digit_number = int(''.join([str(all_numbers[0]), str(all_numbers[-1])]))
    return two_digit_number

numbers = []

for line in lines:
    numbers.append(get_number(line))
print(sum(numbers))

# Part 2 (jeezus christ...)

spelled_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_part2 = []
for line in lines:
    line = line.split("\n")[0]
    parsed_line = ""
    for i in range(len(line)):
        try:
            if line[i].isdigit():
                parsed_line += line[i]
                break
            elif line[i:i+3] in spelled_numbers:
                parsed_line += str(spelled_numbers.index(line[i:i+3]))
                break
            elif line[i:i+4] in spelled_numbers:
                parsed_line += str(spelled_numbers.index(line[i:i+4]))
                break
            elif line[i:i+5] in spelled_numbers:
                parsed_line += str(spelled_numbers.index(line[i:i+5]))
                break
            else:
                continue
        except IndexError:
            continue
    for i in range(len(line), -1, -1):
        try:
            if line[i-1].isdigit():
                parsed_line += line[i-1]
                break
            elif line[i-3:i] in spelled_numbers:
                parsed_line += str(spelled_numbers.index(line[i-3:i]))
                break
            elif line[i-4:i] in spelled_numbers:
                parsed_line += str(spelled_numbers.index(line[i-4:i]))
                break
            elif line[i-5:i] in spelled_numbers:
                parsed_line += str(spelled_numbers.index(line[i-5:i]))
                break
            else:
                continue
        except IndexError:
            continue
    numbers_part2.append(get_number(parsed_line))
print(sum(numbers_part2))
print(len(numbers_part2))