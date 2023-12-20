# 풀이시간 20분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 문제의 데이터가 그래프 형태로 주어지고 각 간선에는 가중치가 주어져있다. 이러한 상황에서 목표로 설정한 두 지점을 잇는 길들 중 가중치가 가장 낮은 경로를 찾아야 하는데, 이 때 이어져있기만 하면 상관없기 때문에, 순환할 필요가 없다고 생각했다. 그러는 도중 가중치가 높은순으로 도로를 잇는데, 사이클이 발생하지 않게 도로를 놓아간다면 목적지가 이어지는 순간 가장 낮은 가중치가 결과값이 된다는 결론에 도달하였다. 최소 신장 트리를 반대로 생각하면서 목표한 지점을 찾는다면 멈추는 식인 것이다.
# 시간복잡도의 경우 ElogE가 정렬로 인해 발생하는데, M이 100,000이기 때문에 가능하다.

import sys

input = sys.stdin.readline

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

n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

edges=[]
for _ in range(m):
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort(reverse=True)

start,end=map(int,input().split())

for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    weight=cost
    if find_parent(parent,start)==find_parent(parent,end):
      break

print(weight)