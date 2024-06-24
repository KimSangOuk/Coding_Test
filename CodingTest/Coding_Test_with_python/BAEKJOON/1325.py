# 풀이시간 10분 시간제한 5초 메모리제한 256MB
# 1회차 정답
# 각 그래프에서 모든 지점에서 다른 지점에 도달하는 갯수를 각 파악한 다음 최댓값이 되는 지점에 컴퓨터들을 출력하는 문제이다. 그래프 탐색인 BFS를 각 지점에서 수행하며 풀면 된다.

from collections import deque

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b=map(int,input().split())
  graph[b].append(a)

answer=[]
max_value=0

def bfs(start):
  global answer, max_value
  visited=[False]*(n+1)
  q=deque()
  q.append(start)
  visited[start]=True
  while q:
    now=q.popleft()
    for i in graph[now]:
      if not visited[i]:
        visited[i]=True
        q.append(i)
  count=0
  for i in range(1,n+1):
    if visited[i]:
      count+=1
  if count==max_value:
    answer.append(start)
  elif count>max_value:
    answer=[]
    answer.append(start)
    max_value=count

for i in range(1,n+1):
  bfs(i)

answer.sort()
for i in answer:
  print(i,end=' ')