# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 문제에서 연결된 모양에서의 1을 탐색하는 형태를 원하고 있고 또한 그 갯수를 파악하라고 하였으니 bfs/dfs 탐색을 사용하였다. 그러기 위해서는 모든 칸을 확인해보면서 단지의 갯수를 파악해야하므로 완전탐색의 형태가 필요하다는 점을 알았다. 

from collections import deque

n=int(input())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

visited=[[0]*n for _ in range(n)]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(graph,start,visited):
  q=deque([start])
  visited[start[0]][start[1]]=1
  house_count=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0 and graph[nx][ny]==1:
        visited[nx][ny]=1
        q.append((nx,ny))
        house_count+=1
  return house_count

count=0
answer=[]
for i in range(n):
  for j in range(n):
    if graph[i][j]==1 and visited[i][j]==0:
      answer.append(bfs(graph,(i,j),visited))
      count+=1

answer.sort()
print(count)
for i in answer:
  print(i)