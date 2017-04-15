import Tkinter
import math
from globals import T_Gen


# gets the angle from point 2 to point 1
def get_angle(x1, y1, x2, y2):
    if x1 == x2:
        if y1 >= y2:
            return math.pi / 2
        else:
            return -math.pi / 2
    if x1 > x2:
        if y1 >= y2:
            return math.atan((y1 - y2) / float(x1 - x2))
        else:
            return 2 * math.pi + math.atan((y1 - y2) / float(x1 - x2))
    else:
        return math.atan((y1 - y2) / float(x1 - x2)) + math.pi


class Ev_Handler:
    def __init__(self, t):
        self.tree = t
        self.guides = []
        self.state = 0
        self.dir = 0
        self.focus = -1

    def on_click(self, e):
        if self.state == 0:
            v = T_Gen.cv.find_enclosed(e.x - T_Gen.RAD * 3, e.y - T_Gen.RAD * 3, e.x + T_Gen.RAD * 3, e.y + T_Gen.RAD * 3)
            if v:
                v = v[0]
                self.enfocus(v)
                T_Gen.cv.bind('<Motion>', self.on_move)
                self.state = 1
        else:
            self.tree.add_v(self.dir, self.focus)
            self.enfocus(-1)
            T_Gen.cv.delete(Tkinter.ALL)
            self.tree.draw()
            T_Gen.cv.unbind('<Motion>')
            self.state = 0

    def on_move(self, e):
        center = [x + T_Gen.RAD for x in T_Gen.cv.coords(self.focus)][:2]
        angle = get_angle(e.x, e.y, center[0], center[1])
        self.dir = int(round(12 * angle / math.pi) + 6) % 24

    def enfocus(self, v):
        T_Gen.cv.itemconfig(self.focus, fill=T_Gen.NODE_FILL)
        T_Gen.cv.itemconfig(v, fill=T_Gen.NODE_FILL_ACTIVE)
        self.focus = v
