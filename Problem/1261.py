# File : 1261.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

n = list(map(int, input().split()))
n = [i for i in n if i%5==0]
print(0 if not n else n[0])
