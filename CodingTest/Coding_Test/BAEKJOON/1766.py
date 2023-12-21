# 풀이시간 15분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 문제에서 먼저 푸는 문제가 있고 그 순서를 나열하라고 하였기 때문에, 먼저 전체적인 틀 면에서 위상 정렬 알고리즘을 생각해볼 수 있다. 이 때, 시간복잡도는 맞아 떨어지기 때문에 사용가능하다. 하지만 그 중에서도 작은 숫자가 먼저 나와야되는 조건이 붙기 때문에, 우리는 최소 힙을 사용하는 것을 생각해 볼 수 있다. 실제로 예시를 통해 확인해본 결과 deque 대신 최소 힙을 사용하면 우리가 원하는 결과가 도출 되는 것을 알 수 있다.

import heapq

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1

def topology_sort():
  q=[]

  for i in range(1,n+1):
    if indegree[i]==0:
      heapq.heappush(q,i)

  while q:
    now=heapq.heappop(q)
    print(now,end=" ")
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        heapq.heappush(q,i)

topology_sort()