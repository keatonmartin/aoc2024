import sys
from collections import *
l,r=defaultdict(int),defaultdict(int)
for line in sys.stdin:
    x,y=map(int,line.split())
    l[x]+=1
    r[y]+=1
print(sum([r[k]*v*k for k,v in l.items()]))
