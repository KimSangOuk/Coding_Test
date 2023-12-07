# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답 - 풀이시간 너무 오래 걸림
# 20분 정도로 풀 수 있는 문제였는데 메모리 초과가 걸렸다. 단순 DFS로 풀 수 있는 문제길래 dfs를 사용해서 풀고 시간복잡도도 데이터의 크기가 10,000인 배열에 높이도 최대가 100이라 문제가 없었다. 하지만 문제는 처음 써보는 setrecursionlimit함수에 있었다. 이 녀석이 메모리 초과를 일으켰다.

import sys

sys.setrecursionlimit(10**4)

n=int(input())
graph=[]
max_height=1
for _ in range(n):
  arr=list(map(int,input().split()))
  max_height=max(max_height,max(arr))
  graph.append(arr)

def dfs(y,x):
  if y<0 or y>=n or x<0 or x>=n:
    return False
  if visited[y][x]==False and graph[y][x]>water:
    visited[y][x]=True
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x-1)
    dfs(y,x+1)
    return True
  return False

answer=0

for water in range(0,max_height):
  visited=[[False]*n for _ in range(n)]
  
  count=0
  for i in range(n):
    for j in range(n):
      if visited[i][j]==False and graph[i][j]>water:
        dfs(i,j)
        count+=1

  answer=max(count,answer)

print(answer)