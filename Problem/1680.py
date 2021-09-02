# File : 1680.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-02
# Brief : 기초

for t in range(0, 1000, 100):
    for s in range(0, 100, 10):
        for o in range(10):
            if 2*(s+o) == t+10*o+o:
                if s!=o!=t:
                    print(s+o,'+',s+o,'=',t+10*o+o, sep='')
