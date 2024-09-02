import sys
from collections import deque

input=sys.stdin.readline

n,d,k,c=map(int,input().split())
dishes=[]
for _ in range(n):
    dishes.append(int(input()))

dishes=dishes*2
now=deque(dishes[:k])
nowSet=set(now)
typeDict=dict()
for i in dishes[:k]:
    if i in typeDict:
        typeDict[i]+=1
    else:
        typeDict[i]=1

answer=0
end=k-1
start=0
while True:
    num=len(nowSet)
    if c not in nowSet:
        num+=1
    answer=max(answer,num)
    end+=1
    start+=1
    if end>=len(dishes):
        break
    if dishes[end] in nowSet:
        typeDict[dishes[end]]+=1
    else:
        nowSet.add(dishes[end])
        typeDict[dishes[end]]=1
    if typeDict[dishes[start-1]]-1==0:
        nowSet.remove(dishes[start-1])
        del typeDict[dishes[start-1]]
    else:
        typeDict[dishes[start-1]]-=1

print(answer)