import math
import Tkinter
from globals import T_Gen


class Tree:
    def __init__(self):
        self.ids = []       # tkinter id
        self.pos = [0]      # position in self.string
        self.dir = [0]      # absolute direction (clockwise)
        self.string = ''    # L-string

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

    def draw(self):
        T_Gen.cv.delete(Tkinter.ALL)    # clear canvas
        dir = 0     # absolute direction of drawing
        vec = (0.0, -1.0)       # vector to represent direction of drawing
        stack = []      # stack to aid parenthesizing
        coords = (300, 300)     # current position of pen
        self.ids = [T_Gen.cv.create_oval(coords[0] - T_Gen.RAD, coords[1] - T_Gen.RAD,
                                         coords[0] + T_Gen.RAD, coords[1] + T_Gen.RAD,
                                         fill=T_Gen.NODE_FILL, tags='vertex')]      # first node
        for i in range(len(self.string)):
            if self.string[i] == '[':
                stack.append((coords[0], coords[1], vec[0], vec[1], dir))   # store current position
            elif self.string[i] == ']':
                # restore positions from stack
                popped = stack.pop()
                coords = popped[:2]
                vec = popped[2:4]
                dir = popped[4]
            elif self.string[i] == 'R':
                # update direction and vector of direction
                dir = (dir + 1) % 24
                vec = (math.cos(((dir - 6) % 24) * math.pi / 12), math.sin(((dir - 6) % 24) * math.pi / 12))
            elif self.string[i] == 'L':
                # update direction and vector of direction
                dir = (dir - 1) % 24
                vec = (math.cos(((dir - 6) % 24) * math.pi / 12), math.sin(((dir - 6) % 24) * math.pi / 12))
            elif self.string[i] == 'F':
                # draw line and node
                T_Gen.cv.create_line(coords[0], coords[1],
                                     coords[0] + T_Gen.EDGE_LEN * vec[0], coords[1] + T_Gen.EDGE_LEN * vec[1],
                                     tags='edge')
                coords = (coords[0] + T_Gen.EDGE_LEN * vec[0], coords[1] + T_Gen.EDGE_LEN * vec[1])
                self.ids += [T_Gen.cv.create_oval(
                    coords[0] - T_Gen.RAD, coords[1] - T_Gen.RAD, coords[0] + T_Gen.RAD, coords[1] + T_Gen.RAD,
                    fill=T_Gen.NODE_FILL, tags='vertex')]   # add node ids to self.ids
