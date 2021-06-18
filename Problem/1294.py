# File  : 1294.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

s = input()
a = []
for i in s:
    if i==' ':
        a.append(i)
    elif i=='x' or i=='y' or i=='z':
        i = 'a' if i=='x' else 'b' if i=='y' else 'c'
        a.append(i)
    else:
        a.append(chr(ord(i)+3))
print(''.join(a))
