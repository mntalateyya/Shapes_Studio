import Tkinter
from PIL import Image, ImageDraw, ImageTk
import frieze, wallpaper_patterns
import ColorPicker

# Looking at Shapes 62-238
# Term Project
# Mohammed Nurul Hoque - Mohammed Yusuf Ansari

# creator: Mohammed Nurul Hoque
# editors: Mohammed Nurul Hoque

# created on 22/4/2017
# last modified on 24/4/2017

class Helper:
    def __init__(self, im):
        self.x = 0
        self.y = 0
        self.coords = []
        self.coordsList = []
        self.im = im
        self.undostack = []
        self.redostack = []
    def new_im(self,im):
        im.save('test.png')
        self.redostack = []
        self.undostack.append(self.im)
        self.im = im
    def undo(self):
        if self.undostack:
            self.redostack.append(self.im)
            self.im = self.undostack.pop()
    def redo(self):
        if self.redostack:
            self.undostack.append(self.im)
            self.im = self.redostack.pop()


class Draw:
    def __init__(self, t, s, parent):
        self.root = Tkinter.Toplevel()
        self.parent = parent
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
        self.cvw = 900
        self.cvh = 120 if (t==2) else 600
        self.cv = Tkinter.Canvas(self.cframe, width=self.cvw,
                                height=self.cvh, bg='white')
        self.tools.pack()
        self.cv.pack(pady=20)

        self.labels = []
        self.ids = []

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/undo.bmp')))
        self.ids += [self.tools.create_image(15, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.undo())

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/redo.bmp')))
        self.ids += [self.tools.create_image(60, 15, image=self.labels[-1],anchor=Tkinter.NW)]
        self.tools.tag_bind(self.ids[-1], '<Button-1>', lambda e:self.redo())

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

        self.color = '#000000'

        self.tools.create_text(690,30,text='Color', fill='slate gray')
        self.colbox = self.tools.create_oval(720, 15, 750, 45, fill=self.color, width=3)
        self.tools.tag_bind(self.colbox, '<Button-1>', lambda e:
                                        ColorPicker.ColorPicker(self, self.color))

        self.labels.append(ImageTk.PhotoImage(Image.open('Resources/finish.bmp')))
        self.end = self.tools.create_image(840, 15, image=self.labels[-1],anchor=Tkinter.NW)
        self.tools.tag_bind(self.end, '<ButtonRelease-1>', self.finish)

        self.cv.bind('<Button-1>', self.press)
        self.cv.bind('<B1-Motion>', self.move)
        self.cv.bind('<ButtonRelease-1>', self.release)

        self.helper = Helper(Image.new('RGBA',(self.cvw, self.cvh), (255,255,255,0)))

        self.toolname = {'pen':0, 'line':1, 'curve':2, 'fill':3, 'eraser':4}
        self.tool = 0
        self.dot = self.tools.create_oval(162,47,168,53,
                    fill='#888888', width=0)
        self.width = self.widthS.get()

    def draw(self):
        self.cv.delete(Tkinter.ALL)
        self.labels.append(ImageTk.PhotoImage(self.helper.im))
        self.cv.create_image(0, 0, image=self.labels[-1],anchor=Tkinter.NW)
        self.grid()

    def undo(self):
        self.helper.undo()
        self.draw()

    def redo(self):
        self.helper.redo()
        self.draw()

    def changeColor(self, color):
        print color
        self.color = color
        self.colbox = self.tools.create_oval(720, 15, 750, 45, fill=self.color, width=3)
        self.tools.tag_bind(self.colbox, '<Button-1>', lambda e:
                                        ColorPicker.ColorPicker(self, self.color))

    def change_tool(self, t, x):
        self.tool = t
        self.tools.coords(self.dot,x-3,47,x+3,53)

    def fill(self, pic, color, target, x, y):
        if 0<x<self.cvw and 1<y<self.cvh:
            stack = [(x,y)]
            while stack:
                x,y = stack.pop()
                if 0<x<self.cvw and 1<y<self.cvh:
                    if pic[x, y]==target:
                        pic[x, y] = color
                        stack += [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def press(self,e):
        if self.type ==0:
            self.helper.x =e.x; self.helper.y=e.y
            self.helper.coords = [(e.x, e.y)]
        elif self.type ==1:
            self.helper.coords = wallpaper_patterns.repeat_wallpaper(self.cvw,self.cvh, 100, 60,
                                    self.sym, (e.x, e.y))
            if self.tool in [0,1,2,4]:
                self.helper.coordsList = self.helper.coords
        elif self.type == 2:
            self.helper.coords = frieze.repeat(self.cvw,self.cvh, 1.5,
                                    self.sym, (e.x, e.y))
            if self.tool in [0,1,2,4]:
                self.helper.coordsList = self.helper.coords
        self.width = self.widthS.get()

    def move(self, e):
        if self.type == 0:
            if self.tool == self.toolname['pen']:
                self.cv.create_line(self.helper.x,self.helper.y,
                 e.x,e.y,width=self.width,
                fill=self.color, tag='temp')
                self.helper.x =e.x; self.helper.y=e.y
                self.helper.coords.append((e.x, e.y))
            elif self.tool == self.toolname['line']:
                self.cv.delete('temp')
                self.cv.create_line(self.helper.x,self.helper.y, e.x,e.y,width=self.width,
                fill=self.color, tag='temp')
            elif self.tool == self.toolname['eraser']:
                self.cv.create_line(self.helper.x,self.helper.y,
                 e.x,e.y,width=self.width,
                fill='#ffffff', tag='temp')
                self.helper.x =e.x; self.helper.y=e.y
                self.helper.coords.append((e.x, e.y))

        if self.type == 1:
            try:
                if self.tool == self.toolname['pen']:
                    coords = wallpaper_patterns.repeat_wallpaper(self.cvw, self.cvh, 100, 60,
                                            self.sym, (e.x, e.y))
                    for i in range(len(coords)):
                        self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                            coords[i][0],coords[i][1], width=self.width,
                                            fill=self.color, tag='temp')
                        self.helper.coordsList[i] += coords[i]

                    self.helper.coords = coords
                elif self.tool == self.toolname['line']:
                    self.cv.delete('temp')
                    coords = wallpaper_patterns.repeat_wallpaper(self.cvw, self.cvh, 100, 60,
                                            self.sym, (e.x, e.y))
                    for i in range(len(coords)):
                        self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                            coords[i][0],coords[i][1], width=self.width,
                                            fill=self.color, tag='temp')
                elif self.tool == self.toolname['eraser']:
                    coords = wallpaper_patterns.repeat_wallpaper(self.cvw, self.cvh, 100, 60,
                                            self.sym, (e.x, e.y))
                    for i in range(len(coords)):
                        self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                            coords[i][0],coords[i][1], width=self.width,
                                            fill='white', tag='temp')
                        self.helper.coordsList[i] += coords[i]

                    self.helper.coords = coords
            except:
                pass

        if self.type == 2:
            if self.tool == self.toolname['pen']:
                coords = frieze.repeat(self.cvw, self.cvh, 1.5,
                                        self.sym, (e.x, e.y))
                for i in range(len(coords)):
                    self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                        coords[i][0],coords[i][1], width=self.width,
                                        fill=self.color, tag='temp')
                    self.helper.coordsList[i] += coords[i]

                self.helper.coords = coords
            elif self.tool == self.toolname['line']:
                self.cv.delete('temp')
                coords = frieze.repeat(self.cvw, self.cvh, 1.5,
                                        self.sym, (e.x, e.y))
                for i in range(len(coords)):
                    self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                        coords[i][0],coords[i][1], width=self.width,
                                        fill=self.color, tag='temp')
            elif self.tool == self.toolname['eraser']:
                coords = frieze.repeat(self.cvw, self.cvh, 1.5,
                                        self.sym, (e.x, e.y))
                for i in range(len(coords)):
                    self.cv.create_line(self.helper.coords[i][0],self.helper.coords[i][1],
                                        coords[i][0],coords[i][1], width=self.width,
                                        fill='white', tag='temp')
                    self.helper.coordsList[i] += coords[i]

                self.helper.coords = coords

    def release(self, e):
        im = self.helper.im.copy()
        draw = ImageDraw.Draw(im)
        if self.type==0:
            if self.tool == self.toolname['pen']:
                draw.line(self.helper.coords, fill=str2hex(self.color)
                , width=self.width)
            elif self.tool == self.toolname['line']:
                draw.line((self.helper.x, self.helper.y, e.x, e.y),
                fill=str2hex(self.color), width=self.width)
            elif self.tool == self.toolname['eraser']:
                draw.line(self.helper.coords, fill=(255,255,255,0)
                , width=self.width)
            elif self.tool == self.toolname['fill']:
                pic = im.load()
                self.fill(pic, str2hex(self.color), pic[e.x, e.y], e.x, e.y)

        if self.type==1:
            try:
                if self.tool == self.toolname['pen']:
                    for i in range(len(self.helper.coordsList)):
                        draw.line(self.helper.coordsList[i], fill=str2hex(self.color)
                        , width=self.width)
                elif self.tool == self.toolname['line']:
                    coords = wallpaper_patterns.repeat_wallpaper(self.cvw, self.cvh, 100, 60,
                                            self.sym, (e.x, e.y))
                    for i in range(len(coords)):
                        draw.line((self.helper.coords[i][0],self.helper.coords[i][1],
                                                coords[i][0],coords[i][1]), width=self.width,
                                                fill=str2hex(self.color))
                elif self.tool == self.toolname['fill']:
                    coords = wallpaper_patterns.repeat_wallpaper(self.cvw, self.cvh, 100, 60,
                                            self.sym, (e.x, e.y))
                    pic = im.load()
                    target = pic[e.x, e.y]
                    for i in range(len(coords)):
                        self.fill(pic, str2hex(self.color), target,
                                    coords[i][0], coords[i][1])
                elif self.tool == self.toolname['eraser']:
                    for i in range(len(self.helper.coordsList)):
                        draw.line(self.helper.coordsList[i], fill=(255,255,255,0), width=self.width)
            except:
                pass

        if self.type==2:
            if self.tool == self.toolname['pen']:
                for i in range(len(self.helper.coordsList)):
                    draw.line(self.helper.coordsList[i], fill=str2hex(self.color)
                    , width=self.width)
            elif self.tool == self.toolname['line']:
                coords = frieze.repeat(self.cvw, self.cvh, 1.5,
                                        self.sym, (e.x, e.y))
                for i in range(len(coords)):
                    draw.line((self.helper.coords[i][0],self.helper.coords[i][1],
                                            coords[i][0],coords[i][1]), width=self.width,
                                            fill=str2hex(self.color))
            elif self.tool == self.toolname['fill']:
                coords = frieze.repeat(self.cvw, self.cvh, 1.5,
                                        self.sym, (e.x, e.y))
                pic = im.load()
                target = pic[e.x, e.y]
                for i in range(len(coords)):
                    self.fill(pic, str2hex(self.color), target,
                                coords[i][0], coords[i][1])
            elif self.tool == self.toolname['eraser']:
                for i in range(len(self.helper.coordsList)):
                    draw.line(self.helper.coordsList[i], fill=(255,255,255,0), width=self.width)
        self.helper.new_im(im)
        self.draw()

    def hover(self, e):
        pass

    def grid(self):
        pass

    def finish(self, e):
        self.parent.add_layer(self.helper.im)
        self.root.destroy()

def str2hex(s):
    return (int(s[1:3],16), int(s[3:5],16), int(s[5:7],16))
