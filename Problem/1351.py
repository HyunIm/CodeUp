# File  : 1351.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

a, b = map(int, input().split())
n = [str(j)+'*'+str(i)+'='+str(i*j) for j in range(a, b+1) for i in range(1,10)]
for i in n:
    print(i)
