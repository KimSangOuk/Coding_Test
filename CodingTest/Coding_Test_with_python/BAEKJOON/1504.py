# 풀이시간 25분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 한 지점에서 출발해서 특정 지점을 경유하여 목적지까지 가는 최단 경로를 구하는 문제이다. N의 크기가 크기 때문에 플로이드 워셜 알고리즘은 불가능 하고 다익스트라 알고리즘을 고려해볼 수 있는데, 이 때, 1에서 출발할 경우, 도착지점까지의 경우, 경유 지점 사이의 거리를 각각 구해야하기 때문에 3번 실행해야 한다는 것을 알 수 있다. ElogN일때 *3을 해도 시간제한 안에 들어오기 때문에 가능하다고 볼 수 있다.

import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start):
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

answer=0
start=1
distance=[INF]*(n+1)
dijkstra(start)
path1,path2=distance[v1],distance[v2]
distance=[INF]*(n+1)
dijkstra(v1)
path1+=distance[v2]
path2+=distance[v2]
distance=[INF]*(n+1)
dijkstra(n)
path1+=distance[v2]
path2+=distance[v1]
answer=min(path1,path2)

if answer>=INF:
  print(-1)
else:
  print(answer)