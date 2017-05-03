import Tkinter
from PIL import Image, ImageDraw, ImageTk

# This class creates a thumbnail of a layer
class Layer:
    def __init__(self, im, frame, meta):
        self.meta = meta
        self.cv = Tkinter.Canvas(frame, width=120, height=40,
                    highlightthickness=0, bd=0, bg='#cccccc')
        self.bd = self.cv.create_rectangle(1, 1, 119, 39, width=2, outline='#777799')
        self.cv.bind('<Button-1>', lambda e: self.change_focus())
        w,h = im.size
        # resize image to fit thumbnail
        if w>h*1.5:
            self.im = im.copy().resize((int(float(w)/w*54), int(float(h)/w*54)),
                        Image.ANTIALIAS)
        else:
            self.im = im.copy().resize((int(float(w)/h*36)+1, int(float(h)/h*36)+1),
                        Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.im)
        self.cv.create_image(40,20, image=self.photo1)
        # draw delete icon
        self.photo2 = ImageTk.PhotoImage(Image.open('Resources/delete.bmp'))
        self.delete = self.cv.create_image(100, 20, image=self.photo2)
        self.cv.tag_bind(self.delete, '<ButtonRelease-1>', lambda e: self.meta.del_layer(self))

    # focus on this layer (changes border thickness)
    def change_focus(self):
        self.meta.change_focus(self)
        self.cv.itemconfig(self.bd, width=2, outline='#777799')

    # this layer loose focus
    def lose_focus(self):
        self.cv.itemconfig(self.bd, width=1, outline='#888888')
