# 풀이시간 7분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순히 문제에서 집합끼리 합치고 그 집합의 부모 노드를 찾는 연산을 언급했기 때문에 서로소 집합을 이용한 알고리즘임을 알 수 있다. 이 때, 시간 복잡도는 V+Mlog2V이기 때문에 가능하다.

import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

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

for _ in range(m):
  oper,a,b=map(int,input().split())
  if oper==0:
    union_parent(parent,a,b)
  else:
    if find_parent(parent,a)==find_parent(parent,b):
      print("YES")
    else:
      print("NO")