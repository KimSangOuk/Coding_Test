import sys
from bisect import bisect_left

input=sys.stdin.readline

N=int(input())

arr=[]
allNum=set()

for _ in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))
    allNum.add((a,b))

arr.sort()

tails=[]
tails_idx=[]
prev_idx=[-1]*N

for i in range(N):
    num=arr[i][1]
    pos=bisect_left(tails,num)
    if pos==len(tails):
        tails.append(num)
        tails_idx.append(i)
    else:
        tails[pos]=num
        tails_idx[pos]=i
    if pos>0:
        prev_idx[i]=tails_idx[pos-1]

print(N-len(tails))
k=tails_idx[-1] if tails_idx else -1
while k!=-1:
    allNum.remove(arr[k])
    k=prev_idx[k]

for t in sorted(allNum):
    print(t[0])
