from tkinter import Tk, Canvas, LAST as TK_LAST, FIRST as TK_FIRST

class Visualizer:
    WIN_SIZE = (500, 500)
    CELL_SIDE = None

    def __init__(self):
        self._root = Tk()

        self._canvas = Canvas(self._root,
                              width=self.WIN_SIZE[0],
                              height=self.WIN_SIZE[1],
                              bg='white')

        self._canvas.pack()

    def draw_grid(self, grid):
        # we assume that grid is square
        if self.CELL_SIDE is None:
            self.CELL_SIDE = min(self.WIN_SIZE)//len(grid)
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                self._canvas.create_rectangle(
                    x * self.CELL_SIDE, y * self.CELL_SIDE,
                    (x+1) * self.CELL_SIDE, (y+1)*self.CELL_SIDE,
                    fill="blue" if val else "white", outline='blue')
        self._root.update()