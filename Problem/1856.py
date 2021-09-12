# File : 1856.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

m = {1:1, 2:2, 3:4}
def f(x):
    if x in m: return m[x]
    else:
        m[x] = f(x-1)+f(x-2)+f(x-3)
        return m[x]

print(f(int(input())))
