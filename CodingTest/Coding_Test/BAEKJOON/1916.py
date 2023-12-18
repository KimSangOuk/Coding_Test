# 풀이시간 5분 시간제한 0.5초 메모리제한 128MB
# 1회차 정답
# 단순히 최단 경로를 구하는 문제이다. V의 값이 크기 때문에 플로이드 워셜이 불가능 하다. 최단거리 중 도착지의 최단거리를 출력하면 된다.

import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  u,v,w=map(int,input().split())
  graph[u].append((v,w))

start,target=map(int,input().split())

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

print(distance[target])