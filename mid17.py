#親骨肉判斷

n=int(input('測試的資料量: '))

for k in range(n):
    k=input('請依父、母、子女順序輸入: ').split(' ')
    if k[0]=='O':
        if k[1]=='O':
            if k[2]!='O':
                print('\nIMPOSSIBLE\n')
            else:
                print('\nYES\n')
        if k[1]=='A':
            if k[2] =='A' or k[2] =='O':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
        if k[1]=='B':
            if k[2] =='B' or k[2] =='O':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
        if k[1]=='AB':
            if k[2] =='A' or k[2] =='B':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
    elif k[0]=='A':
        if k[1]=='A':
            if k[2] =='A' or k[2] =='O':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
        elif k[1]=='B':
            print('\nYES\n')
        elif k[1]=='AB':
            if k[2] =='A' or k[2] =='B' or k[2]=='AB':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
    elif k[0]=='B':
        if k[1]=='B':
            if k[2] =='B' or k[2] =='O':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
        elif k[1]=='AB':
            if k[2] =='A' or k[2] =='B' or k[2]=='AB':
                print('\nYES\n')
            else:
                print('\nIMPOSSIBLE\n')
    elif k[0]=='AB':
        if k[1]=='AB':
            if k[2]=='O':
                print('\nIMPOSSIBLE\n')
            else:
                print('YES')
