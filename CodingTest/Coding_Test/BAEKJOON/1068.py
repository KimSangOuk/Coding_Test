# 풀이시간 25분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순히 그래프를 그린 후 지워지는 노드의 연결을 끊고 깊이 탐색을 수행하는데 이 때, 트리의 경우 순환이 없기 때문에 깊이 탐색에서 더 이상 나아갈 자식 노드가 없으면 리프 노드로 계산하는 문제이다. 단 맨 위의 노드가 삭제 될 시, 그 노드에도 접근할 수 없기 때문에 이 경우를 조건문으로 나타내 주어야 한다.

n=int(input())

arr=list(map(int,input().split()))
visited=[False]*n

start=-1
graph=[[] for _ in range(n)]

for i in range(n):
  if arr[i]==-1:
    start=i
  else:
    graph[arr[i]].append(i)

delete=int(input())

for i in range(n):
  for k in graph[i]:
    if k==delete:
      graph[i].remove(k)

answer=0

def dfs(s):
  global answer
  if s==delete:
    return
  visited[s]=True
  if len(graph[s])==0:
    answer+=1
  for i in graph[s]:
    if visited[i]==False:
      dfs(i)

dfs(start)
print(answer)