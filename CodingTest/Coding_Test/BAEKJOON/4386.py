# 풀이시간 10분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 각 별들의 좌표가 주어졌고 그 별들을 잇는 선들로 이루어진 최소 비용 트리를 구하는 최소 스패닝 트리 문제이다. 그렇기 때문에, 각 좌표에서 다른 좌표까지의 모든 선을 구해서 정렬한다음 최소 스패닝 트리를 구하면 된다.

import sys
import math

input=sys.stdin.readline

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

n=int(input())
stars=[(0,0)]

for _ in range(n):
  x,y=map(float,input().split())
  stars.append((x,y))

parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

edges=[]

for i in range(1,n+1):
  for j in range(i+1,n+1):
    x1,y1=stars[i]
    x2,y2=stars[j]
    cost=math.sqrt((x1-x2)**2+(y1-y2)**2)
    edges.append((cost,i,j))

edges.sort()
result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(round(result,2))