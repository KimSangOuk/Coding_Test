# 풀이시간 13분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 시작점이 0에서 시작해서 고속도로인 길이인 d가 도착점으로 하는 최단 경로를 찾는 문제이다. 각 길에서는 한칸씩 갈 수 있는 길이 있다고 하고 추가적으로 주어진 지름길이 존재한다. 그렇다고 했을 때, 최단경로를 구하면 된다. 특정 위치에서 특정 위치까지의 최단 경로를 구하는 문제이므로 다익스트라 알고리즘으로 푸는 것이 좋고 시간복잡도도 ElogV로 가능하다. 

import heapq

n,d=map(int,input().split())

INF=int(1e9)
distance=[INF]*(10001)

graph=[[] for i in range(10001)]
for _ in range(n):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

for i in range(0,10000):
  graph[i].append((i+1,1))

def dijkstra(start):
  q=[]
  distance[start]=0
  q.append((0,start))
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(0)
print(distance[d])
  