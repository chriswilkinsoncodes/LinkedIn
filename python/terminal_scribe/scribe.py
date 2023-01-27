import os
import time

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]  # error in tutorial "Laying out the code": no space between ''

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
        # use current pos to change point to trail character
        self.canvas.setPos(self.pos, self.trail)
        # update the position coordinates
        self.pos = pos
        # using the updated coordinates, add the mark character
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        # this statement was not included in "Laying out the code" so the demo video did not match the code
        # (i.e. the video included a delay between drawing each point)
        time.sleep(self.framerate)

    def right(self):
        self.canvas.setPos(self.pos, self.trail)
        self.pos[0] += 1
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        time.sleep(self.framerate)


canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

scribe.right()
scribe.right()
scribe.right()
scribe.right()
