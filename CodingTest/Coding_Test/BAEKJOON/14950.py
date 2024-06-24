# 풀이시간 33분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 1번 도시부터 모든 도시를 연결해 가는데 도시를 연결할 때마다 간선의 가중치 이외에도 스택처럼 추가 가중치가 쌓이기 때문에 현재 연결된 집단에서 도시를 연결해 나가야한다. 그렇기 때문에 정점을 연결할 때마다 연결된 간선을 추가하는 식으로 진행해야 한다. 최소 스패닝 트리를 풀되 현재 가장 가중치가 작은 간선만 연결하므로 힙큐로 넣고 꺼내가며 풀면 된다고 생각했다. 그래서 큐에 맨 처음 1번 노드와 연결된 모든 간선을 넣고 간선을 하나씩 꺼내가며 연결이 되어 있는지 확인하고 연결이 되어 있지 않다면 연결하고 추가되는 간선을 넣는 식으로 반복문을 시행하였다.

import heapq

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m,t=map(int,input().split())

parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

graph=[[] for _ in range(n+1)]
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

q=[]
now=1
t_stack=0
result=0

for i in range(len(graph[now])):
  heapq.heappush(q,(graph[now][i][1],now,graph[now][i][0]))

while q:
  cost,now,next=heapq.heappop(q)
  if find_parent(parent,now)!=find_parent(parent,next):
    union_parent(parent,now,next)
    result+=(cost+t_stack)
    t_stack+=t

    for i in range(len(graph[next])):
      heapq.heappush(q,(graph[next][i][1],now,graph[next][i][0]))

print(result)