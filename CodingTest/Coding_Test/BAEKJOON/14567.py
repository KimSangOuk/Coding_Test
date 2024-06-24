# 풀이시간 10분 시간제한 5초 메모리제한 256MB
# 1회차 정답
# 각 선수과목이 있고 그래프 형태일 때, 각 정점까지의 비용을 구하는 문제이기 때문에, 위상정렬을 고민해 볼 수 있다. 이 때, 시간복잡도는 O(N+M)이기 때문에 가능하다. 각 위상정렬을 하는 중 누적할 배열을 하나 더 둬서 그 값을 전까지의 누적된 최댓값과 현재 값과의 덧셈으로 구하면된다. 이때, 여러곳에서 들어올 수 있기 때문에 최대값으로 해두어야된다.

from collections import deque
import copy

def topology_sort():
  q=deque([])

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      indegree[i]-=1
      result[i]=max(result[i],result[now]+cost[i])
      if indegree[i]==0:
        q.append(i)

n,m=map(int,input().split())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1

cost=[1]*(n+1)
result=[1]*(n+1)

topology_sort()
for i in range(1,n+1):
  print(result[i],end=' ')