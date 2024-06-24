# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 구역별로 탐색해서 구역의 갯수를 구하는 탐색문제이다. DFS/BFS로 풀 수 있다.
# 이 때 시간복잡도로 풀 수 있는지를 확인해보면 데이터의 수가 최대 10,000개에 두번 진행하므로 *2 밖에 되지 않는다.

import sys

sys.setrecursionlimit(10**4)

n=int(input())
board=[]
for _ in range(n):
  board.append(list(map(str,input())))

visited=[[0]*n for _ in range(n)]
visited_rg=[[0]*n for _ in range(n)]

def dfs(y,x,color):
  if y<0 or y>=n or x<0 or x>=n:
    return
  if board[y][x]==color and visited[y][x]==0:
    visited[y][x]=1
    dfs(y-1,x,color)
    dfs(y+1,x,color)
    dfs(y,x-1,color)
    dfs(y,x+1,color)
    return True
  return False

def dfs_rg(y,x,color1,color2):
  if y<0 or y>=n or x<0 or x>=n:
    return
  if (board[y][x]==color1 or board[y][x]==color2) and visited_rg[y][x]==0:
    visited_rg[y][x]=1
    dfs_rg(y-1,x,color1,color2)
    dfs_rg(y+1,x,color1,color2)
    dfs_rg(y,x-1,color1,color2)
    dfs_rg(y,x+1,color1,color2)
    return True
  return False

count=0
count_rg=0
for i in range(n):
  for j in range(n):
    if visited[i][j]==0:
      dfs(i,j,board[i][j])
      count+=1
    if visited_rg[i][j]==0:
      if board[i][j]=='B':
        dfs_rg(i,j,'B','B')
      else:
        dfs_rg(i,j,'R','G')
      count_rg+=1

print(count,count_rg)