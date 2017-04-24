#   Color picker module
#   Code designed by: Mohammed Nurul Hoque (andrewID: mnurulho)
#
#   15-112: Principles of Programming and Computer Science at Carnegie Mellon University in Qatar
#   Term Project
#
#   File created on: Sunday 13 of November 2016, 09:03 PM
#   Modification History
#   Start:          End:
#   13/11/16 09:03  13/11/16 09:00
#   17/11/16 17:45  17/11/16 18:02
#   24/11/16 12:20  24/11/16 12:30

import Tkinter
from PIL import Image,ImageTk

# This module contains a class and functions for picking a color
# from a window, changes the color of the drawer class

class ColorPicker:
    def __init__(self,master, color):
        # create window and pack a canvas in its entirety
        self.root = Tkinter.Toplevel()
        self.root.grab_set()
        self.root.resizable(width=False, height=False)
        self.canvas = Tkinter.Canvas(self.root,bg='#cccccc', width=400,height=270)
        self.canvas.pack()

        # RGB values to iterate and gerneate colors
        self.red,self.green,self.blue = [255]*3 # tuple format of color
        self.color = color

        # box showing the currently picked color
        self.colorBox = self.canvas.create_rectangle(310,120,390,200,outline = '#888888', fill = self.color)

        # ok button
        self.ok = ImageTk.PhotoImage(Image.open('Resources/ok.bmp'))
        okButton = self.canvas.create_image(350,235,image=self.ok)
        self.canvas.tag_bind(okButton,'<ButtonRelease-1>',lambda e: OKColor(self.color,self,master))

        # generate 64 colors
        colors = []
        for i in [0,64,128,255]:
            for j in [0,64,128,255]:
                for k in [0,64,128,255]:
                    colors.append((i,j,k))

        # create rectangles for each of 64 colors
        i = 0
        for y in [0,1,2,3]:
            for x in range(16):
                color = '#'+hex(colors[i][0])[2:].rjust(2,'0')+hex(colors[i][1])[2:].rjust(2,'0')+\
                        hex(colors[i][2])[2:].rjust(2,'0')
                box = self.canvas.create_rectangle(x*25+5,y*25+2,x*25+25,y*25+22,fill=color,outline='#00a2e8')
                self.canvas.tag_bind(box,'<Button-1>',lambda e,i=i: self.changeColor(colors[i]))
                i+=1

        # create 17 shades of each of R, G, and B for currently selected color
        self.redLabels = [0]*17
        self.greenLabels = [0] * 17
        self.blueLabels = [0] * 17
        self.canvas.create_text(20,145,text='R')
        for i in range(17):  # Red shades
            color = '#'+hex(i*16 if i<16 else 255)[2:].rjust(2,'0')+hex(self.green)[2:].rjust(2,'0')+\
                    hex(self.blue)[2:].rjust(2,'0')
            self.redLabels[i] = self.canvas.create_rectangle(i*15+40,140,i*15+52,152,outline='#00a2e8',fill=color)
            self.canvas.tag_bind(self.redLabels[i],'<Button-1>'
                                 ,lambda e, i=i: self.changeColor((i*16 if i<16 else 255,self.green,self.blue)))
        self.canvas.create_text(20, 185, text='G')
        for i in range(17):  # Green shades
            color = '#'+hex(self.red)[2:].rjust(2,'0')+hex(i*16 if i<16 else 255)[2:].rjust(2,'0')+\
                    hex(self.blue)[2:].rjust(2,'0')
            self.greenLabels[i] = self.canvas.create_rectangle(i * 15 + 40, 180, i * 15 + 52, 192,
                                                               outline='#00a2e8',fill=color)
            self.canvas.tag_bind(self.greenLabels[i],'<Button-1>',
                                 lambda e, i=i: self.changeColor((self.red,i*16 if i<16 else 255,self.blue)))
        self.canvas.create_text(20, 225, text='B')
        for i in range(17):  # Blue shades
            color = '#'+hex(self.red)[2:].rjust(2,'0')+hex(self.green)[2:].rjust(2,'0')+\
                    hex(i*16 if i<16 else 255)[2:].rjust(2,'0')
            self.blueLabels[i] = self.canvas.create_rectangle(i*15+40,220,i*15+52,232,outline='#00a2e8',fill = color)
            self.canvas.tag_bind(self.blueLabels[i],'<Button-1>',
                                 lambda e, i=i: self.changeColor((self.red,self.green,i*16 if i<16 else 255)))

    # change selection to given color tuple
    def changeColor(self,color):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        # create string reresentation of color
        self.color = '#'+hex(color[0])[2:].rjust(2,'0')+hex(color[1])[2:].rjust(2,'0')+hex(color[2])[2:].rjust(2,'0')

        # redraw RGB shades to match the currently selected color
        for i in range(17):  # red shades
            color = '#'+hex(i*16 if i<16 else 255)[2:].rjust(2,'0')+hex(self.green)[2:].rjust(2,'0')+\
                    hex(self.blue)[2:].rjust(2,'0')
            self.canvas.itemconfig(self.redLabels[i],fill=color)
        for i in range(17):  # green shades
            color = '#'+hex(self.red)[2:].rjust(2,'0')+hex(i*16 if i<16 else 255)[2:].rjust(2,'0')+\
                    hex(self.blue)[2:].rjust(2,'0')
            self.canvas.itemconfig(self.greenLabels[i], fill=color)
        for i in range(17):  # blue shades
            color = '#'+hex(self.red)[2:].rjust(2,'0')+hex(self.green)[2:].rjust(2,'0')+\
                    hex(i*16 if i<16 else 255)[2:].rjust(2,'0')
            self.canvas.itemconfig(self.blueLabels[i], fill=color)
        self.canvas.itemconfig(self.colorBox,fill = self.color) # change color of selected color box

# close window and change color of the parent drawer class
def OKColor(color,window,master):
    window.root.destroy()
    master.changeColor(color)
