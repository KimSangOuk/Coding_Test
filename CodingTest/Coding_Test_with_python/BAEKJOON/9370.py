# 풀이시간 30분 시간제한 3초 메모리제한 256MB
# 1회차 정답
# 시작점을 주어주고 각 지점까지의 최단 거리가 필요하고 특정 루트를 경유해서 목적지에 가는 최단 거리가 필요하기 때문에, 최단거리 알고리즘을 고려해볼 수 있다. 시간복잡도로 보았을 때, ElogV의 연산이 데이터량을 넣어보았을 때 약 60만이 나오기 때문에 다익스트라 알고리즘이 가능하다고 볼 수 있다. 이때, 몇번의 연산을 수행해야하는지를 따져보아야하는데, 처음 시작 지점에서의 목적지 후보까지의 거리와 경유지인 g,h부터의 목적지 후보까지의 거리 총 3개의 연산이 필요하기 때문에 각 연산을 한 다음 시작-g-h-후보, 시작-h-g-후보 까지의 거리를 각 더해서 실제 최단 거리와 같은지를 비교해서 답을 구해주면 된다.

import heapq

INF=int(1e9)

def dijkstra(distance,start):
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
  

for tc in range(int(input())):
  n,m,t=map(int,input().split())
  s,g,h=map(int,input().split())
  dist_g_h=0
  graph=[[] for _ in range(n+1)]
  for _ in range(m):
    a,b,d=map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))
    if (a==g and b==h) or (a==h and b==g):
      dist_g_h=d
  target=[]
  for _ in range(t):
    target.append(int(input()))

  distance_from_start=[INF]*(n+1)
  distance_from_g=[INF]*(n+1)
  distance_from_h=[INF]*(n+1)

  dijkstra(distance_from_start,s)
  dijkstra(distance_from_g,g)
  dijkstra(distance_from_h,h)

  answer=[]
  for k in target:
    if distance_from_start[k]==(distance_from_start[g]+dist_g_h+distance_from_h[k]) or distance_from_start[k]==(distance_from_start[h]+dist_g_h+distance_from_g[k]):
      answer.append(k)
  answer.sort()
  for a in answer:
    print(a,end=' ')
  print()
  