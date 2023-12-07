# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 방향이 여러군데로 늘어났을 뿐 2차원 배열에서 주어진 방향에 따라 탐색하는 그래프 탐색, 즉 DFS/BFS로 풀 수 있는 문제이다. 시간복잡도의 경우도 2차원 배열이기 때문에 데이터가 최대 2,500이기 때문에 여유롭다고 할 수 있다.

def dfs(y,x):
  if y<0 or y>=h or x<0 or x>=w or graph[y][x]==0:
    return False
  if visited[y][x]==False and graph[y][x]==1:
    visited[y][x]=True
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x-1)
    dfs(y,x+1)
    dfs(y-1,x-1)
    dfs(y+1,x+1)
    dfs(y-1,x+1)
    dfs(y+1,x-1)
    return True
  return False

while True:
  w,h=map(int,input().split())
  if w==0 and h==0:
    break

  graph=[]
  for _ in range(h):
    graph.append(list(map(int,input().split())))

  visited=[[False]*w for _ in range(h)]

  count=0
  for i in range(h):
    for j in range(w):
      if visited[i][j]==False and graph[i][j]==1:
        dfs(i,j)
        count+=1
  
  print(count)