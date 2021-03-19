from modules import life
from copy import deepcopy
import time
import pprint

import random

def perform_single_test(side_size, processes_num):
    random.seed(1)

    grid = life.setup(side_size, "random", "strict_border", multiprocessing_const=processes_num)
    i = 0
    grid_old = None
    grid_old_old = None

    start = time.time()
    while True:
        if grid_old:
            grid_old_old = deepcopy(grid_old)
        grid_old = deepcopy(grid)
        grid = life.make_step(grid)
        if grid_old and grid_old_old:
            if life._check_empty(grid) or \
                    life._check_stable(grid, grid_old, grid_old_old):
                # print("Game ended!")
                break
        i += 1
    end = time.time()
    print(f"Game: side: {side_size}, processes: {processes_num}, time: {end-start}")
    return end-start

if __name__ == '__main__':
    res = []
    for side in [5, 10, 20, 40]:
        sub_res = []
        for processes in [1, 2, 4, 6, 8]:
            sub_res.append(perform_single_test(side, processes))
        res.append(sub_res)

    pprint.pprint(res)