from multiprocessing import Pool
from itertools import product
from functools import partial
from random import choice
import numpy as np

displ_base = [-1, 0, 1]
filling_types = ["empty", "full", "random"]
border_logics = ["wrap", "strict_border"]
height, width, processes_num, border_logic = None, None, None, None


def setup(side_size, filling_type, _border_logic, multiprocessing_const=4):
    def z():
        return 0

    def o():
        return 1

    global height, width, processes_num, border_logic
    assert _border_logic in border_logics
    assert filling_type in filling_types, "Wrong filling type"

    border_logic = _border_logic

    if filling_type == "empty":
        val_fun = z
    elif filling_type == "full":
        val_fun = o
    elif filling_type == "random":
        val_fun = partial(choice, [0, 1])
    else:
        raise RuntimeError

    grid = [[val_fun() for _ in range(side_size)] for _ in range(side_size)]
    height = side_size
    width = side_size
    processes_num = multiprocessing_const

    return grid


def _xycheck(x, y, allow_one_step_outside=False):
    if allow_one_step_outside:
        _min = -1
        w = width
        h = height
    else:
        _min = 0
        w = width - 1
        h = height - 1
    assert _min <= x <= w, "X value not allowed"
    assert _min <= y <= h, "Y value not allowed"


def _valcheck(val):
    assert val == 0 or val == 1, "Value is not allowed"


# Каждое следующее поколение рассчитывается на основе
# предыдущего по таким правилам:
#   в пустой (мёртвой) клетке, рядом с которой ровно три живые
#       клетки, зарождается жизнь;
#   если у живой клетки есть две или три живые соседки, то эта
#       клетка продолжает жить;
#       в противном случае, если соседей меньше двух или больше трёх,
#       клетка умирает («от одиночества» или «от перенаселённости»)

def _count_alive_neighbours(_grid, x, y):
    alive = 0
    for displ in product(displ_base, displ_base):
        if displ == (0, 0):
            continue

        if get(_grid, x + displ[0], y + displ[1]) == 1:
            alive += 1

        if alive > 3:
            return alive

    return alive


def _get_next_cell_state(_grid, x, y):
    neighbours = _count_alive_neighbours(_grid, x, y)
    val = get(_grid, x, y)
    is_altered = False
    if val == 0 and neighbours == 3:
        return 1, True
    if val == 1 and 2 <= neighbours <= 3:
        return 1, False
    if val == 1 and (neighbours < 2 or neighbours > 3):
        return 0, True

    return val, is_altered


def _check_empty(_grid):
    return np.all((np.array(_grid) == 0))


def _check_stable(_grid1, _grid2, _grid3):
    return np.all(np.array(_grid1) == np.array(_grid2)) or \
           np.all(np.array(_grid1) == np.array(_grid3))


def get(_grid, x, y):
    allow_one_step_outside = True

    _xycheck(x, y, allow_one_step_outside)

    if border_logic == "wrap":
        if y == -1:
            y = height - 1
        elif y == height:
            y = 0

        if x == -1:
            x = width - 1
        elif x == width:
            x = 0
    elif border_logic == "strict_border":
        try:
            _xycheck(x, y)
        except AssertionError:
            return 0

    return _grid[y][x]


def switch(_grid, x, y):
    _xycheck(x, y)
    _grid[y][x] = (_grid[y][x] + 1) % 2


def set(_grid, x, y, val):
    _xycheck(x, y)
    _valcheck(val)
    _grid[y][x] = val


def make_step(_grid):
    cells_to_alter = []  # tuples list [(x, y), ...]

    for x in range(width):
        for y in range(height):
            new_val, is_altered = _get_next_cell_state(_grid, x, y)
            if is_altered:
                cells_to_alter.append((x, y))

    for x, y in cells_to_alter:
        switch(_grid, x, y)

    return _grid
