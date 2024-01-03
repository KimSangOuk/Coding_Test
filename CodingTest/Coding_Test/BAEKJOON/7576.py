# 풀이시간 30분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 데이터의 총 양은 2차원 배열 이므로 1,000,000이라고 볼 수 있다. O(N)인 탐색을 수행하며 최대 시간이 얼마나 걸리는지 탐색할 수 있는데 이때, 특정칸에서의 시간을 묻는게 아닌 전체가 채워졌을 때, 걸리는 시간을 구하고 있으므로 진행하면서 +1씩 하며 가장 큰 값일 때만 저장해두고 있다가 출력하면 된다. 이 경우 BFS가 시간을 구하는데 있어 더 편리하다. 그리고 전부 익었는지 검사를 한 후 마치면 된다.

from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

m,n=map(int,input().split())

board=[]
q=deque([])
visited=[[-1]*m for _ in range(n)]
for i in range(n):
  arr=list(map(int,input().split()))
  for j in range(m):
    if arr[j]==1:
      q.append((i,j))
      visited[i][j]=0
  board.append(arr)

max_time=0

while q:
  y,x=q.popleft()
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or nx>=m or ny<0 or ny>=n or visited[ny][nx]!=-1 or board[ny][nx]!=0:
      continue
    visited[ny][nx]=visited[y][x]+1
    max_time=max(max_time,visited[ny][nx])
    q.append((ny,nx))

all=True
for i in range(n):
  for j in range(m):
    if board[i][j]==0 and visited[i][j]==-1:
      all=False
      break
  if not all:
    break

if all:
  print(max_time)
else:
  print(-1)