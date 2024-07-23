from collections import deque

n,k=map(int,input().split())
num=list(input())
lastL=len(num)
curL=0
answer=deque([])
for i in range(len(num)):
    if len(answer)==0:
        answer.append(num[i])
        lastL-=1
        curL+=1
        continue
    if lastL+curL<=n-k or int(answer[-1])>=int(num[i]):
        if curL<n-k:
            answer.append(num[i])
            curL+=1
            lastL-=1
    else:
        deleteCnt=0
        while len(answer)!=0 and lastL+curL>n-k and int(answer[-1])<int(num[i]):
            answer.pop()
            curL-=1
        answer.append(num[i])
        curL+=1
        lastL-=1

print("".join(answer))