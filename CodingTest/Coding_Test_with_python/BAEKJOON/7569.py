# 풀이시간 40분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 '7576번 토마토'문제에서 3차원 배열로 높이까지 추가한 문제이다.

from collections import deque

dx=[0,0,-1,1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]

m,n,h=map(int,input().split())

board=[]
q=deque([])
visited=[[[-1]*m for _ in range(n)] for _ in range(h)]
for k in range(h):
  tmp=[]
  for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(m):
      if arr[j]==1:
        q.append((k,i,j))
        visited[k][i][j]=0
    tmp.append(arr)
  board.append(tmp)

max_time=0

while q:
  z,y,x=q.popleft()
  for i in range(6):
    nz=z+dz[i]
    nx=x+dx[i]
    ny=y+dy[i]
    if nz<0 or nz>=h or nx<0 or nx>=m or ny<0 or ny>=n or visited[nz][ny][nx]!=-1 or board[nz][ny][nx]!=0:
      continue
    visited[nz][ny][nx]=visited[z][y][x]+1
    max_time=max(max_time,visited[nz][ny][nx])
    q.append((nz,ny,nx))

all=True
for k in range(h):
  for i in range(n):
    for j in range(m):
      if board[k][i][j]==0 and visited[k][i][j]==-1:
        all=False
        break
    if not all:
      break

if all:
  print(max_time)
else:
  print(-1)