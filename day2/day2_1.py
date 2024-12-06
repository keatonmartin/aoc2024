import sys
n=0
for l in sys.stdin:
    nums=list(map(int,l.split()))
    n+=1
    d=0
    for i in range(1, len(nums)):
        dd=nums[i]-nums[i-1]
        if not (1<=abs(dd)<=3) or (d<0 and dd>0) or (d>0 and dd<0):
            n-=1
            break
        d=dd
print(n)
