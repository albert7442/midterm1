#檢查數值是否有重複
n=input('輸入第一行正整數為:')
k=[int(a) for a in input('輸入第二行中數列中的數字為:').split(' ')]
w={}
g=0

for i in k:
    if i in w:
        w[i]+=1
    else:
        w[i]=1

w_value=[]
for i in w.values():
    w_value.append(i)

if max(w_value)==1:
    print('每個數字剛好只出現一次')
else:
    for k,v in w.items():
        if v==max(w_value):
            print(f'最大出現次數的數字為{k}\n出現次數為{v}')
