# 풀이시간 20분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# DFS 연습 문제로써 풀기 시작했기 때문에, DFS로 시작했다. 각 정점이 끊어져있을 수 있기 때문에 모든 정점을 탐색하지만은 처음 탐색하는 노드는 1로 시작해서 각 방문시에 부호를 바꿔서 방문을 표시해 준다. 이 때, 방문 했지만 전과 같은 방문 부호를 가지고 있다면 이분 그래프가 될 수 없기 때문에 No를 체크해주면 된다. 처음 시도시, 모든 정점을 방문하면서 방문 체크를 새롭게 했다가 시간 초과가 나와서 모든 정점만 체크해준다는 뜻으로 방문표시가 된 곳은 순환 안해도 되게 만들어서 O(N)에 가능하게 만들었다.
from collections import deque

def bfs(start):
  q=deque()
  visited[start]=1
  q.append(start)
  while q:
    x=q.popleft()
    for i in graph[x]:
      if visited[i]==0:
        visited[i]=-visited[x]
        q.append(i)
      elif visited[i]==visited[x]:
        return False
  return True

for tc in range(int(input())):
  v,e=map(int,input().split())
  graph=[[] for _ in range(v+1)]
  for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

  answer=True
  visited=[0]*(v+1)
  for i in range(1,v+1):
    if visited[i]==0 and not bfs(i):
      answer=False
      break
  if answer:
    print("YES")
  else:
    print("NO")
  