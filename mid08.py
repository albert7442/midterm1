#字根與子字串

import re

s1=input('輸入s1為:')
s2=input('輸入s2為:')

if re.match(f'^.*{s1}.*$',s2):
    print('YES')
else:
    print('NO')