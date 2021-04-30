#找出數字字串中的最大質數

d=input()
d_substr=[d[i:j+1] for i in range(len(d)) for j in range(len(d)) if j>=i]
primes=[]

for k in d_substr:
    n=int(k)
    pm=[]
    for i in range(1,n+1):
        if n%i==0:
            pm.append(i)

    if len(pm)==2:
        primes.append(n)
            
if len(primes)!=0:
    print(max(primes))
else:
    print('No prime found')