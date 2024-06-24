# 이것이 취업을 위한 코딩테스트다 part03 '15. 특정 거리의 도시 찾기'와 동일
from collections import deque

n,m,k,x=map(int,input().split())
graph=[[0] for _ in range(n+1)]

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)

visited=[-1]*(n+1)

def bfs(graph,start,k):
  queue=deque([start])
  visited[start]=0
  while queue:
    v=queue.popleft()
    for i in range(1,len(graph[v])):
      if 0> visited[graph[v][i]]:
        visited[graph[v][i]]=visited[v]+1
        queue.append(graph[v][i])
  answer=[]
  for i in range(1,n+1):
    if visited[i]==k:
      answer.append(i)
  return answer

answer=bfs(graph,x,k)
if len(answer)==0:
  print(-1)
else:
  for i in answer:
    print(i)