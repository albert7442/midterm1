#電影票購買計算
n=int(input('組數為: '))

for k in range(n):
    x=[int(i) for i in input(f'第{k+1}組為: ').split(' ')]
    print(f'第{k+1}組應收費用 {x[0]*250+x[1]*175}')