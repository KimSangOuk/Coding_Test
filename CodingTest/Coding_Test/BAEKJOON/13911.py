import sys
import heapq
import copy

input=sys.stdin.readline
INF=int(9e9)

V,E=map(int,input().split())
graph=[[] for _ in range(V+1)]
for i in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(start,distance,graph):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

M,x=map(int,input().split())
mList=list(map(int,input().split()))
mDistance=[INF]*(V+1)
mGraph=copy.deepcopy(graph)
for k in mList:
    mGraph[0].append((k,0))
dijkstra(0,mDistance,mGraph)
S,y=map(int,input().split())
sList=list(map(int,input().split()))
sDistance=[INF]*(V+1)
sGraph=copy.deepcopy(graph)
for k in sList:
    sGraph[0].append((k,0))
dijkstra(0,sDistance,sGraph)

notHouseSpot=set(mList)|set(sList)
answer=INF
for i in range(1,V+1):
    if i not in notHouseSpot:
        if x>=mDistance[i] and y>=sDistance[i]:
            answer=min(answer,mDistance[i]+sDistance[i])
if answer==INF:
    print(-1)
else:
    print(answer)