#學生資料搜尋

class student:
    def __init__(self,id,name,depart):
        self.id=id
        self.name=name
        self.depart=depart

d=[]
d.append(student(123,'Tom','DTGD'))
d.append(student(456,'Cat','CSIE'))
d.append(student(789,'Nana','ASIE'))
d.append(student(321,'Lim','DBA'))
d.append(student(654,'Won','FDD'))

k=int(input('請輸入查詢學號為: '))
out=''


for w in d:
    if k==w.id:
        out=f'學生資料為 {w.id} {w.name} {w.depart}'
        break
    else:
        out='未找到該學生'

print(out)