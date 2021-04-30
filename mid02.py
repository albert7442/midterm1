#生肖
x=['rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig']
n=int(input())
#網路查得1900剛好為鼠年
print(x[(n-1900)%12])