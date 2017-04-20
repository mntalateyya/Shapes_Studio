import Tkinter, math
from PIL import Image,ImageDraw,ImageTk
from globals import T_Gen
import Tree_Repr
import Event_Tree
from L_sys import L_sys


class Main:
    def __init__(self):
        T_Gen.wnd = Tkinter.Toplevel()

        self.frame1 = Tkinter.Frame(T_Gen.wnd, width=300)
        self.frame2 = Tkinter.Frame(T_Gen.wnd, width=200)
        self.frame3 = Tkinter.Frame(T_Gen.wnd, width=300)
        self.frame1.grid(sticky=Tkinter.NW)
        self.frame2.grid(sticky=Tkinter.NW, row=0, column=1)
        self.frame3.grid(sticky=Tkinter.NW, row=0, column=2)

        T_Gen.cv = Tkinter.Canvas(self.frame1, width=280, height=500, bg='white')
        T_Gen.cv.grid()

        self.tree = Tree_Repr.Tree()
        self.e_hand = Event_Tree.Ev_Handler(self.tree)
        self.tree.draw()
        T_Gen.cv.bind('<Button-1>', self.e_hand.on_click)

        self.L_sys = L_sys()
        self.L_sys.make_alphabet('FLR[]X')

        self.iter_c = Tkinter.IntVar()
        self.all = Tkinter.Radiobutton(self.frame2, text='Iterate over edges',
                                       variable=self.iter_c, value=0)
        self.all.pack()
        self.leaf = Tkinter.Radiobutton(self.frame2, text='Iterate over leaves',
                                       variable=self.iter_c, value=1)
        self.leaf.pack()

        self.clearB = Tkinter.Button(self.frame2, text='clear', command=self.reset)
        self.drawB = Tkinter.Button(self.frame2, text='draw', command=self.gen)
        self.clearB.pack()
        self.drawB.pack()
        
        self.imc = Tkinter.Canvas(self.frame3, width=280, height=500, bg='white')
        self.imc.grid()

        T_Gen.wnd.mainloop()

    def reset(self):
        self.tree.reset()

    def gen(self):
        self.L_sys.make_seed(self.tree.get_string(self.iter_c.get()))
        self.L_sys.make_rule('X',self.tree.get_string(self.iter_c.get()))
        for i in range(4):
            self.L_sys.gen_next()
        self.draw(self.L_sys.string)
        self.im = ImageTk.PhotoImage(Image.open("test.png"))
        self.imc.create_image(140,250,image=self.im)
        print 'seed:', self.L_sys.seed
        print 'Rule:'
        print 'X ->', self.L_sys.rules['X']
        print 'string', self.L_sys.string


    def draw(self,s):
        im = Image.new('RGBA', (300,500))
        draw = ImageDraw.Draw(im)
        dir = 0  # absolute direction of drawing
        vec = (0.0, -1.0)  # vector to represent direction of drawing
        stack = []  # stack to aid parenthesizing
        coords = (150, 450)  # current position of pen
        for i in range(len(s)):
            if s[i] == '[':
                stack.append((coords[0], coords[1], vec[0], vec[1], dir))  # store current position
            elif s[i] == ']':
                # restore positions from stack
                popped = stack.pop()
                coords = popped[:2]
                vec = popped[2:4]
                dir = popped[4]
            elif s[i] == 'R':
                # update direction and vector of direction
                dir = (dir + 1) % 24
                vec = (math.cos(((dir - 6) % 24) * math.pi / 12), math.sin(((dir - 6) % 24) * math.pi / 12))
            elif s[i] == 'L':
                # update direction and vector of direction
                dir = (dir - 1) % 24
                vec = (math.cos(((dir - 6) % 24) * math.pi / 12), math.sin(((dir - 6) % 24) * math.pi / 12))
            elif s[i] == 'F':
                # draw line and node
                draw.line((coords[0], coords[1],
                                     coords[0] + T_Gen.EDGE_LEN * vec[0], coords[1] + T_Gen.EDGE_LEN * vec[1]),fill='blue')
                coords = (coords[0] + T_Gen.EDGE_LEN * vec[0], coords[1] + T_Gen.EDGE_LEN * vec[1])
        im.save('test.png')
Main()
