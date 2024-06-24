# 풀이시간 15분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 위상정렬을 풀면서 마지막으로 사이클이 있는지 즉, 위상정렬이 가능한지를 묻는 문제이다. 사이클이 있는지 확인하는 방법은 모든 정렬을 완료되기 전에 q가 비어서 알고리즘이 종료되는 것인데, 이를 확인하기 위해서는, indegree가 전부 0이 되었는지 확인하면 된다.
# 시간복잡도는 가능하다.

from collections import deque
import sys

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
  arr=list(map(int,input().split()))
  number=arr[0]
  sequence=arr[1:]
  for i in range(0,number-1):
    first=sequence[i]
    second=sequence[i+1]
    graph[first].append(second)
    indegree[second]+=1

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

  cycle=False
  for i in range(1,n+1):
    if indegree[i]!=0:
      cycle=True
      break
  if cycle:
    print(0)
  else:
    for i in result:
      print(i)

topology_sort()