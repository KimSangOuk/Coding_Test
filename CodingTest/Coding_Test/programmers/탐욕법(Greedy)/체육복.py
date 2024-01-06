def solution(n, lost, reserve):
answer = 0

count=[0]*(n+1)
for i in range(1,n+1):
    if i in reserve:
        count[i]=2
        if i in lost:
            count[i]=1
    elif i not in lost:
        count[i]=1
for i in range(1,n+1):
    if count[i]==2:
        left=i-1
        right=i+1
        if left>0 and count[left]==0:
            count[left]+=1
        elif right<=n and count[right]==0:
            count[right]+=1
for i in range(1,n+1):
    if count[i]>0:
        answer+=1
return answer