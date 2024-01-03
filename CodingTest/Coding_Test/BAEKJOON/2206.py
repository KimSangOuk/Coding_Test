# 풀이시간 3시간 경과
# 1회차 오답 - 풀이에 접근 못함, 실패
# ...

from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

board=[[] for _ in range(n)]
for i in range(n):
  arr=list(input())
  for j in range(m):
    board[i].append(int(arr[j]))

visited=[[0]*m for _ in range(n)]
wall_break=[[0]*m for _ in range(n)]

def bfs(board,start,visited):
  q=deque([])
  y,x=start
  q.append((y,x))
  visited[y][x]=1
  while q:
    y,x=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=m or ny<0 or ny>=n:
        continue
      if visited[ny][nx]>0:
        if wall_break[y][x]==0:
          wall_break[ny][nx]=0
        continue
      if board[ny][nx]==0:
        wall_break[ny][nx]=wall_break[y][x]
      else:
        if wall_break[y][x]==1:
          continue
        else:
          wall_break[ny][nx]=1
      q.append((ny,nx))
      visited[ny][nx]=visited[y][x]+1

start=(0,0)
bfs(board,start,visited)

for i in range(n):
  print(visited[i])

if visited[n-1][m-1]==0:
  print(-1)
else:
  print(visited[n-1][m-1])