# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 장난감이 만들어지는 부품을 화살표로 연결해보면 방향 비순환 그래프가 그려지는 걸 알 수 있고, 각 드는 부품의 갯수가 그 간선의 가중치가 되어 개수에 곱해진다는 것을 알 수 있다. 그렇기 때문에 각 간선을 타고 이동하는 시점에서 간선의 가중치를 곱해서 결과값에 더해서 누적시켜주면 각 부품이 몇개씩 필요한지 알 수 있다. 이때, 시간복잡도는 반복문을 한번 더 쓰기 때문에 O(N+M^2)이 될 수 있으나 전부 연결된 상태이기도 하고 하나의 노드로 수렴하기 때문에 최대 M이 100이하이기 때문에 가능하다고 볼 수 있다.

from collections import deque

def topology_sort():
  q=deque([])

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)
      result[i][i]=1
      root.add(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      for j in range(1,n+1):
        result[i[0]][j]+=result[now][j]*i[1]
      indegree[i[0]]-=1
      if indegree[i[0]]==0:
        q.append(i[0])
        
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
result=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  x,y,k=map(int,input().split())
  graph[y].append((x,k))
  indegree[x]+=1

root=set([])

topology_sort()
# print(result)

for i in range(1,n+1):
  if i in root:
    print(i,result[n][i])