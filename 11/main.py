file_name = "11/data.txt"
lines = open(file_name,'r').read().split('\n')

def line_is_empty(line: str) -> bool:
    for i in range(len(line)):
        if line[i] == '#':
            return False
    return True

def get_empty_row_indices(lines: list) -> list:
    empty_row_indices = []
    for i in range(len(lines)):
        if line_is_empty(lines[i]):
            empty_row_indices.append(i)
    return empty_row_indices

def get_empty_column_indices(lines: list) -> list:
    empty_column_indices = []
    for j in range(len(lines[0])):
        column = ""
        for i in range(len(lines)):
            column += lines[i][j]

        if line_is_empty(column):
            empty_column_indices.append(j)
    return empty_column_indices


def expand_empty_lines(lines: list, empty_row_indices: list, empty_column_indices: list, expansion_const: int):
    for row_index in reversed(empty_row_indices):
        for i in range(expansion_const):
            lines.insert(row_index+1+i, "."*len(lines[0]))
    for column_index in reversed(empty_column_indices):
        for i in range(len(lines)):
            lines[i] = lines[i][:column_index] + "."*expansion_const + lines[i][column_index:]
    return lines

def get_galaxy_coordinates(lines: list) -> list:
    galaxy_coordinates = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                galaxy_coordinates.append((i, j))
    return galaxy_coordinates

def get_shortest_path(start: tuple, end: tuple):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def get_all_pairs_shortest_path(coordinates: list) -> list:
    all_paths = [[999999999999 for i in range(len(coordinates))] for j in range(len(coordinates))]
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                all_paths[i][j] = get_shortest_path(coordinates[i], coordinates[j])
    return all_paths


if __name__ == "__main__":
    expansion_const = 1
    empty_row_indices = get_empty_row_indices(lines)
    empty_column_indices = get_empty_column_indices(lines)
    lines = expand_empty_lines(lines, empty_row_indices, empty_column_indices, expansion_const)
    # for line in lines:
    #     if "test" in file_name:
    #         assert line == open("11/test_assertion.txt", "r").read().split("\n")[lines.index(line)]
    galaxy_coordinates = get_galaxy_coordinates(lines)
    shortest_paths = get_all_pairs_shortest_path(galaxy_coordinates)
    sum_paths = 0
    for i in range(len(shortest_paths)-1):
        for j in range(i+1, len(shortest_paths[i])):
            sum_paths += shortest_paths[i][j]
    print("Sum of all paths:", sum_paths)