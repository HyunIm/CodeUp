# File : 1285.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

n = input()
s = ['+', '-', '*', '/']
a = []
result = 0
j = '+'
for i in n:
    if i=='=':
        break

    if i in s:
        result = int(eval(str(result) + j + ''.join(a)))
        a = []
        j = i
    else:
        a.append(i)

result = int(eval(str(result) + j + ''.join(a)))
print(result)
