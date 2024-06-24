import sys
sys.setrecursionlimit(10**5)

n,m=map(int,input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

board=[]
for _ in range(n):
  board.append(list(map(int,input().split())))

def dfs(board,y,x,visited):
  if y<0 or y>=n or x<0 or x>=m or visited[y][x] or board[y][x]==0:
    return False
  if board[y][x]>0:
    visited[y][x]=True
    dfs(board,y,x+1,visited)
    dfs(board,y,x-1,visited)
    dfs(board,y-1,x,visited)
    dfs(board,y+1,x,visited)
    return True
  return False

year=0
while True:
  year+=1
  melt=[[0]*m for _ in range(n)]
  visited=[[False]*m for _ in range(n)]
  # 녹는 칸의 갯수
  for i in range(n):
    for j in range(m):
      if board[i][j]>0:
        for k in range(4):
          nx=j+dx[k]
          ny=i+dy[k]
          if board[ny][nx]==0:
            melt[i][j]+=1
  # 녹는 칸의 갯수만큼 녹이기
  for i in range(n):
    for j in range(m):
      if board[i][j]>0:
        board[i][j]-=melt[i][j]
        if board[i][j]<0:
          board[i][j]=0
  # for i in range(n):
  #   print(board[i])
  # print()
  # 몇 덩어리인지 구하기
  count=0
  for i in range(n):
    for j in range(m):
      if board[i][j]>0 and not visited[i][j]:
        dfs(board,i,j,visited)
        count+=1
  if count==0:
    answer=0
    break
  elif count>1:
    answer=year
    break

print(answer)