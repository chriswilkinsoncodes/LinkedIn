import os
import time

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]  # error? in tutorial "Laying out the code": no space between ''

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark     #pos is a cartesian pt. e.g. [1, 2]

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))   # error in tutorial "Laying out the code": [] inside print()


class TerminalScribe():
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [0, 0]
        self.framerate = 0.1
        self.mark = '+'
        self.trail = '.'

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)    # uses current pos, changes to trail char
        self.pos = pos                              # updates pos
        self.canvas.setPos(self.pos, self.mark)     #uses updated pos, changes to mark char
        self.canvas.print()
        time.sleep(self.framerate)                  # wasn't included in "Laying out the code" so the demo of the code did not match the code



canvas = Canvas(20, 20)
# canvas.clear()
scribe = TerminalScribe(canvas)

for i in range(0, 10):
    for j in range(0, 10):
        scribe.draw((i, j))
