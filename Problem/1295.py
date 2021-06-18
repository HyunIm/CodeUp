# File  : 1295.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

s = input()
r = []
for i in s:
    if i.isupper():
        r.append(i.lower())
    else:
        r.append(i.upper())
print(''.join(r))
