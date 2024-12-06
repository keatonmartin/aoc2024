import sys

def f(nums):
    d=0
    for i in range(1, len(nums)):
        dd=nums[i]-nums[i-1]
        if not (1<=abs(dd)<=3) or (d<0 and dd>0) or (d>0 and dd<0):
            return False
        d=dd
    return True
    
n=0
for l in sys.stdin:
    nums=list(map(int,l.split()))
    if any([f(nums[:i]+nums[i+1:]) for i in range(len(nums))]):
        n+=1

print(n)
