import Tkinter
from math import *


def repeat_wallpaper(cw, ch, cell_w,cell_h, s, (x, y)):
    # canvas width, canvas , vell width, cell height, mode
    # symmetry type, (x,y) of mouse
    coords = []
    if s == 0:  # p1
        if y%(2*cell_h)<cell_h:
            x = x%int(cell_w)-int(0.5*cell_w)
        else:
            x = x%int(cell_w)
        y %= int(cell_h)
        coords = [(x, y)]
        while coords[-1][0] < cw+1:
            coords += [(int(i[0] + cell_w), i[1]) for i in coords[-1:]]
            
        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            if(i%2==0):
                coords1 +=[(e[0]-int(0.5*cell_w),int(e[1]+(cell_h*i))) for e in coords]
            if(i%2==1):
                coords1 +=[(e[0],int(e[1]+(cell_h*i))) for e in coords]

    if s == 1:  # cm
        if y%(2*cell_h)<cell_h:
            x = x%int(2*cell_w)-int(0.5*cell_w)
        else:
            x = x%int(2*cell_w)
        y %= int(cell_h)
        coords = [(x, y)]
        coords += [(int( 2*cell_w - i[0] - 1), i[1]) for i in coords[-1:]]
        while coords[-1][0] < cw+1:
            coords += [(int(i[0] + cell_w), i[1]) for i in coords[-2:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            if(i%2==0):
                coords1 +=[(e[0]-int(0.5*cell_w),int(e[1]+(cell_h*i))) for e in coords]
            if(i%2==1):
                coords1 +=[(e[0],int(e[1]+(cell_h*i))) for e in coords]

    if s == 2:  # p2
        if y%(2*cell_h)<cell_h:
            x = (x%int(cell_w)-int(0.5*cell_w))%cell_w
        else:
            x = x%int(cell_w)
        y %= int(cell_h)
        coords = [(x, y)]
        coords += [(int( cell_w - i[0] - 1), int(cell_h - i[1] -1)) for i in coords[-1:]]

        while coords[-1][0] < cw+1:
            coords += [(int(i[0] + cell_w), i[1]) for i in coords[-2:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            if(i%2==0):
                coords1 +=[(e[0]-int(0.5*cell_w),int(e[1]+(cell_h*i))) for e in coords]
            if(i%2==1):
                coords1 +=[(e[0],int(e[1]+(cell_h*i))) for e in coords]
                
    if s == 3:  # pmm
        x = x%int(2*cell_w)
        y = y%int(2*cell_h)
        coords = [(x, y)]
        coords += [(x, 2*cell_h - y - 1)]
        coords += [(int(2*cell_w - i[0] - 1), i[1]) for i in coords[-2:]]
        while coords[-1][0] < cw:
            coords += [(int(i[0] + 2*cell_w), i[1]) for i in coords[-4:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            coords1 +=[(e[0],int(e[1]+(2*cell_h*i))) for e in coords]
        
        
    if s == 4:  # pm
        
        x = x%int(2*cell_w)
        y = y%int(cell_h)
        coords = [(x, y)]
        coords += [(int( 2*cell_w - i[0] - 1), i[1]) for i in coords[-1:]]
        while coords[-1][0] < cw:
            coords += [(int(i[0] + 2*cell_w), i[1]) for i in coords[-2:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            coords1 +=[(e[0],int(e[1]+(cell_h*i))) for e in coords]
        
        
    if s == 5:  # pmg    
        x = x%int(2*cell_w)
        y = y%int(cell_h)
        coords = [(x, y)]
        coords += [(int(cell_w - x - 1), cell_h - y - 1)]
        while coords[-1][0] < cw+1:
            coords += [(int(cell_w + i[0]), cell_h - i[1] - 1) for i in coords[-2:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            coords1 +=[(e[0],int(e[1]+(cell_h*i))) for e in coords]


    if s == 6:  #cmm
        x = x%int(2*cell_w)
        y = y%int(2*cell_h)
        coords = [(x, y)]
        coords += [(int( cell_w - i[0] - 1), int(cell_h - i[1] -1)) for i in coords[-1:]]
        coords += [(i[0], int(2*cell_h - i[1] -1)) for i in coords[-2:]]
        coords += [(int(2*cell_w - i[0] -1), i[1]) for i in coords[-4:]]

        while coords[-1][0] < cw+1:
            coords += [(int(i[0] + 2*cell_w), i[1]) for i in coords[-8:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            coords1 +=[(e[0],int(e[1]+(2*cell_h*i))) for e in coords]
        
        
        
        
    return coords1        


def drawcircle(e):
    global c
    coords = repeat_wallpaper(800, 800, 100, 100, 6, (e.x, e.y))
    for i in coords:
        c.create_oval(i[0] - 2, i[1] - 2, i[0] + 2, i[1] + 2, fill='blue')


print repeat_wallpaper(12, 12, 4, 4, 4,(0, 0))
# '''
wnd = Tkinter.Tk()
c = Tkinter.Canvas(wnd, width=800, height=800)
c.pack()
c.bind('<Button-1>', drawcircle)
c.create_line(100,0,100,800)
c.create_line(200,0,200,800)
c.create_line(300,0,300,800)
c.create_line(400,0,400,800)
c.create_line(500,0,500,800)
c.create_line(600,0,600,800)
c.create_line(700,0,700,800)
for i in range(8):
    c.create_line(0,100*i,800,100*i)
for j in range(6):
    c.create_line(100*i,0,100*i,600)
wnd.mainloop()  # '''
