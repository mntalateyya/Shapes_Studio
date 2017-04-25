from ImageWriter import *
#FIND WIDTH OF THE IMAGE,FIND HEIGHT OF THE IMAGE,GO THROUGH EACH PIXEL,FIND THE AVERAGE COLOR OF EACH PIXEL,CHANGE IT TO WHITE OR BLACK IF AVERAGE IS GREATER OR LESS THAN 125,UPDATE PICTURE
pic=loadPicture("p1.jpg")
def convertBlackWhite(pic):
    rows = getHeight(pic)  # FIND THE HIEGHT OF THE IMAGE
    columns = getWidth(pic) # FIND THE WIDTH OF THE IMAGE
    for i in range(0,rows): # GOING THROUGHT EVERY ROW
        for j in range(0,columns): #GOING THROUGH EVERY COLOUMN
            c = getColor(pic,j,i)  #GETTING THE COLOR OF THE PIXELS
            if sum(c)/3 >= 100:    #FINDING THE AVERAGE
                setColor(pic,j,i,[255,255,255]) #SET THE COLOR TO WHITE
            else:
                setColor(pic,j,i,[0,0,0]) #SET THE COLOR TO BLACK
        showPicture(pic)
        
convertBlackWhite(pic)
savePicture(pic,"sav.jpg")
