# 풀이시간 10분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 모든 주어진 보드로 탐색하면서 각 1인 경우를 찾아 탐색하며 그림의 갯수를 찾고 그 그림마다 bfs 내부에서 q에 들어가는 수, 즉 각 그림의 크기의 최댓값을 구해가며 최댓값을 구하면 되는 문제이다.

from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

board=[]
for i in range(n):
  board.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]
max_value=0
count=0

def bfs(start):
  global max_value
  q=deque()
  q.append(start)
  visited[start[0]][start[1]]=True
  pic_width=0
  while q:
    x,y=q.popleft()
    pic_width+=1
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if board[nx][ny]==0 or visited[nx][ny]:
        continue
      q.append((nx,ny))
      visited[nx][ny]=True
  max_value=max(max_value,pic_width)

for i in range(n):
  for j in range(m):
    if board[i][j]==1 and not visited[i][j]:
      bfs((i,j))
      count+=1

print(count)
print(max_value)