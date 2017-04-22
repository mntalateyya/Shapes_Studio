import Tkinter


def repeat(cw, ch, r, s, (x, y)):
    # canvas width, canvas height, width:height ratio of cell,
    # symmetry type, (x,y) of mouse
    coords = []
    if s == 0:  # pmm2
        x %= int(ch * r)
        coords = [(x, y)]
        coords += [(x, ch - y - 1)]
        coords += [(int(ch * r - i[0] - 1), i[1]) for i in coords[-2:]]
        while coords[-1][0] < cw:
            coords += [(int(i[0] + ch * r), i[1]) for i in coords[-4:]]
    elif s == 1:  # pma2
        x %= int(ch * r)
        coords = [(x, y)]
        coords += [(int(ch * r - x - 1), ch - y - 1)]
        while coords[-1][0] < cw:
            coords += [(int(ch * r + i[0]), ch - i[1] - 1) for i in coords[-2:]]
    elif s == 2:  # p112
        x %= int(ch * r)
        coords = [(x, y)]
        coords += [(int(2 * ch * r - x) - 1, int(ch - y) - 1)]
        while coords[-1][0] < cw:
            coords += [(int(i[0] + 2 * ch * r), i[1]) for i in coords[-2:]]
    elif s == 3:  # p1m1
        x %= int(0.5 * ch * r)
        coords = [(x, y)]
        coords += [(x, ch - y - 1)]
        while coords[-1][0] < cw:
            coords += [(int(i[0] + 0.5 * ch * r), i[1]) for i in coords[-2:]]
    elif s==4:  # pm11
        x %= int(ch * r)
        coords = [(x, y)]
        coords += [(int(2*ch*r-x)-1, y)]
        while coords[-1][0] < cw:
            coords += [(int(i[0] + 2* ch * r), i[1]) for i in coords[-2:]]
    elif s==5:  # p111
        x %= int(ch * r)
        coords = [(x, y)]
        while coords[-1][0] < cw:
            coords += [(coords[-1][0]+int(ch*r), coords[-1][1])]
    elif s==6: # p1a1
        x %= int(ch * r)
        coords = [(x, y)]
        while coords[-1][0] < cw:
            coords += [(coords[-1][0]+int(ch*r), ch-coords[-1][1]-1)]

    return coords

