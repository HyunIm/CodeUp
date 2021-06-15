# File : 1224.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-15
# Brief : 조건문

a, b, c, d = map(int, input().split())
print('>' if a/b>c/d else '=' if a/b==c/d else '<')
