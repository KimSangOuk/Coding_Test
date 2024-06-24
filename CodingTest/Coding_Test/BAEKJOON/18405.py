# 이것이 취업을 위한 코딩테스트다 part03 '17. 경쟁적 전염'과 동일
from collections import deque
import sys

n,k=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

queue=deque()
new_arr=[]

for i in range(n):
  for j in range(n):
    if graph[i][j]!=0:
      new_arr.append((graph[i][j],i,j))

new_arr.sort()
queue.append(new_arr)

s,x_a,y_a=map(int,sys.stdin.readline().split())

dx=[0,-1,0,1]
dy=[-1,0,1,0]

for ms in range(s):
  arr=queue.popleft()
  new_arr=[]
  for d,x,y in arr:
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:
        graph[nx][ny]=d
        new_arr.append((d,nx,ny))
  new_arr.sort()
  queue.append(new_arr)

print(graph[x_a-1][y_a-1])