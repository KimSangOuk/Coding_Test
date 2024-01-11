# 풀이시간 2시간/50분 시간제한 1초 메모리제한 256MB
# 1회차 정답 - But, 풀이시간이 너무 오래 걸려서 재풀이
# 먼저 갯수를 처리하는데 시간이 너무 오래 걸렸다. 알고리즘 적으로 count를 세는 데 O(N)이 쓰이면 안되는 것을 알고 이것을 union_parent에 적용해야 겠다. 이 판단을 하는데 너무 오래걸렸다. 그리고 count를 union 함수로 처리하고 나서 또 오답 판정을 받아서 이유를 찾는데 한시간이 걸렸는데, 친구가 새로 생기는 경우가 아니더라도 관계와 네트워크는 다른 별개의 것이었다. 즉, 집합에 속하는 것과 간선의 차이였는데, 표현이 그렇다보니 이 부분을 캐치하지 못했다.
# 먼저 두번째 문제점 같은 경우, 간선과 집합의 표현이 서로 관계를 표현하는 표현이다보니 헷갈릴 수 있으니 정확히 구분해서 문제에 접근하면 될 것 같다.
# 첫번째로 시간이 오래 걸린 문제는, count 해결 관련인데, 지금까지는 union-find 함수를 건드리는 문제가 없었기에 내가 건드리는데 거부감이 생겨서 오래걸린 것도 있다. 이 문제는 이번에 맞닿드려서 해결했으니 괜찮다.

# 1회차 풀이
import sys

input=sys.stdin.readline

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(count,parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
    count[a]+=count[b]
    count[b]=0
  elif a>b:
    parent[a]=b
    count[b]+=count[a]
    count[a]=0
  # if a!=b:
  #   parent[b]=a
  #   count[a]+=count[b]
  #   count[b]=0

for tc in range(int(input())):
  f=int(input())
  parent=dict()
  count=dict()
  for _ in range(f):
    a,b=map(str,input().split())
    if a not in parent:
      parent[a]=a
      count[a]=1
    if b not in parent:
      parent[b]=b
      count[b]=1
      
    union_parent(count,parent,a,b)
    print(count[find_parent(parent,a)])