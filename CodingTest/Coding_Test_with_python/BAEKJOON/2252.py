# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 한 방향의 간선으로 이루어진 그래프가 주어지고 그 그래프에서 순서대로 출력하는 문제 이기 때문에 위상정렬을 생각해볼 수 있다. 이 때, 시간복잡도는 O(V+E)이기 때문에 가능하다.

from collections import deque
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1

def topology_sort():
  q=deque()
  result=[]

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
  
  return result

result=topology_sort()

for i in result:
  print(i,end=' ')