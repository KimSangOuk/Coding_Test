# 풀이시간 27분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 연결되는 두 정점 사이의 간선의 가중치의 최소값을 구하는 문제이고 정점과 간선을 주었기 때문에 그래프 문제라고 생각할 수 있다. 이 때, 그래프의 간선이 최소값이 되므로 큰 값부터 이었을 때, 두 지점이 이어지는 순간에 끝내는 문제라고 할 수 있다. 이러한 방식을 위해 최소 스패닝 트리의 역으로 큰 순으로 정렬해서 연결하다가 두 지점이 연결되는 순간이 최솟값 중 최대가 된다고 생각해서 풀었다. 시간복잡도는 간선이 300,000이기 때문에 정렬로 ElogE로 풀면 가능하다.

import sys
sys.setrecursionlimit((10**5)*3)

def find_parent(parent, x):
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
s,e=map(int,input().split())
edges=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  edges.append((c,a,b))

edges.sort(reverse=True)
path=True
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)

    if find_parent(parent,s)==find_parent(parent,e):
      break

if find_parent(parent,s)!=find_parent(parent,e):
  print(0)
else:
  print(cost)