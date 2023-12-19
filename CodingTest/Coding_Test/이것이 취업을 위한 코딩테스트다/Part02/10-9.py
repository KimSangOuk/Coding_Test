from collections import deque
import sys

input=sys.stdin.readline

# 노드의 개수 입력받기
n=int(input())
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph=[[] for _ in range(n+1)]
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree=[0]*(n+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1,n+1):
  arr=list(map(int,input().split()))
  # 첫 번째 수는 시간 정보를 담고 있음
  cost=arr[0]
  target=arr[1:-1]
  if len(target)!=0:
    for k in target:
      graph[k].append((i,cost))
      indegree[i]+=1
  else:
    graph[0].append((i,cost))
    indegree[i]+=1

def topology_sort():
  q=deque() # 큐 기능을 위한 deque 라이브러리 사용
  # 각 강의 시간을 0으로 초기화
  result=[0]*(n+1) # 알고리즘 수행 결과를 담을 리스트

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(n+1):
    if indegree[i]==0:
      q.append(i)

  # 큐가 빌 때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now=q.popleft()
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      result[i[0]]=max(result[i[0]],result[now]+i[1])
      indegree[i[0]]-=1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 진입
      if indegree[i[0]]==0:
        q.append(i[0])
        
  # 위상 정렬을 수행한 결과 출력
  for i in range(1,n+1):
    print(result[i])

topology_sort()