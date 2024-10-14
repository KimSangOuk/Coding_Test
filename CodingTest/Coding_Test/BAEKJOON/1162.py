import sys
import heapq
input=sys.stdin.readline
INF=10**12

n,m,k=map(int,input().split())
distance=[[INF]*(n+1) for _ in range(k+1)]
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    for i in range(0,k+1):
        distance[i][start]=0
    q=[]
    heapq.heappush(q,(0,start,0))

    while q:
        dist,now,nowK=heapq.heappop(q)

        if dist>distance[nowK][now]:
            continue

        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[nowK][i[0]]:
                distance[nowK][i[0]]=cost
                heapq.heappush(q,(cost,i[0],nowK))
            if nowK<k:
                if dist<distance[nowK+1][i[0]]:
                    distance[nowK+1][i[0]]=dist
                    heapq.heappush(q,(dist,i[0],nowK+1))

dijkstra(1)
answer=INF
for i in range(0,k+1):
    answer=min(answer,distance[i][n])
print(answer)