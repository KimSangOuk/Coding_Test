# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 풀이 할 때, 데이터의 형태가 그래프로 나타나지고 전파형태를 구하는 것이기 때문에 BFS/DFS 탐색으로 구하는 것이 간편하며 데이터의 수도 최대 100개 이기 때문에 O(N)으로 구해도 가능ㅎ다. 단, 이 경우에도 단방향의 간선만 주어졌기 때문에 양방향으로 확대해서 풀어야 한다.

from collections import deque
v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]
for i in range(e):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(v+1):
  graph[i].sort()

visited=[False]*(v+1)

def bfs(graph,start,visited):
  visited[start]=True
  q=deque([start])
  while q:
    new=q.popleft()
    for i in graph[new]:
      if not visited[i]:
        visited[i]=True
        q.append(i)

bfs(graph,1,visited)
count=0
for i in range(1,v+1):
  if visited[i]==True:
    count+=1

print(count-1)