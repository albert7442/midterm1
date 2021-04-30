n = int(input("請輸入陣列大小:"))
ar = [[0]*n for i in range(n)]
for i in range(n):
    w = input().split(" ")
    for k in range(n):
        ar[i][k] = int(w[k])
ind = []
cs = 0
for w in range(3): 
    temp = 0
    x = 0
    y = 0
    for i in range(3):
        for k in range(3):
            if ar[i][k] > temp:
                temp = ar[i][k]
                x = i
                y = k
    cs += temp
    ind.append("(" + str(x+1) + "," + str(y+1) + ")")
    ar[x][y] = 0
print("最大值為:%d" %(cs))
print("位置為:%s" %(",".join(ind)))