# File : 1163.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-13
# Brief : 조건문

y, m, d = map(int, input().split())
print('대박' if (((y+m+d)//100)%10)%2==0 else '그럭저럭')
