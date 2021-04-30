#兩數差值

n=input('輸入值為:').split(',')
k=[int(a) for a in n]

#a=1 =>由大到小排
#a=2 =>由小到大排
def f(x,a):
    g=0
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j]<x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]

    if a==2:
        x.reverse()

    for i in range(1,len(x)+1):
        n=x[i-1]*(10**(len(x)-i))
        g+=n
    return g

print(f'最大值數列與最小值數列差值為 :{f(k,1)-f(k,2)}')