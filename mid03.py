#2D座標判斷及計算原點距離
import math
x=int(input('x座標 ->'))
y=int(input('y座標 ->'))

dis=f'離原點距離為根號{(x-0)**2+(y-0)**2}'

if x==0 and y==0:
    print('該點位於原點')
elif x>0 and y>0:
    print(f'該點位於第一象限,{dis}')
elif x<0 and y>0:
    print(f'該點位於第二象限,{dis}')
elif x<0 and y<0:
    print(f'該點位於第三象限,{dis}')
elif x>0 and y<0:
    print(f'該點位於第四象限,{dis}')
elif x==0 and y>0:
    print(f'該點位於上半平面y軸上,{dis}')
elif x==0 and y<0:
    print(f'該點位於下半平面y軸上,{dis}')
elif x>0 and y==0:
    print(f'該點位於右半平面x軸上,{dis}')
elif x<0 and y==0:
    print(f'該點位於左半平面x軸上,{dis}')