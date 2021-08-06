# File : 3127.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-06
# Brief : 스택

e = list(input().split())
c = ['+', '-', '*']
s = []
for i in e:
    if i in c: s.append((lambda x, y: str(eval(y+i+x)))(s.pop(), s.pop()))
    else: s.append(i)
print(s[0])
