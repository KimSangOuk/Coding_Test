# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 2차원 배열에서 최단경로를 구하는 다익스트라 알고리즘을 사용하면 되는 문제이다.

import heapq

INF=int(1e9)

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dijkstra(start):
  q=[]
  heapq.heappush(q,(graph[0][0],start))
  distance[start[0]][start[1]]=graph[0][0]
  while q:
    dist,now=heapq.heappop(q)
    if dist>distance[now[0]][now[1]]:
      continue
    for i in range(4):
      nx=now[0]+dx[i]
      ny=now[1]+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      cost=dist+graph[nx][ny]
      if cost<distance[nx][ny]:
        distance[nx][ny]=cost
        heapq.heappush(q,(cost,(nx,ny)))

tc=0
while True:
  tc+=1
  n=int(input())
  if n==0:
    break

  graph=[]
  for i in range(n):
    graph.append(list(map(int,input().split())))

  distance=[[INF]*n for _ in range(n)]

  start=(0,0)
  dijkstra(start)

  print("Problem "+str(tc)+": "+str(distance[n-1][n-1]))