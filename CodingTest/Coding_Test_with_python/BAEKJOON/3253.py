# 풀이시간 25분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 처음에 가리키고 있는 방향은 스위치가 바뀔 필요가 없기 때문에 0으로 계산이 되고 다른 노드들은 1이라고 했을 때, 최단 경로를 구하면 되는 문제이다.

import heapq

n,a,b=map(int,input().split())

INF=int(1e9)

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for i in range(1,n+1):
  array=list(map(int,input().split()))
  if array[0]!=0:
    graph[i].append((array[1],0))
  for j in range(2,len(array)):
    graph[i].append((array[j],1))

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

dijkstra(a)
if distance[b]==INF:
  print(-1)
else:
  print(distance[b])