import pygame as P

def init(size,kolor ):
    P.display.init()
    S=P.display.set_mode((size),1)
    S.fill(kolor)
    P.display.flip() #redraw()
    return S
