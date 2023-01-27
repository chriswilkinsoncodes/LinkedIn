import math
import os
import time

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]  # error in tutorial "Laying out the code": no space between ''

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1] < 0) or round(point[1] >= self._y)

    def setPos(self, pos, mark):
        #pos is a cartesian pt. e.g. [1, 2]
        self._canvas[round(pos[0])][round(pos[1])] = mark     

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

        # this doesn't do anything? it's always overwritten before anything is drawn?
        self.direction = [0, 1]

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

    def setDegrees(self, degrees):
        # 360 degrees = 2pi radians
        radians = (degrees/180) * math.pi
        # converts to cartesian points (between 0 to +-1?) in the direction of the degrees given
        # starting direction always seems to be pointing up?
        # TODO: try: set direction other than pointing up, don't move, set direction again
        self.direction = [math.sin(radians), -math.cos(radians)]

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0] + 1, self.pos[1]]
        self.draw(pos)

    def left(self):
        pos = [self.pos[0] - 1, self.pos[1]]
        self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1] + 1]
        self.draw(pos)

    def up(self):
        pos = [self.pos[0], self.pos[1] - 1]
        self.draw(pos)

    def square(self, length):
        self.length = length

        for _ in range(length):
            self.right()

        for _ in range(length):
            self.down()

        for _ in range(length):
            self.left()

        for _ in range(length):
            self.up()




canvas = Canvas(20, 10)
scribe = TerminalScribe(canvas)

scribe.setDegrees(135)
for i in range(10):
    scribe.forward()
scribe.setDegrees(45)
for i in range(10):
    scribe.forward()
