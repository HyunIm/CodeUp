# File : 1226.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 조건문

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a.pop()
cnt = 8
for i in range(6):
    if b[i] in a:
        cnt -= 1
print(0 if cnt >= 6 else 1 if cnt==2 else cnt-1 if cnt==3 and c in b else cnt)
