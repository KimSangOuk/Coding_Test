# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 데이터의 최대크기가 10,000이고 각 지점을 연결하는 간선수가 대략 한 칸에 4개씩 해서 40,000개라고 할때, 다익스트라 알고리즘으로 ElogV이기 때문에 가능하다. 이 때, 각 벽의 최소 수를 구하는 것이기 때문에 진행하면서 벽이 각 칸까지의 거리라고 생각하고 더해가면 된다. 이 때, 끝 점까지 소모되는 벽의 수를 구하면 되는 것이다.

import heapq

m,n=map(int,input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

INF=int(1e9)
graph=[]
for i in range(n):
  graph.append(list(input()))

distance=[[INF]*m for _ in range(n)]

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start[0]][start[1]]=0
  while q:
    dist,now=heapq.heappop(q)
    if dist>distance[now[0]][now[1]]:
      continue
    for i in range(4):
      nx=now[0]+dx[i]
      ny=now[1]+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      cost=dist+int(graph[nx][ny])
      if cost<distance[nx][ny]:
        distance[nx][ny]=cost
        heapq.heappush(q,(cost,(nx,ny)))

dijkstra((0,0))
print(distance[n-1][m-1])