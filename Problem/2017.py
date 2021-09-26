# File : 2017.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-26
# Brief : 중급

import string

s = string.digits+string.ascii_uppercase
def f(n, k):
    q, r= divmod(n, k)
    if q==0: return s[r]
    else: return f(q, k) + s[r]

n, k = map(int, input().split())
print(f(n, k))
