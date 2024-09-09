import heapq

n=int(input())

q=[]
for _ in range(n):
    s,e=map(int,input().split())
    heapq.heappush(q,(s,e))

seatNum=0
cnt=dict()
endQ=[]
empty=[]

while q:
    s,e=heapq.heappop(q)
    while endQ and endQ[0][0]<=s:
        heapq.heappush(empty,heapq.heappop(endQ)[1])
    if not empty:
        seatNum+=1
        if seatNum not in cnt:
            cnt[seatNum]=1
        else:
            cnt[seatNum]+=1
        heapq.heappush(endQ,(e,seatNum))
    else:
        k=heapq.heappop(empty)
        if k not in cnt:
            cnt[k]=1
        else:
            cnt[k]+=1
        heapq.heappush(endQ,(e,k))

print(len(cnt))
for key in cnt.keys():
    print(cnt[key],end=' ')