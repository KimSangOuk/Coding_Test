import heapq

n=int(input())
meetings=[]
for _ in range(n):
    heapq.heappush(meetings,tuple(map(int,input().split())))

ended=[]
cnt=0
answer=0
while meetings:
    now=heapq.heappop(meetings)
    while ended and ended[0]<=now[0]:
        heapq.heappop(ended)
        cnt-=1
    heapq.heappush(ended,now[1])
    cnt+=1
    answer=max(answer,cnt)
print(answer)