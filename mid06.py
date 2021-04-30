#通話費率

k=[int(a) for a in input('輸入月租費型式及通話時間為:').split(',')]

def f(n,i):
    k=0

    if i==186:
        k=n*0.09
        if k>186:
            k*=0.8
        else:
            k*=0.9
    elif i==386:
        k=n*0.08
        if k>386:
            k*=0.7
        else:
            k*=0.8
    elif i==586:
        k=n*0.07
        if k>586:
            k*=0.6
        else:
            k*=0.7
    elif i==986:
        k=n*0.06
        if k>986:
            k*=0.5
        else:
            k*=0.6
    
    return k

print(f'通話費為:{f(k[1],k[0])}')