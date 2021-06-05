# File : 6077.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-05
# Brief : 종합

n = int(input())
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i

print(sum)
