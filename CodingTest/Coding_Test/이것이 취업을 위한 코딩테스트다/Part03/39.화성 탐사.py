# 풀이시간 25분/40분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 2차원 배열은 그래프의 형태와 구조적으로 같기 때문에 그래프라고 생각하고 문제에 접근할 수 있다. 다만 N이 최대 125이기 때문에 2차원 배열이라는 점에서 V의 갯수가 상당히 5^6가 될 수 있기에 플로이드 워셜은 불가능 하고 ElogV인 다익스트라로 접근하는게 시간복잡도 면에서는 맞다고 생각이 된다.
# 또한 한 지점에서 한 지점까지의 최단 거리를 구하는 문제이기 때문에 다익스트라 알고리즘을 사용하는 것이 좋다.
# 알고리즘 면에서는 큐에 넣을 좌표를 구할 때, 4가지 방향을 검사하는 식으로 접근하면 된다.

import sys
import heapq

input=sys.stdin.readline
INF=int(1e9) # 무한을 의미하는 값으로 10억을 설정

dx=[0,-1,0,1]
dy=[-1,0,1,0]

# 다익스트라 알고리즘 수행
def dijkstra(start):
  q=[]
  # 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여 큐에 삽입
  heapq.heappush(q,(graph[0][0],start))
  distance[0][0]=graph[0][0]
  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
    dist,now=heapq.heappop(q)
    now_x,now_y=now
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if dist>distance[now_x][now_y]:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in range(4):
      nx=now_x+dx[i]
      ny=now_y+dy[i]
      # 맵의 범위를 벗어나는 경우 무시
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      cost=dist+graph[nx][ny]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost<distance[nx][ny]:
        distance[nx][ny]=cost
        heapq.heappush(q,(cost,(nx,ny)))

# 전체 테스트 케이스(Test Case)만큼 반복
for _ in range(int(input())):
  # 노드의 개수를 입력받기
  n= int(input())
  # 전체 맵 정보를 입력받기
  graph=[]
  # 최단 거리 테이블을 모두 무한으로 초기화
  distance=[[INF]*n for _ in range(n)]
  for _ in range(n):
    graph.append(list(map(int,input().split())))

  # 시작 위치는 (0,0)
  dijkstra((0,0))

  print(distance[n-1][n-1])