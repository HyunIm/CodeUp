# File : 1216.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-15
# Brief : 조건문

a, b, c = map(int, input().split())
print('삼각형아님' if a+b<=c else '정삼각형' if a==c else '이등변삼각형' if a==b or b==c else '직각삼각형' if a**2+b**2==c**2 else '삼각형')
