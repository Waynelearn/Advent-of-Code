import copy

"""
Expects input from a local file called input.txt with input in the format:
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def init_cave(gen, with_floor):
    sand_source = Vector(0, 500)
    min_x, max_x = (sand_source.x, sand_source.x)
    min_y, max_y = (sand_source.y, sand_source.y)

    stone_sets = []
    for line in gen:
        vectors = []
        for v in line.split(' -> '):
            (y, x) = [int(num) for num in v.split(',')]
            (min_x, max_x) = (min(x, min_x), max(x, max_x))
            (min_y, max_y) = (min(y, min_y), max(y, max_y))
            vectors.append(Vector(x, y))
        stone_sets.append(vectors)

    cave = Cave(sand_source, max_x, max_y, min_y, with_floor)

    for v_set in stone_sets:
        cave.add_stone_set(v_set)

    return cave


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Cave:
    empty_space_sym = '.'
    stone_sym = '#'
    sand_start_sym = '+'
    sand_stop_sym = 'o'

    def __init__(self, sand_start: Vector, max_x: int, max_y: int, min_y: int,  with_floor: bool):
        self.sand_start = sand_start
        self.y_offset = min_y - 1
        self.print_from = min_y
        self.print_to = max_y + 2
        self.max_x = max_x
        self.max_y = max_y
        self.with_floor = with_floor
        self.matrix = [[self.empty_space_sym for _ in range(max_y * 2)] for _ in range(0, max_x + 3)]
        self.add_point(self.sand_start.x, self.sand_start.y, self.sand_start_sym)
        if self.with_floor:
            self.matrix[max_x + 2] = [self.stone_sym for _ in range(max_y * 2)]

    def drop_sand_until_full(self) -> int:
        sand_pieces = 0
        while True:
            stopped = self.drop_sand()
            if self.matrix[self.sand_start.x][self.sand_start.y] == self.sand_stop_sym:
                sand_pieces += 1
                break
            if not stopped:
                break
            sand_pieces += 1

        return sand_pieces

    def add_stone_set(self, vectors: list[Vector]):
        prev_v = None
        for v in vectors:
            self.add_point(v.x, v.y, self.stone_sym)
            if prev_v:
                if v.x == prev_v.x:
                    [self.add_point(v.x, y, self.stone_sym) for y in range(min(v.y, prev_v.y), max(v.y, prev_v.y) + 1)]
                elif v.y == prev_v.y:
                    [self.add_point(x, v.y, self.stone_sym) for x in range(min(v.x, prev_v.x), max(v.x, prev_v.x) + 1)]
                else:
                    raise RuntimeError(f'unexpected vector pair {prev_v} & {v}')
            prev_v = v

    def add_point(self, x: int, y: int, char: str):
        if y == self.print_from:
            self.print_from = y - 1
        if y == self.print_to:
            self.print_to = y + 2

        self.matrix[x][y] = char

    def drop_sand(self):
        stopped = False
        sand = copy.copy(self.sand_start)

        while self.should_keep_falling(sand):
            if self.point_below(sand, 0) == self.empty_space_sym:
                pass
            elif self.point_below(sand, -1) == self.empty_space_sym:
                sand.y -= 1
            elif self.point_below(sand, 1) == self.empty_space_sym:
                sand.y += 1
            else:
                self.add_point(sand.x, sand.y, self.sand_stop_sym)
                stopped = True
                break
            sand.x += 1

        return stopped

    def should_keep_falling(self, sand: Vector):
        return sand.x + 1 <= self.max_x + 2

    def point_below(self, v: Vector, shift: int) -> str:
        return self.matrix[v.x + 1][v.y + shift]

    def __str__(self):
        return "\n".join([''.join(row[self.print_from:self.print_to]) for row in self.matrix])


def get_lines():
    with open('input.txt') as file:
        for ln in file:
            yield ln.strip()


if __name__ == '__main__':
    for ii, with_floor in enumerate([False, True]):
        cave = init_cave(get_lines(), with_floor)
        solution = cave.drop_sand_until_full()

        # debugging visualization
        print(str(cave))

        print(f'Solution {ii + 1}:', solution)
