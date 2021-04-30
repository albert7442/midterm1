s1 = input("請輸入考試次數與學生數:").split(" ")
s2 = input("每次考試所佔的比率:").split(" ")
t = int(s1[0])
s = int(s1[1])
for i in range(len(s2)):
    s2[i] = float(s2[i])
st = [[0]*t for i in range(s)]
for i in range(s):
    w = input().split(" ")
    for k in range(t):
        st[i][k] = w[k]
sc = 0
for i in range(s):
    temp = 0
    for k in range(t):
        temp += int(st[i][k]) * s2[k]
    sc += temp
print("全班的總平均值:%0.2f" %(sc/s))