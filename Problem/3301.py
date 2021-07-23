# File : 3301.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-23
# Brief : 그리디

n = int(input())
a = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
c = 0
for i in a:
    c += n//i
    n %= i
print(c)
