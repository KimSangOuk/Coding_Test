# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순히 그래프를 그려서 한 지점에서 시작한 최단경로를 구한 뒤, 그 최단경로가 존재하는 지점들의 수와 그 중에서 가장 긴 시간대를 출력하면 되는 문제이다. 다익스트라 알고리즘으로 한 지점에서 다른 지점까지의 최단 거리를 구할 때 유용한데 ElogV이므로 각 100,000과 10,000이 들어가기 때문에 가능하다.

import heapq

INF=int(1e9)

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

for tc in range(int(input())):
  n,d,c=map(int,input().split())
  graph=[[] for _ in range(n+1)]
  distance=[INF]*(n+1)
  
  for _ in range(d):
    a,b,s=map(int,input().split())
    graph[b].append((a,s))
  
  dijkstra(c)
  count=0
  answer=[]
  for i in range(1,n+1):
    if distance[i]!=INF:
      count+=1
      answer.append(distance[i])
  print(count,max(answer))