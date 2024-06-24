# 풀이시간 5분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순히 스패닝 트리에서 마을을 두개로 나누기 때문에 나중에 추가된 가장 긴 경로의 가중치를 빼면 되는 문제이다. 간선의 수가 1,000,000이지만 ElogE에 시간제한이 2초기 때문에 정상적으로 작동한다.

import sys

input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x]!=x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a=find_parent(parent, a)
  b=find_parent(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

edges=[]
for _ in range(m):
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

result=0
last=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost
    last=cost

print(result-last)