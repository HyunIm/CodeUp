# File : 2601.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-02
# Brief : 동적계획법

m = {1:1, 2:1}
def f(n):
    if n in m: return m[n]
    else:
        m[n] = f(n-1) + f(n-2)
        return m[n]
print(f(int(input())))
