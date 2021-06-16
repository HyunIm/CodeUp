# File : 1260.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

a, b = map(int, input().split())
a = a if a%3==0 else a+3-(a%3)
n = [i for i in range(a, b+1, 3)]
print(sum(n))
