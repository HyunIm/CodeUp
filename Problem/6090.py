# File : 6090.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-07
# Brief : 종합

a, m, d, n = map(int, input().split())

for _ in range(0, n - 1):
    a = a * m + d
print(a)

# print(round(((a - (d / (1 - m))) * (m ** (n - 1))) + (d / (1 - m))) if m != 1 else (a + (d * (n - 1))))
# print(round(((m**n)*(a*m+d-a)-d*m)/((m**2)-m)))
