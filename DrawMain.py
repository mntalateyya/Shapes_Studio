import Tkinter
from PIL import Image, ImageDraw, ImageTk
class Helper:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.coords = []
        self.ims = []

class Draw:
    def __init__(self, x, y, t, s):
        self.root = Tkinter.Toplevel()
        self.root.geometry('960x%d'%(320 if t==2 else 640))
        self.tframe = Tkinter.Frame(self.root, width=960, height=60)
        self.tframe.grid()
        self.cframe = Tkinter.Frame(self.root,
            width=960, height=580)
        self.cframe.grid()

        self.type = t
        self.sym = s

        self.tools = Tkinter.Canvas(self.tframe, width=960, height=60,
                                    bg='#cccccc',highlightthickness=0, border=0)
        self.cv = Tkinter.Canvas(self.cframe, width=720,
                                height=(120 if (t==2) else 540), bg='white')
        self.tools.pack()
        self.cv.pack(pady=20)

        self.labels = []

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/undo.bmp')))
        self.tools.create_image(15, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/redo.bmp')))
        self.tools.create_image(60, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/pen.bmp')))
        self.tools.create_image(150, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/line.bmp')))
        self.tools.create_image(210, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/curve.bmp')))
        self.tools.create_image(270, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/fill.bmp')))
        self.tools.create_image(330, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/eraser.bmp')))
        self.tools.create_image(390, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.tools.create_text(500,30,text='Stroke width', fill='slate gray')
        self.widthS = Tkinter.Scale(self.tools, from_=1, to=10,
            orient=Tkinter.HORIZONTAL,bg='#cccccc', bd=0, highlightthickness=0,
            sliderrelief=Tkinter.RIDGE, troughcolor='#888888')
        self.tools.create_window(540, 5, window=self.widthS, anchor=Tkinter.NW)

        self.tools.create_text(690,30,text='Color', fill='slate gray')
        self.tools.create_oval(720, 15, 750, 45, fill='white', width=3)

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/finish.bmp')))
        self.tools.create_image(840, 15, image=self.labels[-1],anchor=Tkinter.NW)

        self.cv.bind('<Button-1>', self.press)
        self.cv.bind('<B1-Motion>', self.move)
        self.helper = Helper()

        self.root.mainloop()
    ###
    def press(self,e):
        self.helper.x = e.x
        self.helper.y = e.y

    def move(self, e):
        self.cv.create_line(self.helper.x,self.helper.y, e.x, e.y)
        self.helper.x = e.x
        self.helper.y = e.y

    def release(self, e):
        pass

    def hover(self, e):
        pass

Draw(640,480, 2, 1)
