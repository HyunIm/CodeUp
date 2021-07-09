# File : 1916.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

m={1:1,2:1}
def f(x) :
    if x in m: return m[x]
    m[x]=f(x-1)+f(x-2)
    return m[x]

print(f(int(input()))%10009)
