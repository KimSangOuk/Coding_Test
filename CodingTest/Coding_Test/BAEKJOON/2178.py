# 풀이시간 10분 시간제한 1초 메모리제한 192MB
# 1회차 정답
# 데이터의 크기가 가로 세로를 최대치로 해도 10,000 이기 때문에 O(NlogN)까지지만 bfs문제로 쉽게 풀 있는 탐색 형식이기 때문에 bfs를 선택했다. 최단거리를 구할 때는 맵에 표시하는 방법과 직접 큐에 기록하는 방법이 있는데 여기서는 간단히 맵에 기록했다.

from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(graph,start):
  q=deque([start])
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        q.append((nx,ny))

bfs(graph,(0,0))

# for i in range(n):
#   print(graph[i])

print(graph[n-1][m-1])  