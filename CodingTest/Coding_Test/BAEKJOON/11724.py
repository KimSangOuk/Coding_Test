# 풀이시간 10분 시간제한 3초 메모리제한 512MB
# 1회차 정답
# 간단히 정점과 간선을 문제에서 언급했기 때문에 그래프 문제이며 이 그래프를 탐색하며 전체 연결 횟수를 구하는 문제이기 때문에 DFS/BFS로 풀면 되는 문제이다. 이 때, 완전 탐색으로 전체 정점을 체크하면서 풀면 된다.
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited=[False]*(n+1)

def dfs(graph,start,visited):
  visited[start]=True
  for i in graph[start]:
    if not visited[i]:
      dfs(graph,i,visited)

count=0
for i in range(1,n+1):
  if visited[i]==False:
    dfs(graph,i,visited)
    count+=1
print(count)