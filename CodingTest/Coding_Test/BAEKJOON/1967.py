# 풀이시간 25분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 한 트리에서 최댓값을 구한 다음, 그 트리에서의 가장 긴 루트를 가진 노드가 제일 긴 노드가 되기 때문에 그 노드에서 부터의 다른 노드까지의 길이를 다시 구하면 된다. DFS로 풀었다.

import sys
sys.setrecursionlimit(10**5)

n=int(input())

graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)

for _ in range(n-1):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dfs(v):
  for i in graph[v]:
    if visited[i[0]]==-1:
      visited[i[0]]=visited[v]+i[1]
      dfs(i[0])

visited[1]=0
dfs(1)

max_index=0
max_value=0
for i in range(1,n+1):
  if visited[i]>max_value:
    max_index=i
    max_value=visited[i]

visited=[-1]*(n+1)
visited[max_index]=0
dfs(max_index)
print(max(visited))