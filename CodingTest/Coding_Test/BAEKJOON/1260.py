# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 문제 자체에서 알고리즘을 지목해서 사용하라고 한 DFS/BFS의 기본 문제
# 간선과 정점 사이의 관계를 나타낼 때, 정렬이 어떤 영향을 미치는지 알 수 있는 문제였다.

from collections import deque

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

# print(graph)

visited_dfs=[False]*(n+1)
visited_bfs=[False]*(n+1)

def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

def bfs(graph,v,visited):
  visited[v]=True
  q=deque([v])
  while q:
    new=q.popleft()
    print(new,end=' ')
    for i in graph[new]:
      if not visited[i]:
        visited[i]=True
        q.append(i)

dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)