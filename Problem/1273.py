# File : 1273.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-17
# Brief : 단순 반복문

n = int(input())
a = [i for i in range(1, n+1) if n%i==0]
for i in a:
    print(i, end=' ')
