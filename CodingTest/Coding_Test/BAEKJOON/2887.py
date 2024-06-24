# 이것이 취업을 위한 코딩테스트다 part03 '44. 행성 터널'과 동일

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

array_x=[]
array_y=[]
array_z=[]
for i in range(1,n+1):
  x,y,z=map(int,input().split())
  array_x.append((x,i))
  array_y.append((y,i))
  array_z.append((z,i))

array_x.sort()
array_y.sort()
array_z.sort()

edges=[]
for i in range(0,n-1):
  cost_x=array_x[i+1][0]-array_x[i][0]
  cost_y=array_y[i+1][0]-array_y[i][0]
  cost_z=array_z[i+1][0]-array_z[i][0]
  edges.append((cost_x,array_x[i][1],array_x[i+1][1]))
  edges.append((cost_y,array_y[i][1],array_y[i+1][1]))
  edges.append((cost_z,array_z[i][1],array_z[i+1][1]))

edges.sort()
result=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(result)