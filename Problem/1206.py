# File : 1206.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-14
# Brief : 조건문

n = list(map(float, input().split()))
print('%d'%min(n)+'*%d'%(max(n)/min(n))+'=%d'%max(n) if max(n)%min(n)==0 else 'none')
