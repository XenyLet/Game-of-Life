from modules import life
from modules.visualizer import Visualizer
from copy import deepcopy
from time import sleep

import random

random.seed(1)

vis = Visualizer()
grid = life.setup(50, "random", "strict_border")
vis.draw_grid(grid)
i = 0
grid_old = None
grid_old_old = None
while True:
    try:
        print (f"Step {i}")
        if grid_old:
            grid_old_old = deepcopy(grid_old)
        grid_old = deepcopy(grid)
        grid = life.make_step(grid)
        if grid_old and grid_old_old:
            if life._check_empty(grid) or \
                    life._check_stable(grid, grid_old, grid_old_old):
                print("Game ended!")
                break
        if i % 1 == 0:
            vis.draw_grid(grid)
        i += 1
        sleep(0.2)
    except KeyboardInterrupt:
        ans = input("resume?")
        if ans.lower() == "n":
            break

