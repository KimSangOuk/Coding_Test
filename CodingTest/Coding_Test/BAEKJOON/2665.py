# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 다익스트라 알고리즘으로 문을 지나가는 최소의 갯수를 구해서 그 값을 출력하면 되는 문제이다. 방의 수가 최대 2500개 이므로 충분히 가능하다.

import heapq

dx=[0,0,-1,1]
dy=[-1,1,0,0]

INF=int(1e9)

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

n=int(input())
graph=[]
distance=[[INF]*n for _ in range(n)]
for i in range(n):
  arr=list(input())
  real=[]
  for j in range(n):
    if arr[j]=='0':
      real.append(1)
    else:
      real.append(0)
  graph.append(real)

start=(0,0)
dijkstra(start)
print(distance[n-1][n-1])