# File  : 1675.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

s = input()
a = []
for i in s:
    if i==' ':
        a.append(i)
    elif i=='a' or i=='b' or i=='c':
        i = 'x' if i=='a' else 'y' if i=='b' else 'z'
        a.append(i)
    else:
        a.append(chr(ord(i)-3))
print(''.join(a))
