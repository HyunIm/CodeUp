# File : 1166.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

n = int(input())
print('yes' if (n%4==0 and n%100!=0) or (n%400==0) else 'no')
