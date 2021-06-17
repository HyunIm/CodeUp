# File : 1266.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-17
# Brief : 단순 반복문

n = input()
a = list(map(int, input().split()))
a = [i for i in a if i%5==0]
print(sum(a))
