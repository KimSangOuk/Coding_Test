# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 보드를 그려낸 다음 그 보드에서 칠이 안된 칸을 완전 탐색형태로 전부 확인하며, dfs나 bfs형태로 칸의 갯수를 구하는 문제이다. 이번 문제의 경우, dfs를 연습할 때 풀었기 때문에 dfs로 풀었지만 상관없다. 또한 시간복잡도도 최대 보드의 크기가 10,000이기 때문에 O(N)으로 가능하다.

import sys
sys.setrecursionlimit(10 ** 4)

m,n,k=map(int,input().split())

board=[[0]*n for _ in range(m)]

for _ in range(k):
  s_x,s_y,e_x,e_y=map(int,input().split())

  for i in range(s_y,e_y):
    for j in range(s_x,e_x):
      board[i][j]=1

def dfs(y,x):
  global count
  if y<0 or y>=m or x<0 or x>=n or board[y][x]==1:
    return False
  if board[y][x]==0:
    board[y][x]=2
    count+=1
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x-1)
    dfs(y,x+1)
    return True
  return False
  

answer=[]
for i in range(m):
  for j in range(n):
    if board[i][j]==0:
      count=0
      dfs(i,j)
      answer.append(count)

answer.sort()
print(len(answer))
for a in answer:
  print(a,end=' ')