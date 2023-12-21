# 풀이시간 over/40분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이방식에 접근하지 못함
# 문제를 보았을 때, 행성간의 간선을 구해서 행성이 모두 연결되는 최소 거리를 구하는 최소 스패닝 트리의 알고리즘으로 풀 수 있다는 것을 알 수 있다. 행성의 개수가 100,000이기 때문에 최소 스패닝 트리의 ElogE를 적용시켜야 하는데, 간선의 개수가 원래 구하는 방법으로 구한다면 모든 행성을 각자 서로 연결시켜야 하므로 100,000*100,000/2가 나와서 시간복잡도 면에서나 메모리제한 면에서 불가능 하다는 것을 알 수 있다.
# 여기까지는 생각해 낼 수 있었다. 즉, 간선을 구하는 방법을 최소화 시켜서 풀어야되는데, 이중 포문을 쓰지 않고 각 간선을 건드려야 가능했다.
# 풀이에서는 각 x,y,z의 차이 중 최소가 되는 값이 행성 간의 거리가 되기 때문에 이를 이용하는데, 이 때, 각 x,y,z가 나눠져있으므로 따로 1차원 평면으로 생각해볼 수 있다. 각 좌표를 생각했을 때, 정렬했을 때, 각 좌표 사이의 거리가 각 행성사이의 거리의 최소 값의 후보가 되므로 이를 이용해서 풀수 있다. 이 것들을 간선으로 이용해서 풀이를 하면된다.
# 나는 왜 이 풀이를 생각하지 못했나? 거리를 구하기 위해서는 무조건 모든 점들끼리의 비교가 필요하고, 그래야 모든 후보군이 나온다고 생각했다. 왜? 특정점 사이의 비용만 구한다면 구할 수 없다고 생각했다. 즉, 밑에서의 논리의 증명이 필요했다. 또 다르게 표현한다면 1차원적으로 생각하지 못했다. 왜? 단순 거리의 문제로 받아들이지 않고 좌표를 따로 생각했기 때문이다. 왜? 이런 거리를 구할 때, 뜻으로 생각해보거나 좌표를 일차원적으로 바꿔서 생각해본 경험이 없기 때문이다.

# < 왜 정렬된 상태의 인접한 간선 이외에는 다른 선들은 고려하지 않는지? >
# 모든 축에 대해 인접하지 않은 두 정점 A와 B가 있다고 하자.
# 두 정점을 연결하는데 드는 비용을 결정하는 축의 값에 따라 모든 점을 축 위에 찍어 놓았다고 생각해보자.
# A와 B는 사이에 점이 최소 1개 이상 있을 것이다.
# 이 점들을 r0​,r1​,⋯,rk​라고 이름 붙여 보자.
# 이렇게 한 후, 모든 간선을(O(N2)의 간선) 추가하고 크루스칼 알고리즘을 수행한다고 해보자.
# 크루스칼 알고리즘은 가중치가 작은 간선들부터 차례로 검사하므로 E(A,B)를 검사하기 전에 E(A,r0​),E(r0​,r1​),E(r1​,r2​),⋯,E(rk​,B) 들을 먼저 검사했을 것이다.
# 크루스칼 알고리즘은 간선을 두 가지중 하나로 처리하는데,
# 1. 간선을 추가
# 2. 간선이 연결된 두 정점이 이미 하나의 컴포넌트이므로 추가하지 않음.
# 어떤 경우든 간에 검사한 간선의 양 쪽 정점은 하나의 컴포넌트였거나, 하나의 컴포넌트가 되므로 검사 후에는 반드시 하나의 컴포넌트라는 사실을 알 수 있다.
# 따라서 E(A,B)를 검사하는 시점에서는 반드시 A,B가 하나의 컴포넌트라는 사실을 알 수 있으므로 E(A,B)는 크루스칼 알고리즘에서 절대 추가되지 않는 간선임을 알 수 있다.
# 결국 임의의 축에 대해 인접하지 않은 두 정점 사이의 간선은 크루스칼 알고리즘 수행 과정에서 사용되지 않는다는 것을 알 수 있으므로, 인접한 두 정점 사이의 간선만을 이용해도 된다는 것을 알 수 있다.

# 즉, 너무 복잡하게 생각했었는데, min이 없다면 1차원적인 선에서, 크루스칼 알고리즘을 구한다고 치면 되는 거다. 그때, 간선을 구하는데, 건너 뛴 점을 생각할 필요가 없다는 뜻.
# 이러한 논리를 알고 있다면 역순으로 아이디어의 생각이 가능하다. 즉, 각 좌표 사이의 차이 중에서 가장 작은 값? 근데, 각 좌표에서는 모든 점을 비교할 필요가 없이 가까이에 있는 것만 생각하면 되잖아? -> 그러면 각 영역별로 정렬해서 인접한 간선만 구해서 그 중에서만 처리하자.

# 2회차 풀이




# 1회차 풀이
import sys
import heapq

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
parent=[0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

planets=[(0,0,0)]
for i in range(1,n+1):
  x,y,z=map(int,input().split())
  planets.append((x,y,z))

edges=[]
# 여기서 문제가 생긴다는 것을 깨달았지만, 개선하지 못했다.
for i in range(1,n+1):
  for j in range(i+1,n+1):
    cost=min(abs(planets[i][0]-planets[j][0]),abs(planets[i][1]-planets[j][1]),abs(planets[i][2]-planets[j][2]))
    edges.append((cost,i,j))

edges.sort()
print(edges)
result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(result)

# 답안 예시
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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

# 노드의 개수 입력받기
n= int(input())
parent=[0]*(n+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,n+1):
  parent[i]=i

x=[]
y=[]
z=[]

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1,n+1):
  data=list(map(int,input().split()))
  x.append((data[0],i))
  y.append((data[1],i))
  z.append((data[2],i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n-1):
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
  edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
  edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
  cost,a,b=edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(result)