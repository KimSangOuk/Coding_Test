# 이것이 취업을 위한 코딩테스트다 part03 '21. 인구 이동'과 동일

from collections import deque

n,l,r=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

dy=[0,0,-1,1]
dx=[-1,1,0,0]

def bfs(graph,start,visited):
  q=deque([start])
  unity=[]
  unity.append(start)
  visited[start[0]][start[1]]=True
  while q:
    y,x=q.popleft()
    for i in range(4):
      ny=y+dy[i]
      nx=x+dx[i]
      if ny>=0 and ny<n and nx>=0 and nx<n and abs(graph[ny][nx]-graph[y][x])>=l and abs(graph[ny][nx]-graph[y][x])<=r and (ny,nx) not in unity and visited[ny][nx]==False:
        q.append((ny,nx))
        unity.append((ny,nx))
        visited[ny][nx]=True
  return unity

def same(prev,graph):
  for i in range(n):
    for j in range(n):
      if prev[i][j]!=graph[i][j]:
        return False
  return True

count=0
prev=[[0]*n for _ in range(n)]
while True:
  for i in range(n):
    for j in range(n):
      prev[i][j]=graph[i][j]

  visited=[[False]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if visited[i][j]==False:
        unity=bfs(graph,(i,j),visited)
        # print(unity)
        sum_people=0
        box_people=0
        for y,x in unity:
          sum_people+=graph[y][x]
        box_people=int(sum_people/len(unity))
        for y,x in unity:
          graph[y][x]=box_people

  count+=1
  # print(count)

  if same(prev,graph):
    count-=1
    break


print(count)