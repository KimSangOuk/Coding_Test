# 풀이시간 10분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 연결을 주어진 대로 하고 각 집합 중 대표 하나씩 출력하면 되는 문제이다. 그렇기 때문에 find_union인 서로소 집합문제로 접근할 수 있는데 이 때, 300,000이기 때문에 V+MlogV로 가능하다. 집합으로 parent를 변형해서 같은건 하나씩 들어있게 해서 출력하였다.

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

for _ in range(n-2):
  a,b=map(int,input().split())
  union_parent(parent,a,b)

for i in range(1,n+1):
  find_parent(parent,i)

answer=set(parent[1:])

print(*answer)
