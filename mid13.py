#數字加密
k=[int(a) for a in input('輸入一組四位數為:')]
x=[(i+7)%10 for i in k]
x[0],x[1],x[2],x[3]=x[2],x[3],x[0],x[1]
out=''
for i in x:
    out+=str(i)
print(f'輸出加密後的數字為{out}')