# 풀이시간 10분/40분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 집과 도로로 이루어져 있고 이어지는 그래프를 만들었을 때, 그 도로의 비용의 값을 이용하는 문제이기 때문에 그래프 이론 중 크루스칼 알고리즘을 생각해 볼 수 있다. 이 때, 시간 복잡도가 ElogE로 가능하기 때문에 크루스칼 알고리즘으로 풀 수 있었다.
# 답은 전체 비용에서 이어지는 도로의 비용을 빼면 된다.
# 답안지와 같기 때문에 주석만 달았다.

import sys

input=sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트 노드가 찾을 때까지 재귀적으로 호출
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

# 노드의 개수와 간선의 개수 입력받기
n,m=map(int,input().split())
parent=[0]*n # 부모 테이블을 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
  parent[i]=i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((c,a,b))

# 간선을 비용순으로 정렬
edges.sort()
result=0 # 전체 가로등 비용
# 간선을 하나씩 확인하며
for edge in edges:
  cost,a,b=edge
  result+=cost
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result-=cost

print(result)