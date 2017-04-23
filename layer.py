import Tkinter
from PIL import Image, ImageDraw, ImageTk

class Layer:
    def __init__(self, im, parent, meta):
        self.cv = Tkinter.Canvas(parent, width=120, height=40,
                    highlightthickness=0, bd=0, bg='#cccccc')
        self.cv.create_rectangle(1, 1, 119, 39, width=2, outline='#888888')
        w,h = im.size
        if w>h*1.5:
            self.im = im.copy().resize((int(float(w)/w*54), int(float(h)/w*54)),
                        Image.ANTIALIAS)
        else:
            self.im = im.copy().resize((int(float(w)/h*36), int(float(h)/h*36)),
                        Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.im)
        self.cv.create_image(40,20, image=self.photo1)
        self.photo2 = ImageTk.PhotoImage(Image.open('Resources/delete.bmp'))
        self.delete = self.cv.create_image(100, 20, image=self.photo2)

wnd = Tkinter.Tk()
im = Image.new("RGB", (500, 100), "red")
c = Layer(im, wnd, None)
c.cv.pack()
wnd.mainloop()
