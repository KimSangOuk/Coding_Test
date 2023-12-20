# 풀이시간 1시간30분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 먼저 문제의 전체적인 그림은 섬을 잇는 다리와 가중치를 구해서 섬을 전부 연결하는 최소값을 구하고 연결하지 못하는 경우 -1을 출력하는 최소 신장 트리가 전체 적인 문제의 틀이다.
# 먼저 메인 쪽을 보면 dfs로 섬의 각 좌표들을 구하고 섬의 번호를 구할 수 있다.
# 그런 다음 섬을 서로 잇는 길이를 구해야 하는데, 이 때, x좌표가 같을 때, 중간에 현재 두 좌표를 제외한 섬이 없는 y좌표의 최소 거리와 반대로 y좌표가 같을 때, 중간에 현재 두 좌표를 제외한 섬이 없는 x좌표의 최소 거리를 구하면 된다.
# 그렇게 각 섬마다 이어지는 길과 가중치를 간선으로 저장한 다음 정렬하여 최소 간선 트리를 구해서 비용을 출력하면 되는데, 이 때, 서로소 집합의 find 알고리즘으로 모든 섬이 이어져 있는지 확인해서 이어져 있으면 출력하고 ,이어져 있지 않으면 -1을 출력하면 된다.

import sys
from collections import deque

input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

INF=int(1e9)

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

def bfs(start):
  q=deque([start])
  start_x,start_y=start
  visited[start_x][start_y]=True
  island_xy=[start]
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if not visited[nx][ny] and graph[nx][ny]==1:
        visited[nx][ny]=True
        q.append((nx,ny))
        island_xy.append((nx,ny))
  island.append(island_xy)

def mid_island(island,ax,ay,bx,by):
  for i in range(1,len(island)):
    for x,y in island[i]:
      if x==ax and (ay<y<by or by<y<ay):
        return False
      elif y==ay and (ax<x<bx or bx<x<ax):
        return False
  return True

def take_island_dist(island,a,b):
  a=island[a]
  b=island[b]
  dist=INF
  for a_x,a_y in a:
    for b_x,b_y in b:
      a_b=0
      if a_x==b_x:
        a_b=abs(a_y-b_y)-1
      elif a_y==b_y:
        a_b=abs(a_x-b_x)-1
      if mid_island(island,a_x,a_y,b_x,b_y) and a_b>1:
        dist=min(dist,a_b)
        # print(dist,a_x,a_y,b_x,b_y)
  return dist
        
n,m=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]

island=[0]
island_count=0

for i in range(n):
  for j in range(m):
    if graph[i][j]==1 and not visited[i][j]:
      bfs((i,j))
      island_count+=1

# print(island)

parent=[0]*(island_count+1)

for i in range(1,island_count+1):
  parent[i]=i

edges=[]

for i in range(1,island_count+1):
  for j in range(i+1,island_count+1):
    cost=take_island_dist(island,i,j)
    if cost!=INF:
      edges.append((cost,i,j))
      # print(i,j,cost)

edges.sort()

# print(edges)

result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

possible=True
for i in range(1,island_count):
  if find_parent(parent,i)!=find_parent(parent,i+1):
    possible=False
    break

if possible==False:
  print(-1)
else:
  print(result)  