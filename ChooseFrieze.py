import Tkinter
from PIL import ImageTk, Image
import DrawMain

class ChooseFrieze:
    def __init__(self, parent):
        self.root = Tkinter.Toplevel()
        self.cv = Tkinter.Canvas(self.root, width=521, height=400, highlightthickness=0, bd=0)
        self.cv.pack()
        photos=[]
        ids=[]

        photos.append(ImageTk.PhotoImage(Image.open('Resources/fpmm2.bmp')))
        ids.append(self.cv.create_image(3,3, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(131, 90, text='pmm2', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:DrawMain.Draw(2, 0, parent))


        photos.append(ImageTk.PhotoImage(Image.open('Resources/fpma2.bmp')))
        ids.append(self.cv.create_image(262,3, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(390, 90, text='pma2', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:DrawMain.Draw(2, 1, parent))

        photos.append(ImageTk.PhotoImage(Image.open('Resources/fp112.bmp')))
        ids.append(self.cv.create_image(3,100, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(131, 190, text='p112', fill='slate gray')

        photos.append(ImageTk.PhotoImage(Image.open('Resources/fp1m1.bmp')))
        ids.append(self.cv.create_image(262,100, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(390, 190, text='p1m1', fill='slate gray')

        photos.append(ImageTk.PhotoImage(Image.open('Resources/fpm11.bmp')))
        ids.append(self.cv.create_image(3,200, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(131, 290, text='pm11', fill='slate gray')

        photos.append(ImageTk.PhotoImage(Image.open('Resources/fp111.bmp')))
        ids.append(self.cv.create_image(262,200, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(390, 290, text='p111', fill='slate gray')

        photos.append(ImageTk.PhotoImage(Image.open('Resources/fp1a1.bmp')))
        ids.append(self.cv.create_image(136,300, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(256, 390, text='p1a1', fill='slate gray')
        self.root.mainloop()
