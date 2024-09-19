N,L,R,X=map(int,input().split())
arr=list(map(int,input().split()))

answer=0

for i in range(2<<(N-1)):
    maxValue=0
    minValue=1e9
    sumValue=0
    for j in range(N):
        if i&(1<<j):
            sumValue+=arr[j]
            maxValue=max(maxValue,arr[j])
            minValue=min(minValue,arr[j])
    if L<=sumValue<=R and maxValue-minValue>=X:
        answer+=1

print(answer)