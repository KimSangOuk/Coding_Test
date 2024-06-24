# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 먼저 데이터의 양은 최대 100이기 떄문에 어떤 특정한 경우에서 특정한 경우까지의 값을 구하는 탐색을 이용하면 되는데, 이때 단순히 dfs와 bfs를 사용할 수 있다. 이 문제의 경우 dfs를 연습중이였기에 dfs로 풀었다.

n=int(input())

start,end=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)

m=int(input())

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v,prev):
  visited[v]=visited[prev]+1
  for i in graph[v]:
    if visited[i]==-1:
      dfs(i,v)

dfs(start,0)
print(visited[end])