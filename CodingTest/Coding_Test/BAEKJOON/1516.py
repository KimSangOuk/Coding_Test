# 풀이시간 15분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 위상정렬에서 현재 노드로 오는 가중치를 구하는 문제이다. 시간복잡도는 V가 500이기 때문에 n*(n+1)/2을 한 E가 +V를 해도 연산횟수가 괜찮기 때문에 가능하다.

from collections import deque
import copy
import sys

input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
cost=[0]*(n+1)
# result=[0]*(n+1)

for i in range(1,n+1):
  now_num=i
  arr=list(map(int,input().split()))
  cost[i]=arr[0]
  prev=arr[1:-1]
  for p in prev:
    graph[p].append(i)
    indegree[i]+=1

def topology_sort():
  q=deque()
  result=copy.deepcopy(cost)

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      result[i]=max(result[i],result[now]+cost[i])
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)

  for i in range(1,n+1):
    print(result[i])

topology_sort()

