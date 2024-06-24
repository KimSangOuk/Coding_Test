# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 등급에 따라 순차적으로 진행되면서 가장 큰 시간으로 이어지는 위상 정렬문제임을 그래프를 그려보며 조건을 보면 알 수 있다. 그래서 등급에 따라 그래프를 만들기 위해 기록을 받으며 등급별로 노드의 번호를 받고 노드번호별로 동작속도를 저장해두었다. 그리고 난 뒤 계급은 많아야 0,1차이가 나기 때문에 모든 등급은 순차적으로 하나씩 커지고 문제에서도 바로 하나 낮은 단계라고 명시되어 있기 때문에 바로 하나 차이 나는 등급들 끼리 낮아짐에 따라 그래프로 이어 완성시킨다. 그리고 난 후 위상정렬을 수행하며 다음 칸으로 이어질 때, 그 전까의 결과값에 간선의 가중치와 현재 노드의 수치를 더해주면서 최댓값만을 기록하면 된다.

from collections import deque
import copy

n=int(input())
rank=[[] for _ in range(n+1)]
cost=[0]*(n+1)
for i in range(1,n+1):
  r,t=map(int,input().split())
  rank[r].append(i)
  cost[i]=t
  
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
for i in range(1,n):
  for f in rank[i]:
    for s in rank[i+1]:
      graph[f].append((s,(f-s)**2))
      indegree[s]+=1

def topology_sort():
  q=deque()
  result=copy.deepcopy(cost)
  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i,c in graph[now]:
      result[i]=max(result[i],result[now]+cost[i]+c)
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
  # print(result)
  print(max(result))

topology_sort()