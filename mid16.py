#撲克牌13點

k=input('輸入五張牌:').split(' ')

for i in range(len(k)):
    if k[i]=='A':
        k[i]='14'
    elif k[i]=='J':
        k[i]='11'
    elif k[i]=='Q':
        k[i]='12'
    elif k[i]=='K':
        k[i]='13'

w=[int(n) for n in k]
print(sum(w))