# File : 1990.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 문자열

from functools import reduce
n = input()
r = reduce(lambda x, y: y+x, map(int, n))
print(1 if r%3==0 else 0)
