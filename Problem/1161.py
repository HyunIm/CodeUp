# File : 1161.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

a, b = map(int, input().split())
print('홀수' if a%2==1 else '짝수', '+', '홀수' if b%2==1 else '짝수', '=', '홀수' if (a+b)%2==1 else '짝수', sep='')
