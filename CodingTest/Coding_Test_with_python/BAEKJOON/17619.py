# 2회차 풀이

# 풀이시간 120분/60분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# x값의 범위가 겹치면 같은 그룹으로 칠 수 있고 다르면 다른 그룹으로 칠 수 있을 때, 그룹간을 비교해서 속해있는지 아니면 다른 그룹인지 확인하는 문제이다. 집합을 분리하고 그 집합에 소속되어 있는지 따지는 문제이기 때문에 서로소 집합 알고리즘을 생각해 낼 수 있다. 데이터의 크기도 최대 V가 100,000이기 때문에 V+MlogV로 풀 수 있다. 각 범위가 겹치도록 비교하기 위해서는 일단 정렬이 되어야 V회에 진행할 수 있기 때문에 V회에 각 통나무를 비교하기 위해서는 x1,x2순으로 정렬이 되어 있어야 한다. 이 때, 우리는 번호로 나중에 답을 찾을 것이기 때문에 번호를 달아서 범위를 따로 저장해두고 나머지는 번호를 달아서 정렬한다. 그런 후, 앞에서부터 비교하면서 범위가 겹쳐지는 경우 합치는데 이 때에도 집합에 포함되더라도 범위가 다르기 때문에 parent 뿐만 아니라 범위도 정정하면서 기록해나가야 한다. 우리는 앞에서부터 합쳐지기 때문에 맨 부모가 되는 범위만 지속적으로 업데이트 되면 된다. 그런 후 parent를 통해 q의 질문이 가능한지 확인해서 출력하면 된다.
# 시간이 꽤 오래걸렸는데 먼저 범위를 늘리면서 확인해야 하는 부분에서 오래걸렸고, 늘어나는 범위를 업데이트하기 위해 저장해두는 과정과 업데이트 과정에서 시간이 오래걸렸다. 순차적으로 진행하기 때문에 예외케이스로 앞뒤가 연결되어 있지 않지만 집합에 영역에 속하는 경우를 생각을 하는 과정에서 오래걸렸다. 이런 경우는 비교를 하는 경우에 예외가 되는 경우가 있지는 않은지 생각해보는 습관을 들여야 할 것 같다. 또한 데이터를 다루는 경우에는 find와 union의 특성상 parent[x]와 x가 같아질 수 있는지 확인하고 같아질 수 있다면 데이터를 parent에 함께 저장하고 같아질 수 없다면 따로 빼서 기록하는 방법을 써야한다는 것을 인지하고 있어야 겠다.

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

n,q=map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

array=[]
range_list=dict()

for i in range(1,n+1):
  x1,x2,y=map(int,input().split())
  range_list[i]=[x1,x2,y]
  array.append([i,x1,x2,y])

array.sort(key=lambda x:(x[1],x[2],x[3]))
for i in range(n-1):
  a=find_parent(parent,array[i][0])
  b=find_parent(parent,array[i+1][0])
  range_a=range_list[a]
  range_b=range_list[b]
  if range_a[0]<=range_b[0]<=range_a[1] or range_a[0]<=range_b[1]<=range_a[1]:
    union_parent(parent,array[i][0],array[i+1][0])
    start=min(range_a[0],range_b[0])
    end=max(range_a[1],range_b[1])
    range_list[a][0]=start
    range_list[a][1]=end
    range_list[b][0]=start
    range_list[b][1]=end

for i in range(1,n+1):
  find_parent(parent,i)

for i in range(q):
  a,b=map(int,input().split())
  if find_parent(parent,a)==find_parent(parent,b):
    print(1)
  else:
    print(0)