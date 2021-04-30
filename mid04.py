#階層判斷

def f(x):
    n=k=1
    while k<=x:
        n*=k
        k+=1
    return n

M=int(input('請輸入階層值M : '))

n=1
while True:
    k=f(n)
    if k>M:
        print(f'超過M為{M}的最小階層N值為 : {n}')
        break
    else:
        n+=1