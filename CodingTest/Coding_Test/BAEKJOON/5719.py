import heapq
import copy
INF=1e9

def dijkstra_trace(start,end):
    q=[]
    heapq.heappush(q,(0,start))
    distance_trace[start]=[0,set()]
    delete_edges=set()
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance_trace[now][0]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<=distance_trace[i[0]][0]:
                if cost<distance_trace[i[0]][0]:
                    distance_trace[i[0]][1].clear()
                distance_trace[i[0]][1].update(distance_trace[now][1])
                distance_trace[i[0]][1].add((now,i[0]))
            if cost<distance_trace[i[0]][0]:
                distance_trace[i[0]][0]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance_trace[end][1]

def dijkstra(start,end):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]

while True:
    n,m=map(int,input().split())
    if not n and not m:
        break

    s,d=map(int,input().split())
    graph=[[] for _ in range(n)]
    distance_trace=dict()
    for i in range(n):
        distance_trace[i]=[INF,set()]
    distance=[INF]*n
    for _ in range(m):
        u,v,p=map(int,input().split())
        graph[u].append((v,p))

    delete_edges=dijkstra_trace(s,d)

    for i in range(n):
        for j in range(len(graph[i])-1,-1,-1):
                if (i,graph[i][j][0]) in delete_edges:
                    graph[i].pop(j)

    ans=dijkstra(s,d)
    if ans==INF:
        print(-1)
    else:
        print(ans)