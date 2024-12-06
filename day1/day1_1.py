import sys
l,r=[],[]
for line in sys.stdin:
    x,y=map(int,line.split())
    l.append(x)
    r.append(y)
l.sort()
r.sort()
print(sum([abs(l[i]-r[i]) for i in range(len(l))]))
