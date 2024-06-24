# 풀이시간 9분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 1에서 N까지 중에 경로를 걸쳐서 갈 수 있는 최단 비용을 구하는 문제이기 때문에 데익스트라 알고리즘으로 접근 할 수 있다. 이 때, 시간복잡도도 ElogV로 가능하다. 양쪽 방향이 서로 연결될 수 있기 때문에, 길 연결 시에만 양방향 연결을 해주면 된다.

import heapq

INF=int(1e9)

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(1)
print(distance[n])