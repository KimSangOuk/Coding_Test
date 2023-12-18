# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 최단 경로를 구하는 문제이다. V의 값이 크기 때문에 플로이드 워셜이 아닌 다익스트라 알고리즘으로 풀어내면 된다.

import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

start=int(input())

for _ in range(m):
  u,v,w=map(int,input().split())
  graph[u].append((v,w))

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

dijkstra(start)

for d in distance[1:]:
  if d==INF:
    print("INF")
  else:
    print(d)