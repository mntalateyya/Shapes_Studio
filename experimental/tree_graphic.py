import Tkinter
import math


class C:
    def __init__(self):
        self.v = [(300, 350, 0)]
        self.e = []

    def add_v(self, x, y, d):
        self.v.append((x, y, d))

    def add_e(self, v1, v2):
        self.e.append((v1, v2))

    def draw(self, c, d):
        for i in self.v:
            c.create_oval(i[0] - d, i[1] - d, i[0] + d, i[1] + d, fill='blue', tags='vertex')
        for i in self.e:
            c.create_line(self.v[0][0], self.v[0][1], self.v[1][0], self.v[1][1], fill='black')


class E:
    def __init__(self, c):
        self.c = c
        self.guides = []
        self.state = 0
        self.focus = -1

    def on_click(self, e):
        if self.state == 0:
            v = self.c.find_enclosed(e.x - 10, e.y - 10, e.x + 10, e.y + 10)
            print v
            if v:
                v = v[0]
                self.enfocus(v)
                c.bind('<Motion>', self.on_move)
                self.state = 1
        else:
            self.enfocus(-1)
            self.state=0
            print 'here'

    def on_move(self, e):
        pass

    def enfocus(self, v):
        c.itemconfig(self.focus, fill='blue')
        c.itemconfig(v, fill='purple')
        self.focus = v


w = Tkinter.Tk()
c = Tkinter.Canvas(w, bg='white', width=600, height=400)
c.pack()
d = 5
tree = C()
e_hand = E(c)
tree.draw(c, d)
c.bind('<Button-1>', e_hand.on_click)
Tkinter.mainloop()
