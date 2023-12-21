# 풀이시간 30분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 단방향의 그래프에서 앞에 것을 이수해야 뒤에 것을 이수할 수 있는 위상정렬의 문제 형태를 띄고 있다. 시간복잡도 상으로도 가능하므로 문제에 접근할 수 있다.
# 각 노드로 새로 진입할 때, 가중치를 누적시켜야되는데, 이 때 현재의 노드의 값은 현재노드로 진입하기 전의 노드의 결과값과 현재의 노드의 가중치의 합이나 그 전에 현재의 노드 진입한 결과값 중 큰 값을 가지면 된다.

from collections import deque
import sys
import copy

input=sys.stdin.readline

def topology_sort(last):
  q=deque()

  result=copy.deepcopy(time)

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    
    for i in graph[now]:
      indegree[i]-=1
      result[i]=max(result[i],result[now]+time[i])
      if indegree[i]==0:
        q.append(i)
  
  return result[last]

for tc in range(int(input())):

  n,k=map(int,input().split())
  graph=[[] for _ in range(n+1)]
  indegree=[0]*(n+1)

  time=[0]*(n+1)
  tmp=list(map(int,input().split()))
  for i in range(1,n+1):
    time[i]=tmp[i-1]

  for _ in range(k):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

  last=int(input())
  
  result=topology_sort(last)

  print(result)