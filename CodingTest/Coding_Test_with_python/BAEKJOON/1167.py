# 풀이시간 15분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 한 점을 기준으로 가장 먼 점에서 시작하는 점이 지름을 이루고 있는 양 끝 중 하나가 되기 때문에 가장 먼 지점을 찾기를 두번 시행해주면 되는 문제이다. 데이터의 크기가 100,000이기떄문에 DFS인 O(N)*2회로 가능하다.

v=int(input())
graph=[[] for i in range(v+1)]

for _ in range(v):
  arr=list(map(int,input().split()))
  for k in range(1,1+len(arr[1:-1]),2):
    graph[arr[0]].append((arr[k],arr[k+1]))

visited=[-1]*(v+1)

def dfs(v):
  for i in graph[v]:
    if visited[i[0]]==-1:
      visited[i[0]]=visited[v]+i[1]
      dfs(i[0])

visited[1]=0
dfs(1)
max_index=0
for i in range(1,v+1):
  if visited[max_index]<visited[i]:
    max_index=i

visited=[-1]*(v+1)
visited[max_index]=0
dfs(max_index)
print(max(visited))