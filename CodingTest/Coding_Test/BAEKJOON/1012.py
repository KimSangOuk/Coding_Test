# 풀이시간 20분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 모든 칸을 브루트 포스 알고리즘으로 훑은 다음, DFS나 BFS로 찾은 칸을 체크하며 그 수를 세면 되는 문제.
# 최대 칸의 수가 2,500이기 때문에 시간복잡도가 O(N^2) 정도 되는 문제

from collections import deque

t=int(input())

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(graph,start,visited):
  visited[start[0]][start[1]]=True
  q=deque([start])
  while q:
    y,x=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<m and ny>=0 and ny<n and visited[ny][nx]==False and graph[ny][nx]==1:
        visited[ny][nx]=True
        q.append((ny,nx))

for _ in range(t):
  
  m,n,k=map(int,input().split())
  graph=[[0]*m for _ in range(n)]
  for _ in range(k):
    x,y=map(int,input().split())
    graph[y][x]=1
  visited=[[False]*m for _ in range(n)]

  count=0
  for i in range(n):
    for j in range(m):
      if graph[i][j]==1 and visited[i][j]==False:
        bfs(graph,(i,j),visited)
        count+=1
  
  print(count)

