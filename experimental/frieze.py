import Tkinter

def repeat(cw, ch, r, s, (x, y)):
    # canvas width, canvas height, width:height ratio of cell,
    # symmetry type, (x,y) of mouse
    x %= int(ch * r)
    coords = []
    if s == 0:
        coords = [(x, y)]
        coords += [(x, ch - y-1)]
        coords += [(int(ch * r - i[0]-1), i[1]) for i in coords[-2:]]
        while coords[-1][0] < cw:
            coords += [(int(i[0]+ch*r), i[1]) for i in coords[-4:]]
    elif s==1:
        coords = [(x, y)]
        coords += [(int(ch*r-x-1), ch - y - 1)]
        while coords[-1][0] < cw:
            coords += [(int(ch*r+i[0]), ch - i[1] - 1) for i in coords[-2:]]
    return coords

def drawcircle(e):
    global c
    coords = repeat(600,60,1.5,1,(e.x,e.y))
    for i in coords:
        c.create_oval(i[0]-2,i[1]-2,i[0]+2,i[1]+2, fill='blue')

# print repeat(30, 3, 1, 1, (2,0))

wnd = Tkinter.Tk()
c = Tkinter.Canvas(wnd,width=600, height=60)
c.pack()
c.bind('<Button-1>',drawcircle)
wnd.mainloop()