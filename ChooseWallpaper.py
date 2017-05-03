import Tkinter
from PIL import ImageTk, Image
import DrawMain

# This class creates window that allows the user to choose a wallpaper pattern

class ChooseWallpaper:
    def __init__(self, meta):
        self.root = Tkinter.Toplevel()
        self.meta = meta
        self.cv = Tkinter.Canvas(self.root, width=521, height=710, highlightthickness=0, bd=0)
        self.cv.pack()
        photos=[]
        ids=[]

        photos.append(ImageTk.PhotoImage(Image.open('Resources/wp1.bmp')))
        ids.append(self.cv.create_image(3,3, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(131, 170, text='p1', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:self.start(0))


        photos.append(ImageTk.PhotoImage(Image.open('Resources/wcm.bmp')))
        ids.append(self.cv.create_image(262,3, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(390, 170, text='cm', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:self.start(1))

        photos.append(ImageTk.PhotoImage(Image.open('Resources/wp2.bmp')))
        ids.append(self.cv.create_image(3,180, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(131, 348, text='p2', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:self.start(2))

        photos.append(ImageTk.PhotoImage(Image.open('Resources/wpmm.bmp')))
        ids.append(self.cv.create_image(262,180, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(390, 348, text='pmm', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:self.start(3))

        photos.append(ImageTk.PhotoImage(Image.open('Resources/wpm.bmp')))
        ids.append(self.cv.create_image(3,358, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(131, 525, text='pm', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:self.start(4))

        photos.append(ImageTk.PhotoImage(Image.open('Resources/wpmg.bmp')))
        ids.append(self.cv.create_image(262,358, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(390, 525, text='pmg', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e:self.start(5))

        photos.append(ImageTk.PhotoImage(Image.open('Resources/wcmm.bmp')))
        ids.append(self.cv.create_image(136,533, image=photos[-1], anchor=Tkinter.NW))
        self.cv.create_text(256, 700, text='cmm', fill='slate gray')
        self.cv.tag_bind(ids[-1], '<Button-1>', lambda e: self.start(6))

        self.root.mainloop()

    def start(self, i):
        DrawMain.Draw(1, i, self.meta)
        self.root.destroy()
