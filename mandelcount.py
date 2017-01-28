power=2
def z_count(z, dist, Max_iter ):
    count=0
    zz=complex(z)
    z=complex(0,0)
    while(count < Max_iter and abs(z)< dist):
        nz=(z**power + zz)
        z=nz
        count+=1
    return(count)

    
