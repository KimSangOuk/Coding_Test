from collections import deque

def topology_sort():
    q=deque()
    result=[]

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            result.append(i)

    for i in range(1,n+1):
        if len(q)==0:
            print('IMPOSSIBLE')
            return
        if len(q)>1:
            print('?')
            return

        now=q.popleft()
        for j in graph[now]:
            indegree[j]-=1
            if indegree[j]==0:
                q.append(j)
                result.append(j)
    print(*result)


for tc in range(int(input())):
    n=int(input())
    last_year_rank=list(map(int,input().split()))
    indegree=[0]*(n+1)
    graph=[[] for _ in range(n+1)]
    for i in range(0,n-1):
        for j in range(i+1,n):
            indegree[last_year_rank[j]]+=1
            graph[last_year_rank[i]].append(last_year_rank[j])

    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b]-=1
            indegree[a]+=1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a]-=1
            indegree[b]+=1

    topology_sort()

# 2회차 풀이
# 전에 풀었던 풀이대로 생각도 나고 일관성이 없는 잘못된 정보일 경우에 노드 횟수만큼 돌렸을 때, 큐를 비우는 작업이 끝나버려 사이클이 발생한다는 점도 알고 있었다. 하지만 확실한 순위를 만들 수 없는 경우의 뜻을 이해를 하지 못했다. 확실한 순위를 만들 수 없다는 것이 즉, 순위를 만들 수는 있으나 여러가지 케이스가 나올 수 있다는 경우라는 것을 말이다.
# 이것은 한번 더 풀어보면서 정확히 케이스를 외우고 넘어가는 것이 좋다고 생각해서 다시 풀기로 하였다.

# 풀이시간 35분/60분 시간제한 1초 메모리제한 256MB
# 1회차 정답 - 하지만 풀이에서 배울게 있다고 생각해서 다시 풀기, 특히 2개씩 들어가는 것을 표현하는 부분이나 사이클이 발생하는 것을 표현한 부분이 색달라서
# 단순하게 생각하면 순위를 구하는 문제이고 순위가 바뀌었을 때, 정해진 순서대로 출력하는 문제이기 때문에 위상 정렬을 생각해볼 수 있다. n의 수가 500이기 때문에 모든 수를 연결 하더라도 O(V+E)의 시간복잡도를 통과할 수 있다.
# 나의 풀이의 경우에는 순위별로 모든 간선을 연결한 후, 바뀌는 부분만 방향을 반대로 뒤집어서 출력하면 되었다. 이 때, 사이클이 발생한다면 문제의 요구대로 IMPOSSIBLE을 출력한다. 하지만 나의 풀이의 경우에는 확실한 순위를 찾을 수 없는 경우, 즉 동시 진행으로 나아가는 경우가 없다는 것을 깨닫고 이러한 경우를 표현하지 않았다.

# 1회차 풀이 - 정답
# 답은 맞았지만, 답안지 풀이에서 배울점이 있었다.
# 첫번째, 모든 원소를 각 연결할 때, 이차원배열로 graph를 표현할 수도 있다는 점, 알고는 있었지만 쓰는 경우는 처음 보았기에 눈여겨 보았다.
# 두번째, 사이클과 동시 진행(즉, 순위가 확실하지 않은 경우)를 표현하는 것을 배웠다. 단 n개만 진행하기 때문에 사이클은 indgree가 전부 진행하는지 보아도 되지만, n개 진행을 이용해서 단 n번만 for문을 실행하면서 나아간 후, 그 전에 q가 비어버린다면 cycle 있다고 선언하는 것이다. 또한 q에 두개 이상이 담긴다면(동시 진행이 없으면 들어가는 방향 화살표가 0인 수가 하나 이상 생길 수 없어서) 동시 진행을 캐치할 수 있다는 것을 배웠다.
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

# 답안 예시
from collections import deque

# 테스트 케이스(Test Case)만큼 반복
for tc in range(int(input())):
  # 노드의 개수 입력 받기
  n=int(input())
  # 모든 노드에 대한 진입차수는 0으로 초기화
  indegree=[0]*(n+1)
  # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
  graph=[[False]*(n+1) for _ in range(n+1)]

  # 작년 순위 정보 입력
  data=list(map(int,input().split()))
  # 방향 그래프의 간선 정보 초기화
  for i in range(n):
    for j in range(i+1,n):
      graph[data[i]][data[j]]=True
      indegree[data[j]]+=1

  # 올해 변견된 순위 정보 입력
  m=int(input())
  for _ in range(m):
    a,b=map(int,input().split())
    # 간선의 방향 뒤집기
    if graph[a][b]:
      graph[a][b]=False
      graph[b][a]=True
      indegree[b]-=1
      indegree[a]+=1
    elif graph[b][a]:
      graph[b][a]=False
      graph[a][b]=True
      indegree[a]-=1
      indegree[b]+=1

  # 위상 정렬(Topology Sort) 시작
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q=deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 떄는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  cycle=False # 그래프 내 사이클이 존재하는지 여부
  certain=True # 위상 정렬 결과가 오직 하나인지의 여부

  # 정확히 노드의 개수만큼 반복
  for i in range(1,n+1):
    # 큐가 비어 있다면 사이클이 발생했다는 의미
    if len(q)==0:
      cycle=True
      break
    # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
    if len(q)>=2:
      certain=False
      break
    # 큐에서 원소 꺼내기
    now=q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for j in range(1,n+1):
      if graph[now][j]:
        indegree[j]-=1
        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[j]==0:
          q.append(j)

  # 사이클이 발생하는 경우(일관성이 없는 경우)
  if cycle:
    print("IMPOSSIBLE")
  # 위상 정렬 결과가 여러 개인 경우
  elif not certain:
    print("?")
  # 위상 정렬을 수행한 결과 출력
  else:
    for i in result:
      print(i,end=' ')
    print()