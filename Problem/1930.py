# File : 1930.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

m = {}
def f(k, n):
    if k==0: return n
    if (k, n) in m: return m[(k, n)]
    else:
        m[(k, n)] = 0
        for i in range(1, n+1):
            m[(k, n)] += f(k-1, i)
        return m[(k, n)]

while True:
    try: k, n = map(int, input().split())
    except: break
    print(f(k, n))
