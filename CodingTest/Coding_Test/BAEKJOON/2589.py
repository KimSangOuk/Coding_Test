from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

board=[]
for i in range(n):
  board.append(list(input()))

answer=0

def bfs(start):
  global answer
  q=deque()
  q.append(start)
  visited=[[-1]*m for _ in range(n)]
  visited[start[0]][start[1]]=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if board[nx][ny]=='W' or visited[nx][ny]>=0:
        continue
      visited[nx][ny]=visited[x][y]+1
      q.append((nx,ny))
  max_value=-1
  for i in range(n):
    for j in range(m):
      max_value=max(max_value,visited[i][j])
  answer=max(max_value,answer)

for i in range(n):
  for j in range(m):
    if board[i][j]=='L':
      bfs((i,j))

print(answer)