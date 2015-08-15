import pygame as P
import mandelgrid
import mandelinit
P.init()

def kg():
    P.display.quit()

def redraw():
    P.display.flip()


def loop(center, radius,size ):
    print( "looping")
    Running = True
    while Running:
        for E in P.event.get():
            if E.type == P.KEYDOWN:
                if E.key == P.K_q:
                    Running = False
            if E.type == P.MOUSEBUTTONDOWN:
                i,j=P.mouse.get_pos()
                zx,zy=mandelgrid.gridtocomplex(center,radius,size,(i,j))    
                print zx,zy
                Running = False
    kg()
    return


