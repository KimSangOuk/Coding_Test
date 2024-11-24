import sys
from bisect import bisect_left, bisect_right
input=sys.stdin.readline

n=int(input())
a,b,c,d=[],[],[],[]
for i in range(n):
    an,bn,cn,dn=map(int,input().split())
    a.append(an)
    b.append(bn)
    c.append(cn)
    d.append(dn)

plusAB=[]
plusCD=dict()
for i in range(n):
    for j in range(n):
        plusAB.append(a[i]+b[j])
        if c[i]+d[j] in plusCD:
            plusCD[c[i]+d[j]]+=1
        else:
            plusCD[c[i]+d[j]]=1

cnt=0
for k in plusAB:
    if -k in plusCD:
        cnt+=plusCD[-k]

print(cnt)