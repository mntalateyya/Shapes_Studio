import Tkinter, math
from PIL import Image,ImageDraw,ImageTk
import Tree_Repr
import Event_Tree
from L_sys import L_sys

NODE_FILL = 'blue'  # color of idle nodes
NODE_FILL_ACTIVE = 'purple'  # color of active node
EDGE_FILL = 'black'  # color of edges
EDGE_LEN = 30
RAD = 3  # radium of node drawing

class Main:
    def __init__(self, parent):
        self.wnd = Tkinter.Toplevel()
        self.parent = parent

        self.frame1 = Tkinter.Frame(self.wnd)
        self.frame2 = Tkinter.Frame(self.frame1)
        self.frame3 = Tkinter.Frame(self.wnd)
        self.frame1.grid(sticky=Tkinter.NW)
        self.frame2.grid(sticky=Tkinter.NW)
        self.frame3.grid(sticky=Tkinter.NW, row=0, column=1)

        self.cv = Tkinter.Canvas(self.frame1, width=300, height=400, bg='white')
        self.cv.grid()

        self.tree = Tree_Repr.Tree(self.cv)
        self.e_hand = Event_Tree.Ev_Handler(self.tree, self.cv)
        self.tree.draw()
        self.cv.bind('<Button-1>', self.e_hand.on_click)

        self.L_sys = L_sys()
        self.L_sys.make_alphabet('FLR[]X')

        self.iter_c = Tkinter.IntVar()
        self.all = Tkinter.Radiobutton(self.frame2, text='Iterate over edges',
                                       variable=self.iter_c, value=0)
        self.all.pack()
        self.leaf = Tkinter.Radiobutton(self.frame2, text='Iterate over leaves',
                                       variable=self.iter_c, value=1)
        self.leaf.pack()
        Tkinter.Label(self.frame2, text='').pack()
        slabel = Tkinter.Label(self.frame2, text='# Iterations:')
        slabel.pack()

        self.num = Tkinter.Scale(self.frame2, from_=1, to=7, orient=Tkinter.HORIZONTAL)
        self.num.pack()
        Tkinter.Label(self.frame2, text='').pack()

        self.bframe = Tkinter.Frame(self.frame2)
        self.bframe.pack()

        self.undo = Tkinter.Button(self.bframe, text='Undo', command=self.tree.undo)
        self.undo.grid(padx=20)
        self.clearB = Tkinter.Button(self.bframe, text='Clear', command=self.reset)
        self.drawB = Tkinter.Button(self.bframe, text='Draw', command=self.gen)
        self.end = Tkinter.Button(self.bframe, text='Finish', command=self.finish)
        self.clearB.grid(row=0, column=1, padx=10)
        self.drawB.grid(row=0, column=2, padx=10)
        self.end.grid(row=0, column=3, padx=20)

        self.imc = Tkinter.Canvas(self.frame3, width=900, height=600, bg='white')
        self.imc.grid()

    def reset(self):
        self.tree.reset()

    def gen(self):
        self.L_sys.make_seed(self.tree.get_string(self.iter_c.get()))
        self.L_sys.make_rule('X',self.tree.get_string(self.iter_c.get()))
        for i in range(self.num.get()):
            self.L_sys.gen_next()
        self.im = self.draw(self.L_sys.string)
        self.photo = ImageTk.PhotoImage(self.im)
        self.imc.create_image(450,300,image=self.photo)

    def draw(self,s):
        im = Image.new('RGBA', (3000,2000))
        draw = ImageDraw.Draw(im)
        dir = 0  # absolute direction of drawing
        vec = (0.0, -1.0)  # vector to represent direction of drawing
        stack = []  # stack to aid parenthesizing
        coords = (1500, 1000)  # current position of pen
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
                                     coords[0] + EDGE_LEN * vec[0], coords[1] + EDGE_LEN * vec[1]),fill='blue')
                coords = (coords[0] + EDGE_LEN * vec[0], coords[1] + EDGE_LEN * vec[1])
        if im.getbbox():
            im = im.crop(im.getbbox())
        width, height = im.size
        if width>height*1.5 and width>900:
            im = im.resize((900, int(900.0*height/width)),Image.ANTIALIAS)
        elif height>600:
            im = im.resize((int(600.0*width/height), 600),Image.ANTIALIAS)
        return im

    def finish(self):
        self.parent.add_layer(self.im)
        self.wnd.destroy()
