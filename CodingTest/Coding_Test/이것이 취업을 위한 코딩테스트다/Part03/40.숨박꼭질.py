# 풀이시간 15분/40분 시간제한 1초 메모리제한 128MB
# 1회차 정답
#

import sys
import heapq

INF=int(1e9) # 무한을 의미하는 값으로 10억 설정
input=sys.stdin.readline

# 노드의 개수, 간선의 개수를 입력받기
n,m=map(int,input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a,b=map(int,input().split())
  # a번 노드와 b번 노드의 이동 비용이 1이라는 의미(양방향)
  graph[a].append((b,1))
  graph[b].append((a,1))

def dijkstra(start):
  q=[]
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q: # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
    dist,now=heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if dist>distance[now]:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost=dist+i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

# 시작 노드를 1번 헛간으로 설정
start=1
# 다익스트라 알고리즘 수행
dijkstra(start)
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_value=0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
answer=[]
for i in range(1,n+1):
  if distance[i]!=INF and distance[i]>max_value:
    max_value=distance[i]

for i in range(1,n+1):
  if distance[i]==max_value:
    answer.append(i)

print(min(answer),max_value,len(answer))