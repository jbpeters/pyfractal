import math as M
PI=M.pi

def Make_color(Max_iter,frequency,count):
    w=[]
    d=[]
    value=[]
    for hue in range(3):
        w.append(frequency[hue]*PI/Max_iter)
        d.append(w[hue]*Max_iter+PI)
        value.append(int(255/2.0*(1+M.cos(w[hue]*count-d[hue]))))
    return(value)


#print Make_color(1024,(3,7,9),1024)

