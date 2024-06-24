# 풀이시간 23분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 간선을 통해 모두 연결되어야 되는데 모두 연결되고 남은 간선의 가중치의 최댓값을 구하므로 연결되는 가중치의 합이 최솟값이 되는 최소 스패닝 트리 문제라는 것을 알 수 있다. 문자로 나타내지는 각 정점간의 가중치를 정렬하여 최소로 연결되는 값을 전체 간선의 가중치의 합에서 빼면 된다. n이 최대 50이기 때문에 간선의 갯수가 많아야 2500이 되서 ElogE가 가능해진다.

def find_parent(parent, x):
  if parent[x] != x:
    parent[x]=find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a=find_parent(parent, a)
  b=find_parent(parent, b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n=int(input())
parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

edges=[]
for i in range(1,n+1):
  array=list(input())
  for j in range(1,n+1):
    if array[j-1]==0:
      continue
    elif ord('a')<=ord(array[j-1])<=ord('z'):
      edges.append((ord(array[j-1])-ord('a')+1,i,j))
    elif ord('A')<=ord(array[j-1])<=ord('Z'):
      edges.append((ord(array[j-1])-ord('A')+27,i,j))

edges.sort()
all_value=0
connect=0
for edge in edges:
  cost,a,b=edge
  all_value+=cost
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    connect+=cost

all_connect=True
for i in range(1,n):
  if find_parent(parent,i)!=find_parent(parent,i+1):
    all_connect=False
    break

if all_connect:
  print(all_value-connect)
else:
  print(-1)