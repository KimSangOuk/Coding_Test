# 풀이시간 36분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 그룹을 이루고 있는 사람들 중에 타인들과의 최단거리의 최댓값이 최소가 되는 사람을 찾는 문제이다. 먼저 그룹을 그분하고 사람들을 분리하기 위해 분리 집합인 서로소 find_union 연산을 통해 사람들의 글부을 묶고 그 사람들의 모든 거리가 필요하기 때문에 플로이드 워셜 함수를 통해 상호 간 최단거리를 구한다. 그런 후, 그룹 내 사람들 서로를 비교해서 최단거리의 최댓값이 최소가 되는 사람을 구하면 되는 문제이다.

n=int(input())
m=int(input())

INF=int(1e9)

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

parent=[0]*(n+1)
for i in range(n+1):
  parent[i]=i

graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  union_parent(parent,a,b)
  graph[a][b]=1
  graph[b][a]=1

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for i in range(1,n+1):
  find_parent(parent,i)

group=[[] for _ in range(n+1)]
for i in range(1,n+1):
  group[parent[i]].append(i)

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

count=0
answer=[]
for i in range(1,n+1):
  if len(group[i])>0:
    count+=1
    min_value=INF
    choice=-1
    for j in range(0,len(group[i])):
      max_value=0
      for k in range(0,len(group[i])):
        if j!=k and max_value<graph[group[i][j]][group[i][k]]:
          max_value=graph[group[i][j]][group[i][k]]
      if max_value<min_value:
        min_value=max_value
        choice=group[i][j]
    answer.append(choice)

print(count)
answer.sort()
for i in answer:
  print(i)
  