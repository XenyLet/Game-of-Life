import life
from visualizer import print_simple

mesh = life.setup(5, "random")
print_simple(mesh)
mesh = life.make_step(mesh)
print_simple(mesh)