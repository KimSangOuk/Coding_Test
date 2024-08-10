import heapq

def dijkstra_fox(start,distance):
    q=[]
    distance[start]=0
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

def dijkstra_wolf(start,distance):
    q=[]
    heapq.heappush(q,(0,start,0))
    while q:
        dist,now,state=heapq.heappop(q)
        if distance[state][now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]*(0.5 if state==0 else 2)
            if cost<distance[(state-1)%2][i[0]]:
                distance[(state-1)%2][i[0]]=cost
                heapq.heappush(q,(cost,i[0],(state-1)%2))

n,m=map(int,input().split())
INF=5e9
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

fox_distance=[INF]*(n+1)
wolf_distance=[[INF]*(n+1) for _ in range(2)]
dijkstra_fox(1,fox_distance)
dijkstra_wolf(1,wolf_distance)

ans=0
for i in range(2,n+1):
    if fox_distance[i]<min(wolf_distance[0][i],wolf_distance[1][i]):
        ans+=1
print(ans)