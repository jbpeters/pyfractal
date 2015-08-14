import pygame as P

P.init()
    
def kg():
    P.display.quit()

def redraw():
    P.display.flip()


def loop():
    print( "looping")
    Running = True
    while Running:
        for E in P.event.get():
            if E.type == P.KEYDOWN:
                if E.key == P.K_q:
                    Running = False
            if E.type == P.MOUSEBUTTONDOWN:
                Running = False
    kg()
    return

