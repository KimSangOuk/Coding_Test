import sys
from bisect import bisect_left

def LIS(arr,N):
    answer=[]
    for i in range(N):
        now=arr[i]
        index=bisect_left(answer,now)
        if index==len(answer):
            answer.append(now)
        else:
            answer[index]=now
    return(len(answer))

while True:
    try:
        N=int(input())
    except:
        break
    arr=list(map(int,input().split()))
    print(LIS(arr,N))