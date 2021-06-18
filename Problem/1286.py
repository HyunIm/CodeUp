# File  : 1286.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

n = []
for i in range(5):
    n.append(int(input()))
print(max(n), min(n), sep='\n')
