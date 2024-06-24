# 풀이시간 20분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 각 작업에 따라 그래프를 그린다음 선후 관계에 맞게 정렬하는 식의 문제이기 때문에 위상정렬로 접근하였다. 시간복잡도인 O(N+M)도 가능하다. 그렇기에 위상정렬로 풀면서 각 구간의 누적 가중치를 구해서 그 중 가장 큰 수가 끝까지 전부 수행했을 때, 걸린 시간이 된다.

from collections import deque

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

n=int(input())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
cost=[0]*(n+1)
result=[0]*(n+1)
for i in range(1,n+1):
  arr=list(map(int,input().split()))
  cost[i]=arr[0]
  result[i]=arr[0]
  k=arr[1]
  prev=arr[2:]
  for j in prev:
    graph[j].append(i)
    indegree[i]+=1

topology_sort()
print(max(result))