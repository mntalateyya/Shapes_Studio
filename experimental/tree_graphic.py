import Tkinter
import math

NODE_FILL = 'white'  # color of idle nodes
NODE_FILL_ACTIVE = 'purple'  # color of active node
EDGE_FILL = 'black'  # color of edges
EDGE_LEN = 30
RAD = 3  # radium of node drawing


class C:
    def __init__(self):
        self.ids = []  # tkinter id
        self.pos = [0]  # position in self.string
        self.dir = [0]  # absolute direction (clockwise)
        self.string = ''  # L-string

    # add node: n=abs direction of node, id=id of parent
    def add_v(self, n, id):
        order = self.ids.index(id)  # order of parent
        relative = (n - self.dir[order]) % 24  # relative direction to parent
        pos = self.pos[order]  # position of parent in self.string
        if relative <= 12:
            nodestring = '[' + 'R' * relative + 'F]'  # string representing new branch for the node
        else:
            nodestring = '[' + 'L' * (24 - relative) + 'F]'
        # update string, pos and dir
        self.string = self.string[:pos] + nodestring + self.string[pos:]
        self.pos = self.pos[:order + 1] + [self.pos[order] + len(nodestring) - 1] + \
                   [x + len(nodestring) for x in self.pos[order + 1:]]
        self.dir = self.dir[:order + 1] + [n] + self.dir[order + 1:]
        print self.string

    def draw(self):
        global c
        c.delete(Tkinter.ALL)
        vec = (0.0, -1.0)
        dir = 0
        stack = []
        coords = (300, 300)
        self.ids = [c.create_oval(coords[0] - RAD, coords[1] - RAD, coords[0] + RAD, coords[1] + RAD,
                                  fill=NODE_FILL, tags='vertex')]
        for i in range(len(self.string)):
            if self.string[i] == '[':
                stack.append((coords[0], coords[1], vec[0], vec[1], dir))
                print 'push', (coords[0], coords[1], vec[0], vec[1], dir), self.string[i:]
            elif self.string[i] == ']':
                popped = stack.pop()
                print 'pop', popped, self.string[i:]
                coords = popped[:2]
                vec = popped[2:4]
                dir = popped[4]
            elif self.string[i] == 'R':
                dir = (dir + 1) % 24
                vec = (math.cos(((dir - 6) % 24) * math.pi / 12), math.sin(((dir - 6) % 24) * math.pi / 12))
            elif self.string[i] == 'L':
                dir = (dir - 1) % 24
                vec = (math.cos(((dir - 6) % 24) * math.pi / 12), math.sin(((dir - 6) % 24) * math.pi / 12))
            elif self.string[i] == 'F':
                c.create_line(coords[0], coords[1],
                              coords[0] + EDGE_LEN * vec[0], coords[1] + EDGE_LEN * vec[1], tags='edge')
                coords = (coords[0] + EDGE_LEN * vec[0], coords[1] + EDGE_LEN * vec[1])
                self.ids += [c.create_oval(
                    coords[0] - RAD, coords[1] - RAD, coords[0] + RAD, coords[1] + RAD,
                    fill=NODE_FILL, tags='vertex')]


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


class E:
    def __init__(self, t):
        self.tree = t
        self.guides = []
        self.state = 0
        self.dir = 0
        self.focus = -1

    def on_click(self, e):
        global c
        if self.state == 0:
            v = c.find_enclosed(e.x - RAD * 3, e.y - RAD * 3, e.x + RAD * 3, e.y + RAD * 3)
            if v:
                v = v[0]
                self.enfocus(v)
                c.bind('<Motion>', self.on_move)
                self.state = 1
        else:
            self.tree.add_v(self.dir, self.focus)
            self.enfocus(-1)
            c.delete(Tkinter.ALL)
            self.tree.draw()
            c.unbind('<Motion>')
            self.state = 0

    def on_move(self, e):
        global c
        center = [x + RAD for x in c.coords(self.focus)][:2]
        angle = get_angle(e.x, e.y, center[0], center[1])
        self.dir = int(round(12 * angle / math.pi) + 6) % 24

    def enfocus(self, v):
        c.itemconfig(self.focus, fill=NODE_FILL)
        c.itemconfig(v, fill=NODE_FILL_ACTIVE)
        self.focus = v


w = Tkinter.Tk()
c = Tkinter.Canvas(w, bg='white', width=600, height=400)
c.pack()
d = 5
tree = C()
e_hand = E(tree)
tree.draw()
c.bind('<Button-1>', e_hand.on_click)
Tkinter.mainloop()
