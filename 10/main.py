from math import ceil

lines = open('10/data.txt','r').read().split('\n')

class PipePiece:
    def __init__(self, pipe_type: str, y: int, x: int):
        self.type = pipe_type
        self.x = x
        self.y = y
        self.d = False

    def get_up(self):
        if self.y == 0:
            return None
        else:
            return lines[self.y - 1][self.x]
    def get_right(self):
        if self.x == len(lines[self.y]) - 1:
            return None
        else:
            return lines[self.y][self.x + 1]
    def get_down(self):
        if self.y == len(lines) - 1:
            return None
        else:
            return lines[self.y + 1][self.x]
    def get_left(self):
        if self.x == 0:
            return None
        else:
            return lines[self.y][self.x - 1]
    def can_go_left(self):
        return self.get_left() == '-' or self.get_left() == 'F' or self.get_left() == 'L'
    def can_go_right(self):
        return self.get_right() == '-' or self.get_right() == '7' or self.get_right() == 'J'
    def can_go_up(self):
        return self.get_up() == '|' or self.get_up() == 'F' or self.get_up() == '7'
    def can_go_down(self):
        return self.get_down() == '|' or self.get_down() == 'L' or self.get_down() == 'J'
    def get_possible_neighbors(self):
        possible_neighbors = []
        if self.type == 'S':
            if self.can_go_right():
                possible_neighbors.append((self.y, self.x + 1))
            if self.can_go_down():
                possible_neighbors.append((self.y + 1, self.x))
            if self.can_go_left():
                possible_neighbors.append((self.y, self.x - 1))
            if self.can_go_up():
                possible_neighbors.append((self.y - 1, self.x))
            return possible_neighbors
        if self.type == '-':
            if self.can_go_left():
                possible_neighbors.append((self.y, self.x - 1))
            if self.can_go_right():
                possible_neighbors.append((self.y, self.x + 1))
            return possible_neighbors
        if self.type == '|':
            if self.can_go_up():
                possible_neighbors.append((self.y - 1, self.x))
            if self.can_go_down():
                possible_neighbors.append((self.y + 1, self.x))
            return possible_neighbors
        if self.type == 'F':
            if self.can_go_right():
                possible_neighbors.append((self.y, self.x + 1))
            if self.can_go_down():
                possible_neighbors.append((self.y + 1, self.x))
            return possible_neighbors
        if self.type == '7':
            if self.can_go_left():
                possible_neighbors.append((self.y, self.x - 1))
            if self.can_go_down():
                possible_neighbors.append((self.y + 1, self.x))
            return possible_neighbors
        if self.type == 'L':
            if self.can_go_right():
                possible_neighbors.append((self.y, self.x + 1))
            if self.can_go_up():
                possible_neighbors.append((self.y - 1, self.x))
            return possible_neighbors
        if self.type == 'J':
            if self.can_go_left():
                possible_neighbors.append((self.y, self.x - 1))
            if self.can_go_up():
                possible_neighbors.append((self.y - 1, self.x))
            return possible_neighbors
    def __str__(self) -> str:
        return self.type + " at (" + str(self.y) + ", " + str(self.x) + ")"
    
def get_start_piece():
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "S":
                start_piece = PipePiece(lines[y][x], y, x)
                return start_piece
    return None

def get_grid():
    pipe_pieces = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            pipe_pieces.append(PipePiece(lines[y][x], y, x))
    return pipe_pieces

def main():
    start_piece = get_start_piece()
    stack = [start_piece]
    grid = get_grid()
    neighboring_coordinates = start_piece.get_possible_neighbors()
    steps = 0
    while len(stack) > 0:
        pipe_piece = stack.pop()
        if not pipe_piece.d:
            steps += 1
            pipe_piece.d = True
            neighboring_coordinates = pipe_piece.get_possible_neighbors()
            for coordinate in neighboring_coordinates:
                stack.append(grid[coordinate[0] * len(lines[0]) + coordinate[1]])
    print(ceil(steps/2))

main()