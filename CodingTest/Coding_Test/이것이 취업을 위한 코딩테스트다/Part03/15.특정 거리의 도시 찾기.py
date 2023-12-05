# 풀이시간 50분/30분 시간제한 2초 메모리제한 256MB
# 1회차 오답 - 풀이 시간 초과
# N이 최대 300,000이기 때문에 O(N)이 걸리는 DFS/BFS로 풀면 된다는 생각이 들었음. 게다가 최단 거리의 문제이기 때문에 BFS로 푸는 편이 훨씬 쉬울 거라는 생각도 듬
# 풀이에는 시간이 얼마 안걸렸으나 출력 오류를 고치는데 시간을 많이 잡아먹었다. 첫 번째 인덱스를 문제에 맞춰서 두다보니 +1을 해서 고려하느라 시간이 많이 잡아먹혔다. 하지만 이러한 점도 시간내에 해결되었다.
# 두번째는 방문한 것의 처리를 다른 것들과 다르게 하는 부분에서 재방문의 가능성이 있다는 것을 무시하고 푼 점이 문제가 되었다. 처음 접해보는 경우라서 다시 재방문이 되는 경우를 빼먹고 있었는데 그러한 점을 숫자로 처리할 때의 미숙함과 맞물리면서 재방문의 반복 처리가 일어나 문제가 되었다.***
# 또한 리스트의 표현이 길어지면서 어떤 표현이 무엇을 나타내는지 헷갈리기 시작하니 이부분에서 꼬여서 문제가 되었다. 이러한 부분은 변수의 이름을 따로 두어서 풀었다면 더 빨리 해결할 수 있을 것 같다.

# 2회차 풀이


# 1회차 풀이
from collections import deque

n,m,k,x=map(int,input().split())
# 여기서가 문제의 시작임. [[] for _ in range(n+1)]이 안되는줄 앎. *****
graph=[[0] for _ in range(n+1)]

# print(graph)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)

#print(graph)
visited=[-1]*(n+1)

def bfs(graph,start,k):
  queue=deque([start])
  visited[start]=0
  while queue:
    v=queue.popleft()
    for i in range(1,len(graph[v])):
      # 위에서의 문제때문에 굳이 0을 앞에 하나 더 넣느라 표현이 복잡해지기 시작.
      # 이부분에서 표현이 복잡해짐 + 방문을 숫자로 표시하기 시작하면서 재방문의 경우를 염두해 두지 않고 풀었기에 이런일이 생겼다.
      # 숫자 방문 시 앞으로만 나아간다고 생각하고 다시 돌아오는 경우는 True와 False의 경우에서는 없었기에 방심하고 있던 부분이었다.
      if 0> visited[graph[v][i]]:
        visited[graph[v][i]]=visited[v]+1
        queue.append(graph[v][i])
  #print(visited)
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

# # 답안 예시
# from collections import deque

# # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x =map(int,input().split())
# graph = [[] for _ in range(n+1)]

# # 모든 도로 정보 입력받기
# for _ in range(m):
#   a,b=map(int,input().split())
#   graph[a].append(b)
  
# # 모든 도시에 대한 최단 거리 초기화
# distance=[-1]*(n+1)
# distance[x]=0 # 출발 도시까지의 거리는 0으로 설정

# # 너비 우선 탐색(BFS) 수행
# q=deque([x])
# while q:
#   now = q.popleft()
#   # 현재 도시에서 이동할 수 있는 모든 도시를 확인
#   for next_node in graph[now]:
#     # 아직 방문하지 않은 도시라면
#     if distance[next_node]==-1:
#       # 최단 거리 갱신
#       distance[next_node]=distance[now]+1
#       q.append(next_node)

# # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
# check=False
# for i in range(1,n+1):
#   if distance[i]==k:
#     print(i)
#     check=True

# # 만약 최단 거리가 K인 도시가 없다면, -1 출력
# if check==False:
#   print(-1)