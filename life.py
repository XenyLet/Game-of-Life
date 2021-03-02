from multiprocessing import Pool
from itertools import product
from functools import partial
from random import choice

displ_base = [-1, 0, 1]
filling_types = ["empty", "full", "random"]
height, width, processes_num = None, None, None


def setup(side_size, filling_type, multiprocessing_const=4):
    def z():
        return 0
    def o():
        return 1

    global height, width, processes_num
    assert filling_type in filling_types, "Wrong filling type"

    if filling_type == "empty":
        val_fun = z
    elif filling_type == "full":
        val_fun = o
    elif filling_type == "random":
        val_fun = partial(choice, [0, 1])
    else:
        raise RuntimeError

    mesh = [[val_fun() for _ in side_size] for _ in side_size]
    height = side_size
    width = side_size
    processes_num = multiprocessing_const

    return mesh


def _xycheck(x, y):
    assert 0 <= x < width, "X value not allowed"
    assert 0 <= y < height, "Y value not allowed"


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

def _count_alive_neighbours(_mesh, x, y):
    alive = 0
    for displ in product(displ_base, displ_base):
        if displ == (0, 0):
            continue

        if get(_mesh, x + displ[0], y + displ[1]) == 1:
            alive += 1

        if alive > 3:
            return alive


def _get_next_cell_state(_mesh, x, y):
    neighbours = _count_alive_neighbours(_mesh, x, y)
    val = get(_mesh, x, y)
    is_altered = False
    if val == 0 and neighbours == 3:
        return 1, True
    if val == 1 and 2 <= neighbours <= 3:
        return 1, False
    if val == 1 and (neighbours < 2 or neighbours > 3):
        return 0, True

    return val, is_altered


def get(_mesh, x, y):
    _xycheck(x, y)
    return _mesh[y][x]


def switch(_mesh, x, y):
    _xycheck(x, y)
    _mesh[y][x] = (_mesh[y][x] + 1) % 2


def set(_mesh, x, y, val):
    _xycheck(x, y)
    _valcheck(val)
    _mesh[y][x] = val


def make_step(_mesh):
    cells_to_alter = []  # tuples list [(x, y), ...]

    for x in range(width):
        for y in range(height):
            new_val, is_altered = _get_next_cell_state(_mesh, x, y)
            if is_altered:
                cells_to_alter.append((x, y))

    for x, y in cells_to_alter:
        switch(_mesh, x, y)

    return mesh
