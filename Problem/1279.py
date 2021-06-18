# File : 1279.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

a, b = map(int, input().split())
n = [i if i%2==1 else -i for i in range(a, b+1)]
print(sum(n))
