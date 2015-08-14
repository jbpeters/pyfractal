#! /usr/bin/python
# vi:syntax=python

def gridtocomplex(center,radius,size,(i,j)):
    width,height = size
    if (width > height):
        b = radius
        a = radius*width/height
    elif(width< height): 
        a = radius
        b = radius*height/width
    else:
        a=b=radius
    x_guage=2*a/width
    y_guage=2*b/height

    x=center[0]-a+i*x_guage
    y=center[1]+b-j*y_guage
    return (x,y)


#   print gridtocomplex((0,0),10,(20,20), ( 0 , 0 ))

    
"""
def gridtocomplex(center,radius,size,(i,j)):
    width,height=size
    if(width >= height):
        pixelwidth=2*radius/height # b=radius ; a =radius*width/height
    else:
        pixelwidth=2*radius/width  # a=radius ; b=radius*height/width
    # x_gauge = 2*a/width
    # y_guage = 2*b/height
    # x=cx-a+i*x_guage 
    # y=cy+b-j*y_guage
    #print("pw=",pixelwidth)
    x=center[0]-( (width/2.0 )*   pixelwidth)+i*pixelwidth
    y=center[1]+( (height/2.0)*   pixelwidth)-j*pixelwidth
    return (x,y)

for j in reversed(range(10)):
    print("-------")
    for i in range(10):
        
        print("{:.1f}".format(gridtocomplex((0,0),2.0,(10,10),(i,j))[0]),"{:.1f}".format(gridtocomplex((0,0),2.0,(10,10),(i,j))[1])),

"""
