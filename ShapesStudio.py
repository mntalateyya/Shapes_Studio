import Tkinter
from PIL import Image, ImageDraw, ImageTk
import Layer
import ChooseFrieze, L_sys_Main

class Meta:
    def __init__(self, i):
        self.instance = i
        self.im = Image.new('RGBA', (900, 600), 'white')
        self.layers = []
        self.layer_thumb = []

    def add_layer(self, im):
        layer = Layer.Layer(im, self.instance.layers, self)
        self.layers = [im] + self.layers
        self.layer_thumb = [layer] + self.layer_thumb
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

        self.layers = Tkinter.Frame(self.f2, width=150, height=620)
        self.layers.grid(row=0, column=1)

        freedraw = Tkinter.Button(self.cmd, text='Add Free Drawing', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:0)
        freedraw.pack(side=Tkinter.LEFT, padx=5, pady=10)

        frieze = Tkinter.Button(self.cmd, text='Add Frieze', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:ChooseFrieze.ChooseFrieze())
        frieze.pack(side=Tkinter.LEFT, padx=5, pady=10)

        wall = Tkinter.Button(self.cmd, text='Add Wallpaper', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:0)
        wall.pack(side=Tkinter.LEFT, padx=5, pady=10)

        frac = Tkinter.Button(self.cmd, text='Add L-fractal', bg='#cccccc',
                    relief=Tkinter.FLAT, command=lambda:L_sys_Main.Main(self.meta))
        frac.pack(side=Tkinter.LEFT, padx=5, pady=10)


        self.root.mainloop()


    def add_frac(self):
        pass

    def redraw(self):
        pass


if __name__ == '__main__':
    application = Main()
