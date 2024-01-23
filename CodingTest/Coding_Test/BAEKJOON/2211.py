# 풀이시간 37분 시간제한 2초 메모리제한 192MB
# 1회차 정답
# 정점과 간선으로 이루어진 그래프에서 시작점이 1로하는 최단거리만을 유지하는 간선을 구하는 문제이다. 최단거리 문제로 생각하고 접근할 수 있는데, 이 때, 각 노선의 갯수와 그 노선을 구해야 하므로 최단 거리를 체크하며 간선을 체크하는 다익스트라 알고리즘을 생각해 볼 수 있다. 다익스트라 알고리즘으로 풀 경우, ElogV로 약 1000만이 나오기 때문에 한번 정도만 가능하다는 것을 알 수 있다. 그렇기 때문에 다익스트라 알고리즘 내부에서의 연산이 필요하거나 외부에서 소소한 연산이 추가적으로 이루어질 수 있다고 판단할 수 있고 내부에서의 간선이 힙에 간선이 추가될 때마다, 최단거리가 갱신되기 때문에 그 간선이 최단거리를 나타내는 간선이라는 것을 알 수 있다. 추가적으로 기존에 있던 간선에 대해 갱신이 될 때의 전의 간선에 대한 처리가 필요한데 한 정점에 관해서 모두 이어질 때, 그 정점으로 들어오는 간선은 최단 거리를 유지하는 간선 하나 뿐 이므로 각 정점을 기준으로 간선이 갱신 될 때, 그 간선또한 따로 저장해두면 된다. 그렇게 된다면 간선의 총 갯수는 정점-1개이고 저장된 간선을 출력하면 된다.

import heapq

INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
answer=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

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

        answer[i[0]]={now,i[0]}
          
dijkstra(1)
print(n-1)
for i in range(1,len(answer)):
  if len(answer[i])!=0:
    print(*answer[i])