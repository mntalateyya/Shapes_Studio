import Tkinter
from globals import T_Gen
import Tree_Repr
import Event_Tree

T_Gen.wnd = Tkinter.Tk()
T_Gen.cv = Tkinter.Canvas(T_Gen.wnd, bg='white', width=600, height=400)
T_Gen.cv.pack()
d = 5
tree = Tree_Repr.Tree()
e_hand = Event_Tree.Ev_Handler(tree)
tree.draw()
T_Gen.cv.bind('<Button-1>', e_hand.on_click)
Tkinter.mainloop()
