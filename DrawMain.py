import Tkinter
from PIL import Image, ImageDraw, ImageTk
import frieze
class Helper:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.coords = []
        self.ims = []

class Draw:
    def __init__(self, x, y, t, s):
        self.root = Tkinter.Toplevel()
        self.root.geometry('960x%d'%(240 if t==2 else 680))
        self.tframe = Tkinter.Frame(self.root, width=960, height=60)
        self.tframe.grid()
        self.cframe = Tkinter.Frame(self.root)
        self.cframe.grid()

        self.fsymm = {'pmm2':0, 'pma2':1, 'p112':2, 'p1m1':3, 'pm11':4,
                        'p111':5, 'p1a1':6}

        self.type = t
        self.sym = s

        self.tools = Tkinter.Canvas(self.tframe, width=960, height=60,
                                    bg='#cccccc',highlightthickness=0, border=0)
        self.cv = Tkinter.Canvas(self.cframe, width=900,
                                height=(120 if (t==2) else 590), bg='white')
        self.tools.pack()
        self.cv.pack(pady=20)

        self.labels = []
        self.ids = []

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/undo.bmp')))
        self.ids += [self.tools.create_image(15, 15, image=self.labels[-1],anchor=Tkinter.NW)]

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/redo.bmp')))
        self.ids += [self.tools.create_image(60, 15, image=self.labels[-1],anchor=Tkinter.NW)]

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/pen.bmp')))
        self.ids += [self.tools.create_image(150, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.change_tool(0, 165))

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/line.bmp')))
        self.ids += [self.tools.create_image(210, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.change_tool(1, 225))

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/curve.bmp')))
        self.ids += [self.tools.create_image(270, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.change_tool(2, 285))

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/fill.bmp')))
        self.ids += [self.tools.create_image(330, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.change_tool(3, 345))

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/eraser.bmp')))
        self.ids += [self.tools.create_image(390, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.change_tool(4, 405))

        self.tools.create_text(500,30,text='Stroke width', fill='slate gray')
        self.widthS = Tkinter.Scale(self.tools, from_=1, to=10,
            orient=Tkinter.HORIZONTAL,bg='#cccccc', bd=0, highlightthickness=0,
            troughcolor='#888888')
        self.tools.create_window(540, 5, window=self.widthS, anchor=Tkinter.NW)

        self.tools.create_text(690,30,text='Color', fill='slate gray')
        self.tools.create_oval(720, 15, 750, 45, fill='white', width=3)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/finish.bmp')))
        self.tools.create_image(840, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.cv.bind('<Button-1>', self.press)
        self.cv.bind('<B1-Motion>', self.move)
        self.helper = Helper()

        self.toolname = {'pen':0, 'line':1, 'curve':2, 'fill':3, 'eraser':4}
        self.tool = 0
        self.dot = self.tools.create_oval(162,47,168,53,
                    fill='#888888', width=0)
        self.width = self.widthS.get()
        self.root.mainloop()

    def change_tool(self, t, x):
        self.tool = t
        self.tools.coords(self.dot,x-3,47,x+3,53)

    def press(self,e):
        if self.type == 2:
            self.helper.coords = frieze.repeat(900,120, 1.5,
                                    self.sym, (e.x, e.y))
        self.width = self.widthS.get()

    def move(self, e):
        if self.type == 2:
            if self.tool == self.toolname['pen']:
                coords = frieze.repeat(900,120, 1.5,
                                        self.sym, (e.x, e.y))
                for i in range(len(coords)):
                    self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                        coords[i][0],coords[i][1], width=self.width)

                self.helper.coords = coords
            elif self.tool == self.toolname['line']:
                self.cv.delete('temp')
                coords = frieze.repeat(900,120, 1.5,
                                        self.sym, (e.x, e.y))
                for i in range(len(coords)):
                    self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                        coords[i][0],coords[i][1], width=self.width, tag='temp')

    def release(self, e):
        # PIL draw image

    def hover(self, e):
        pass

Draw(640,480, 2, 0)
