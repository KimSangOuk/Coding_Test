# 풀이시간 15분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 좌표를 탐색해서 그 탐색 할 때마 카운트해서 그 크기를 구하면 되는 문제이다. DFS를 연습 중이기 때문에 DFS에 탐색하는 순간 count를 global로 선언해서 크기를 구하면서 최댓값을 구했다.

import sys
sys.setrecursionlimit(10**5)

n,m,k=map(int,input().split())

answer=0
board=[[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]
for _ in range(k):
  a,b=map(int,input().split())
  board[a-1][b-1]=1

def dfs(start):
  global count
  if start[0]<0 or start[0]>=n or start[1]<0 or start[1]>=m:
    return
  if board[start[0]][start[1]]==1 and not visited[start[0]][start[1]]:
    visited[start[0]][start[1]]=True
    count+=1
    dfs((start[0]+1,start[1]))
    dfs((start[0]-1,start[1]))
    dfs((start[0],start[1]+1))
    dfs((start[0],start[1]-1))

for i in range(n):
  for j in range(m):
    if board[i][j]==1 and not visited[i][j]:
      count=0
      dfs((i,j))
      answer=max(answer,count)

print(answer)