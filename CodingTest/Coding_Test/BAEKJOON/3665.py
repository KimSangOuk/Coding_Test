# 이것이 취업을 위한 코딩테스트다 part03 '45. 최종 순위'와 동일
from collections import deque
import sys

input=sys.stdin.readline

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

for tc in range(int(input())):
  n=int(input())
  graph=[[] for _ in range(n+1)]
  
  prev_rank=list(map(int,input().split()))

  indegree=[0]*(n+1)

  for i in range(n):
    for j in range(i+1,n):
      graph[prev_rank[i]].append(prev_rank[j])
      indegree[prev_rank[j]]+=1

  m=int(input())
  for _ in range(m):
    a,b=map(int,input().split())
    if b in graph[a]:
      graph[a].remove(b)
      indegree[b]-=1
      graph[b].append(a)
      indegree[a]+=1
    elif a in graph[b]:
      graph[b].remove(a)
      indegree[a]-=1
      graph[a].append(b)
      indegree[b]+=1

  result=topology_sort()
  
  cycle=False
  for i in range(1,n+1):
    if indegree[i]!=0:
      cycle=True

  if cycle:
    print("IMPOSSIBLE",end=' ')
  else:
    for i in result:
      print(i,end=' ')
  print()