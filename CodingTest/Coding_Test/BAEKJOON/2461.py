import heapq

n,m=map(int,input().split())
classes=[]
for _ in range(n):
    arr=list(map(int,input().split()))
    heapq.heapify(arr)
    classes.append(arr)
answer=1e9
max_value=-1
q=[]
for i in range(n):
    k=heapq.heappop(classes[i])
    heapq.heappush(q,(k,i))
    max_value=max(k,max_value)
while True:
    now=heapq.heappop(q)
    if answer>abs(now[0]-max_value):
        answer=abs(now[0]-max_value)
    if not classes[now[1]]:
        break
    tmp=heapq.heappop(classes[now[1]])
    max_value=max(tmp,max_value)
    heapq.heappush(q,(tmp,now[1]))
print(answer)