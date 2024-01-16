# 풀이시간 10분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 지점을 탐색한 순서대로 저장해 두었다가 출력하는 문제이다. DFS 연습중이므로 DFS로 풀었다. 오름차순대로 탐색해 들어가야하기 때문에 저장한 그래프를 정렬하고 탐색을 수행해야 한다.

import sys
sys.setrecursionlimit(10**5)

n,m,r=map(int,input().split())

graph=[[] for i in range(n+1)]
visited=[0]*(n+1)
index=1

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,n+1):
  graph[i].sort()

def dfs(graph,s,visited):
  global index
  visited[s]=index
  index+=1
  for i in graph[s]:
    if visited[i]==0:
      dfs(graph,i,visited)

dfs(graph,r,visited)
for i in range(1,n+1):
  print(visited[i])