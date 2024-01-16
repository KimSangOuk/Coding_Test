# 풀이시간 40분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 모든 모양을 전체 맵에서 탐색하면서 그 합 중 최대값을 도출해내는 문제이다. 처음에 'ㅗ'을 보지 못하고 있다가 dfs로 먼저 풀고 나중에 'ㅗ'을 추가하였다. 모양별로 전체 탐색을 해도 전체 연산이 5백만회 정도 되기 때문에 충분히 가능하다.

n,m=map(int,input().split())

board=[]
for _ in range(n):
  board.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,deep,now):
  global answer
  if x<0 or x>=n or y<0 or y>=m or visited[x][y]:
    return False
  if deep==4:
    now+=board[x][y]
    answer=max(answer,now)
    # print("도착")
  else:
    visited[x][y]=True
    dfs(x+1,y,deep+1,now+board[x][y])
    dfs(x-1,y,deep+1,now+board[x][y])
    dfs(x,y+1,deep+1,now+board[x][y])
    dfs(x,y-1,deep+1,now+board[x][y])
    visited[x][y]=False
  return True

shape=[[(0,0),(1,0),(2,0),(1,1)],[(0,0),(1,0),(2,0),(1,-1)],[(0,0),(0,1),(0,2),(1,1)],[(0,0),(0,1),(0,2),(-1,1)]]

def check_this(x,y):
  global answer
  for i in range(4):
    value=0
    for j in range(4):
      sx,sy=shape[i][j]
      nx=sx+x
      ny=sy+y
      if nx<0 or nx>=n or ny<0 or ny>=m:
        break
      value+=board[nx][ny]
    answer=max(answer,value)

answer=0
for i in range(n):
  for j in range(m):
    dfs(i,j,1,0)
    check_this(i,j)

print(answer)