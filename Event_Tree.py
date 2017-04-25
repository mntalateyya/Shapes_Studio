import Tkinter, math


NODE_FILL = 'blue'  # color of idle nodes
NODE_FILL_ACTIVE = 'purple'  # color of active node
EDGE_FILL = 'black'  # color of edges
EDGE_LEN = 30
RAD = 3  # radium of node drawing

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
    def __init__(self, t, cv):
        self.tree = t
        self.guides = []
        self.state = 0
        self.dir = 0
        self.focus = -1
        self.cv = cv

    def on_click(self, e):
        if self.state == 0:
            v = self.cv.find_enclosed(e.x - RAD * 3, e.y - RAD * 3, e.x + RAD * 3, e.y + RAD * 3)
            if v:
                v = v[0]
                self.enfocus(v)
                self.cv.bind('<Motion>', self.on_move)
                self.state = 1
        else:
            self.tree.add_v(self.dir, self.focus)
            self.enfocus(-1)
            self.cv.delete(Tkinter.ALL)
            self.tree.draw()
            self.cv.unbind('<Motion>')
            self.state = 0

    def on_move(self, e):
        center = [x + RAD for x in self.cv.coords(self.focus)][0:2]
        angle = get_angle(e.x, e.y, center[0], center[1])
        self.dir = int(round(12 * angle / math.pi) + 6) % 24

    def enfocus(self, v):
        self.cv.itemconfig(self.focus, fill=NODE_FILL)
        self.cv.itemconfig(v, fill=NODE_FILL_ACTIVE)
        self.focus = v
