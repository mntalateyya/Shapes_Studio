import Tkinter
from PIL import Image, ImageDraw, ImageTk
import Layer
import ChooseFrieze, L_sys_Main, DrawMain, ChooseWallpaper

class Meta:
    def __init__(self, i):
        self.instance = i
        self.im = Image.new('RGBA', (900, 600), 'white')
        self.layers = []
        self.layerscoords = []
        self.layer_thumb = []
        self.focus = -1

    def add_layer(self, im):
        if self.focus >-1:
            self.layer_thumb[self.focus].lose_focus()
        layer = Layer.Layer(im, self.instance.layers, self)
        self.layers = [im] + self.layers
        self.layerscoords = [(450,300)] + self.layerscoords
        self.layer_thumb = [layer] + self.layer_thumb
        layer.cv.pack()
        layer.change_focus()
        self.focus = self.layer_thumb.index(layer)
        self.instance.redraw()

    def change_focus(self, layer):
        self.layer_thumb[self.focus].lose_focus()
        if layer in self.layer_thumb:
            self.focus = self.layer_thumb.index(layer)
        elif self.layer_thumb:
            self.layer_thumb[0].change_focus()
            self.focus = 0
        else:
            self.focus = -1

    def del_layer(self, layer):
        i = self.layer_thumb.index(layer)
        self.layer_thumb[i].cv.pack_forget()
        self.layers.pop(i)
        self.layerscoords.pop(i)
        self.change_focus(layer)
        self.instance.redraw()


class Main:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.geometry('1080x680')

        self.meta = Meta(self)

        self.cmd = Tkinter.Frame(self.root, width=1080, height=60, bg='#dddddd')
        self.cmd.grid()

        self.f2 = Tkinter.Frame(self.root, width=1080, height=620)
        self.f2.grid(row=1,column=0)

        self.cv = Tkinter.Canvas(self.f2, bd=0, highlightthickness=0,
                    width=900, height=600, bg='white')
        self.cv.grid(row=0,column=0, padx=15, pady=15)

        self.cv.bind('<B1-Motion>', self.move_layer)
        self.cv.bind('<Button-1>', self.press)
        self.cv.bind('<ButtonRelease-1>', self.release)

        self.layers = Tkinter.Frame(self.f2, width=150, height=620)
        self.layers.grid(row=0, column=1)

        freedraw = Tkinter.Button(self.cmd, text='Add Free Drawing', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:DrawMain.Draw(0, 0, self.meta))
        freedraw.pack(side=Tkinter.LEFT, padx=5, pady=10)

        frieze = Tkinter.Button(self.cmd, text='Add Frieze', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:ChooseFrieze.ChooseFrieze(self.meta))
        frieze.pack(side=Tkinter.LEFT, padx=5, pady=10)

        wall = Tkinter.Button(self.cmd, text='Add Wallpaper', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda: ChooseWallpaper.ChooseWallpaper(self.meta))
        wall.pack(side=Tkinter.LEFT, padx=5, pady=10)

        frac = Tkinter.Button(self.cmd, text='Add L-fractal', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:L_sys_Main.Main(self.meta))
        frac.pack(side=Tkinter.LEFT, padx=5, pady=10)

        self.photos = []
        self.root.mainloop()


    def add_frac(self):
        pass

    def redraw(self):
        self.photos = []
        self.images = []
        for i in range(len(self.meta.layers)):
            self.photos.append(ImageTk.PhotoImage(self.meta.layers[i]))
            self.images.append(self.cv.create_image(self.meta.layerscoords[i][0],
                self.meta.layerscoords[i][1], image=self.photos[-1]))

    def press(self, e):
        if self.meta.layers:
            self.x = e.x
            self.y = e.y
            self.imcoords = self.meta.layerscoords[self.meta.focus]

    def move_layer(self, e):
        if self.meta.layers:
            dx = e.x - self.x
            dy = e.y - self.y
            self.cv.coords(self.images[self.meta.focus], self.imcoords[0]+dx, self.imcoords[1]+dy)

    def release(self, e):
        if self.meta.layers:
            self.meta.layerscoords[self.meta.focus] = self.imcoords[0]+e.x - self.x, self.imcoords[1]+e.y - self.y
            self.redraw()

if __name__ == '__main__':
    application = Main()
