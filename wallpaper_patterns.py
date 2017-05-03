import Tkinter
from math import *

# routines to calculate for each point in canvas, the corresponding points
# in the whole wallpaper

def repeat_wallpaper(cw, ch, cell_w,cell_h, s, (x, y)):
    # canvas width, canvas height, width:height ratio of cell,
    # symmetry type, (x,y) of mouse
    coords = []
    if s == 0:  # p1
        if y%(2*cell_h)<cell_h:
            x = x%int(cell_w)-int(0.5*cell_w)
        else:
            x = x%int(cell_w)
        y %= int(cell_h)
        coords = [(x, y)]
        for j in range(cw/cell_w+1):
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
            x = x%int(cell_w)-int(0.5*cell_w)
        else:
            x = x%int(cell_w)
        y %= int(cell_h)
        coords = [(x, y)]
        coords += [(cell_w-x-1, y)]
        for j in range(cw/cell_w+2):
            coords += [(int(i[0] + cell_w), i[1]) for i in coords[-2:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            if(i%2==0):
                coords1 +=[(e[0]-int(0.5*cell_w),int(e[1]+(cell_h*i))) for e in coords]
            if(i%2==1):
                coords1 +=[(e[0]-cell_w,int(e[1]+(cell_h*i))) for e in coords]

    if s == 2:  # p2
        if y%(2*cell_h)<cell_h:
            x = (x%int(cell_w)-int(0.5*cell_w))%cell_w
        else:
            x = x%int(cell_w)
        y %= int(cell_h)
        coords = [(x, y)]
        coords += [(int( cell_w - i[0] - 1), int(cell_h - i[1] -1)) for i in coords[-1:]]

        for j in range(cw/cell_w+1):
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
        for j in range(cw/cell_w/2+1):
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
        for j in range(cw/cell_w/2+1):
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
        for j in range(cw/cell_w+1):
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

        for j in range(cw/cell_w/2+1):
            coords += [(int(i[0] + 2*cell_w), i[1]) for i in coords[-8:]]

        count=int(ceil(float(ch)/cell_h))
        coords1 = []
        for i in range(count):
            coords1 +=[(e[0],int(e[1]+(2*cell_h*i))) for e in coords]
    return coords1
