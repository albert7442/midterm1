#迴文問題

a=input('輸入一字元為: ')
lf=''
rg=''

if len(a)%2==0:
    lf=a[0:len(a)//2]
    rg=a[len(a)//2:]
else:
    lf=a[0:(len(a)//2)]
    rg=a[(len(a)//2)+1:]

if rg==lf[::-1] or lf==rg[::-1]:
    print('YES')
else:
    print('NO')