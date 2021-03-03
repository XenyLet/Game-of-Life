from modules import life
from modules.visualizer import Visualizer
from copy import deepcopy
import time

import random

random.seed(1)

grid = life.setup(50, "random", "strict_border", multiprocessing_const=1)
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
            print("Game ended!")
            break
    i += 1
end = time.time()
print(f"Game last for {end - start} sec and made {i} steps")
