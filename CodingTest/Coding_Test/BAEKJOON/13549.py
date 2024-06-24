# 풀이시간 30분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 문제만 보았을 때, 수빈이의 위치로 부터 동생의 위치로 가는 그래프를 그려 최단 거리를 구하는 문제이다. 수빈이가 갈 수 있는 E는 매 순간 3개씩 있으며 걸리는 시간이 거리가 될 수 있다. 이러한 조건들이 성립하는 최단 경로를 구하는 문제이다. V는 최대 100,000이기 때문에 각 순간에 갈 수 있는 루트는 3개씩 해서 300,000이 최대로 나올 수 있다. 그렇기에 ElogV를 해도 문제 없이 풀어낼 수 있는 다익스트라 알고리즘을 사용하면 된다.
# 세개의 루트에 대한 계산을 할 때, 범위를 벗어나지 않도록 확인해주는 과정이 필요했다.

import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,k=map(int,input().split())

distance=[INF]*100001

q=[]
heapq.heappush(q,(0,n))
distance[n]=0
while q:
  dist,now=heapq.heappop(q)
  if dist>distance[now]:
    continue
  
  cost=dist
  if now*2<=100000 and cost<distance[now*2]:
    distance[now*2]=cost
    heapq.heappush(q,(cost,now*2))
  cost=dist+1
  if now+1<=100000 and cost<distance[now+1]:
    distance[now+1]=cost
    heapq.heappush(q,(cost,now+1))
    # print(dist,now+1)
  if now-1>=0 and cost<distance[now-1]:
    distance[now-1]=cost
    heapq.heappush(q,(cost,now-1))
    # print(dist,now-1)

print(distance[k])