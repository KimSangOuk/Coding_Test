# 풀이시간 25분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 그래프를 그릴 수 있는 입력값들을 제시해주어서 그래프 문제임을 알 수 있다. 우리는 최단 경로를 구하고 그 경로가 지나간 갯수와 그 경로를 나타내어야 하는데, 일단 특정지점에서 특정 지점까지의 최단 경로를 구해야 하고 E의 개수가 100,000개 V의 개수가 1,000개 이므로 ElogV가 가능해 보이므로 다익스트라 알고리즘을 고려한다.
# 이 때 경로를 구해야 되는데, 우리는 한 지점을 한번씩만 처리하기 때문에 큐에들어가는 순간에 우리는 그 전 도시에 대해서 알 수 있다. 그렇기 때문에 각 지점의 전 지점을 기록해 두었다가 역으로 우리의 목적지 부터 역추적하면 우리가 원하는 경로가 나올 수 있다.

import heapq
from collections import deque

INF=int(1e9)

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  shortest_path[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if dist>distance[now]:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))
        shortest_path[i[0]]=now
        

n=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

m=int(input())
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

start,target=map(int,input().split())
shortest_path=[0]*(n+1)
dijkstra(start)
print(distance[target])
answer=[]
answer.append(target)
while True:
  target=shortest_path[target]
  if target==0:
    break
  answer.append(target)
answer.reverse()
print(len(answer))
for i in answer:
  print(i,end=' ')