from modules import life
import numpy as np


def test_rules_1():
    life.setup(3, "empty", "strict_border")
    start_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    res_grid = life.make_step(start_grid)
    assert np.all((np.array(res_grid) == 0))


def test_rules_2():
    life.setup(3, "empty", "strict_border")
    start_grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    res_grid = life.make_step(start_grid)
    assert np.all((np.array(res_grid) == 0))


def test_rules_3():
    life.setup(3, "empty", "strict_border")
    start_grid = [
        [1, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    res_grid = np.array(life.make_step(start_grid))
    assert np.all(np.argwhere(res_grid == 1) == [
        [0, 1],
        [1, 1]])


def test_rules_4():
    life.setup(3, "empty", "strict_border")
    start_grid = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    res_grid = np.array(life.make_step(start_grid))
    assert np.all(np.argwhere(res_grid == 1) == \
                  [[0, 1], [0, 2],
                   [1, 1], [1, 2]])


def test_rules_5():
    life.setup(3, "empty", "strict_border")
    start_grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    res_grid = np.array(life.make_step(start_grid))
    assert np.all(np.argwhere(res_grid == 1) == \
                  [[0, 0], [0, 2],
                   [2, 0], [2, 2]])


def test_rules_6():
    life.setup(3, "empty", "strict_border")
    start_grid = [
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0]
    ]
    res_grid = np.array(life.make_step(start_grid))
    assert np.all(np.argwhere(res_grid == 1) == \
                  [[0, 1], [0, 2],
                   [1, 1], [1, 2]])
