# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 문제를 보면 그래프를 그려서 최단경로를 푸는 문제이다. 조건을 살펴봤을 때, V가 1,000이고 E가 10,000이기 때문에 파티 장소에서 돌아올 때는 문제가 되지 않지만, 파티장소까지 갈 때는, 총 10,000번을 실행해야 하므로 문제가 될 수도 있다. 하지만 무조건 돌아올 수 있고 한 장소까지 한번의 경로만 있다는 점을 본다면, E의 수가 반이 되어 계산되는 것을 알 수 있다. 그렇기에 시간제한에 통과할 수 있다.

import sys
import heapq

input=sys.stdin.readline

INF=int(1e9)

n,m,x=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

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

answer=[0]*(n+1)

for i in range(1,n+1):
  distance=[INF]*(n+1)
  dijkstra(i)
  answer[i]=distance[x]

distance=[INF]*(n+1)
dijkstra(x)
for i in range(1,n+1):
  answer[i]+=distance[i]

print(max(answer[1:]))