#過半元素
m=input('輸入第一整數序列為:').split(' ')
w={}
g=0

for i in m:
    if i in w:
        w[i]+=1
    else:
        w[i]=1

out=''
for w,v in w.items():
    if v>len(m)/2:
        out=f'過半元素為 : {w}'
        break
    else:
        out='NO'

print(out)