# 풀이시간 1시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 가족 관계도에서 위상정렬을 수행하면서 전의 값의 반을 더해주면 되는 문제이다.

from collections import deque
import copy

n,m=map(int,input().split())

graph=dict()
cost=dict()
# 유토피아 세운 사람 포함
indegree=dict()
first=input()
cost[first]=1
indegree[first]=0
for _ in range(n):
  now,father,mother=map(str,input().split())
  if father not in graph:
    graph[father]=[]
  if mother not in graph:
    graph[mother]=[]
  graph[father].append(now)
  graph[mother].append(now)
  if father not in cost:
    cost[father]=0
  if mother not in cost:
    cost[mother]=0
  if father not in indegree:
    indegree[father]=0
  if mother not in indegree:
    indegree[mother]=0
  cost[now]=0
  indegree[now]=2

candidate=[]
for _ in range(m):
  name=input()
  if name not in cost:
    cost[name]=0
  if name not in indegree:
    indegree[name]=0
  candidate.append(name)
  
def topology_sort():
  q=deque([])

  result=copy.deepcopy(cost)

  for i in indegree.keys():
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    if now not in graph:
      continue
    for child in graph[now]:
      result[child]+=float(result[now]/2)
      indegree[child]-=1
      if indegree[child]==0:
        q.append(child)
  
  answer=""
  max_value=0
  for c in candidate:
    if max_value<result[c]:
      max_value=result[c]
      answer=c
  print(answer)

topology_sort()