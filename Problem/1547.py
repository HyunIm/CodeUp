# File : 1547.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

def prime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True
n = int(input())
print('prime' if prime(n) else 'composite')
