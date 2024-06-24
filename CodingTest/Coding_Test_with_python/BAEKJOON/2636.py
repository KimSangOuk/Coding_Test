# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 바깥에 접해있는 공기를 탐색으로 구해서 구멍과는 분리되게 구한 다음 그 공기와 닿아있는 치즈만 제거해 나가면서 답을 구하면 되는 문제이다. 그래프 DFS/BFS 탐색과 시뮬레이션을 합쳐놓았다고 할 수 있다.

from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
board=[]

cheeze=[]
for i in range(n):
  arr=list(map(int,input().split()))
  for j in range(m):
    if arr[j]==1:
      cheeze.append((i,j))
  board.append(arr)

def get_out_bfs(start):
  q=deque([])
  q.append(start)
  arr=[]
  visited=[[False]*m for _ in range(n)]
  visited[start[0]][start[1]]=True
  arr.append(start)
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if board[nx][ny]==1 or visited[nx][ny]:
        continue
      q.append((nx,ny))
      arr.append((nx,ny))
      visited[nx][ny]=True
  return arr

time=0
count=0
prev=len(cheeze)
while True:
  time+=1
  # 바깥 공기 집합 구하기
  out=set(get_out_bfs((0,0)))

  # 바깥 공기에 닿아있는 치즈 제거
  touch_out_cheeze=[]
  for c in range(len(cheeze)):
    x,y=cheeze[c]
    if (x+1,y) in out or (x-1,y) in out or (x,y+1) in out or (x,y-1) in out:
      board[x][y]=0
      touch_out_cheeze.append(c)
  touch_out_cheeze.sort(reverse=True)
  for i in touch_out_cheeze:
    cheeze.pop(i)

  # 남아 있는 치즈 덩어리 갯수 구하기
  count=len(cheeze)
  if count==0:
    break
  prev=count

print(time)
print(prev)