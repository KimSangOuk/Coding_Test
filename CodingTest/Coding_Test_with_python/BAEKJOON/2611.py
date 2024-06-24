# 풀이시간 40분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 정점과 간선으로 이뤄진 그래프에서 무조건 적으로 한 정점 1에서 시작해서 1로 들어오기 때문에 한쪽 방향을 지향하는 그래프 형태를 가지고 있으며 1번 지점을 지나지 않고서는 다시 돌아오지 않기 때문에 1번 지점을 제외하고는 순환하지 않는다는 것을 알 수 있다. 그렇기 때문에 1번으로 이어지는 선이나 1번에서 나가는 선을 끊는다면 한쪽 방향으로만 이어지는 그래프가 된다는 것을 알 수 있고 이런 형태의 그래프에서 가장 많은 점수를 누적시키는 문제의 형태는 위상정렬로 풀 수 있다는 생각을 할 수 있다. 1번을 처음에 먼저 포함시킨 상태에서 위상정렬을 수행하며 간선의 가중치를 누적시키면서 큰 값만을 저장하면 다시 1번으로 돌아왔을 때 최대 수치가 나온다. 경로 또한 이러한 가중치의 수치가 최대가 될 때, 정점에서마다 경로를 누적시키면서 진행하면 다시 1번으로 돌아왔을 때, 최대 수치를 지닌 경로가 나오게 된다. N이 1000이히 이기 때문에 경로의 수는 많아도 100만이고 그렇기 때문에 위상정렬의 시간복잡도 O(V+E)는 가능하다.

from collections import deque

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
visited=[False]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  indegree[b]+=1

def topology_sort():
  q=deque()
  result=[0]*(n+1)
  
  path=[[] for _ in range(n+1)]
  q.append(1)

  while q:
    now=q.popleft()
    for i in graph[now]:
      if visited[i[0]]:
        continue
      if result[i[0]]<result[now]+i[1]:
        result[i[0]]=result[now]+i[1]
        path[i[0]]=path[now]+[i[0]]
      indegree[i[0]]-=1
      if indegree[i[0]]==0:
        q.append(i[0])
        visited[i[0]]=True

  print(result[1])
  print(*([1]+path[1]))

topology_sort()