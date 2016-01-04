import tkinter as tk
import sudoku


class SudokuCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.margin = 20
        self.size = tk.IntVar()
        self.size.set(9)
        self.generate()

    def generate(self):
        self.grid = sudoku.Grid(sudoku.Sudoku.random(self.size.get()))
        self.resize()
        self.draw()

    def resize(self):
        n = self.size.get()
        self.side = 500 // n
        self.height = self.width = self.margin * 2 + self.side * n

    def draw_grid(self):
        n = self.size.get()
        self.delete("lines")
        for i in range(n + 1):
            color = "blue" if i % n ** .5 == 0 else "gray"
            x0 = self.margin + i * self.side
            y0 = self.margin
            x1 = self.margin + i * self.side
            y1 = self.height - self.margin
            self.create_line(x0, y0, x1, y1, fill=color, tags="lines")
            self.create_line(y0, x0, y1, x1, fill=color, tags="lines")

    def draw_numbers(self):
        self.delete("numbers")
        for cell in filter(lambda c: c.fixed, self.grid):
            x = self.margin + cell.coord[0] * self.side + self.side / 2
            y = self.margin + cell.coord[1] * self.side + self.side / 2
            self.create_text(x, y, text=cell, tags="numbers")

    def draw(self):
        self.draw_grid()
        self.draw_numbers()


def main():
    WIDTH = 550
    HEIGHT = 700

    root = tk.Tk()
    root.title('Sudoku')
    root.geometry('%dx%d+200+200' % (WIDTH, HEIGHT))
    root.resizable(0, 0)

    sizes = [('%dx%d' % (i, i), i) for i in [4, 9, 16, 25]]

    canvas = SudokuCanvas(root, height=WIDTH, width=WIDTH)

    for text, size in sizes:
        tk.Radiobutton(root, text=text,
                       variable=canvas.size, value=size).pack(anchor=tk.W)

    tk.Button(root, text='Generate', command=canvas.generate).pack(anchor=tk.W)

    canvas.pack(fill=tk.BOTH, expand=1)
    root.mainloop()


if __name__ == '__main__':
    main()
