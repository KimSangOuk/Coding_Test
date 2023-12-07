# 풀이시간 20분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 풀이는 단순히 그래프를 그려서 시작점 부터 탐색하면서 그 전 정점을 기록하면 되는 문제였다. DFS/BFS로 간단히 풀 수 있었다. 단, 노드의 개수가 100,000이기 때문에 인접 행렬 방식은 이용하지 않는 것이 좋으며 인접 리스트 방식을 사용하는 것이 좋다.
# 여기서 한가지 배운게 재귀 반복문 런타임 에러가 너무 재귀의 수가 많아지면 뜬다는 것이였다. 이 때, 재귀 함수의 이러한 횟수제한을 늘리려면 밑에 코드를 사용하면 된다.
# sys.setrecursionlimit(10**6)

from collections import deque

n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited=[False]*(n+1)
answer=[1]*(n+1)

def bfs(graph,start,visited):
  q=deque([start])
  visited[start]=True
  while q:
    new=q.popleft()
    for i in graph[new]:
      if not visited[i]:
        answer[i]=new
        visited[i]=True
        q.append(i)

bfs(graph,1,visited)

for i in range(2,n+1):
  print(answer[i])