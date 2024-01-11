# 풀이시간 15분 시간제한 1초 메모리제한 256MB
# 2회차 정답
# 탑승구의 수는 비행기가 들어올 수 있는 칸들이라고 생각하고 비행기의 수는 앞으로의 입력이라고 생각할 때, 우리는 뒤에서부터 채워간다고 생각할 수 있다. 그래서 만약 번호가 된다면 비행기를 하고 번호가 다르더라도 그 낮은 번호에는 비행기를 탑승구에 넣을 수 있다. 그러다가 다 찰경우에만 비행기를 넣을 수 없고 상황이 종료된다. 그렇기 때문에 우리는 비행기를 넣으며 그보다 낮은 칸으로 시선이 갈 수 있게 해놓아야한다. 이때, 포인터가 한칸 작은 칸씩 이동한다 했을 때, 모든 비행기가 찾을 경우에는 0번칸에 포인터가 가있을 수 있다고 볼 수 있다. 그렇다면 현재 들어오는 위치의 부모를, 즉 현재 다음에 들어오는 위치를 저장해 나가면서 하면 되는데 이 때, 우리는 0번째에 도착하면 끝난다는 것을 알 수 있다. 이러한 형태는 부모를 나타내느 방식으로 표현할 수 있고 그렇기에 현재 들어오는 비행기 번호의 부모의 부모가 어디를 가리키는 지를 보고 답을 결정할 수 있다.

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

g=int(input())
parent=[0]*(g+1)
for i in range(1,g+1):
  parent[i]=i

p=int(input())
count=0
for _ in range(p):
  now=int(input())
  tmp=find_parent(parent,now)
  if tmp==0:
    break
  else:
    union_parent(parent,tmp,tmp-1)
    count+=1

print(count)

# 풀이시간 초과 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이방식 접근하지 못함
# 간선과 정점의 개수가 100,000이라고 했을 때, 그래프 이론에서 나온 모든 알고리즘이 가능하다고 생각했다. 그렇지만 아무리 생각해봐도 위상 정렬은 될 수 없으며, 크루스칼 알고리즘도 아니라고 생각했다. 그렇기에 무조건 서로소 집합을 이용한 풀이여야 한다는 결론을 내렸다.
# 서로소 집합을 이용하는 경우는 그룹을 나누고 그 그룹이 연결되어 있는지, 아닌지를 보아야 된다고 생각했기 때문에, 계속 해서 간선에 집착하게 되었다. 그러나 그룹을 나누는 식의 그래프 형태는 나오지 않았고 답으로 이어지지도 않았다.
# 문제가 간선에 대해 주지 않는다면, 간선을 연결하는 경우를 내가 생각해야 된다고 생각할만 했지만, 정점끼리 연결하는데 너무 집착하는 나머지, 간선에 대한 정보가 없고, 원하는 그래프 형태가 나오지 않아도 다른 쪽으로 생각하지 못했다.
# 즉, 이 문제를 풀지못한 가장 큰 이유는 서로소 집합 문제가 그룹을 나누고 그 그룹으로 문제를 푸는 것이라는 좁은 생각을 가지고 있었기 때문이다.
# 그래프 형태가 문제를 풀기 적합하지 않고, 이러한 문제처럼 간선에 대한 정보가 없다면, 이미 모든 정보를 주고 다른 방식으로 간선을 연결하지 않나를 살펴봐야 한다. 서로소 집합 문제는 union-find 에 의존한다는 것을 말이다.

# 1회차 풀이

# 답안 예시
# 특정 원소가 속한 집합을 찾기
# def find_parent(parent,x):
#   # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#   if parent[x]!=x:
#     parent[x]=find_parent(parent,parent[x])
#   return parent[x]

# # 두 원소가 속한 집합을 합치기
# def union_parent(parent,a,b):
#   a=find_parent(parent,a)
#   b=find_parent(parent,b)
#   if a<b:
#     parent[b]=a
#   else:
#     parent[a]=b

# # 탑승구의 개수 입력받기
# g=int(input())
# # 비행기의 개수 입력받기
# p=int(input())

# # 부모 테이블 초기화
# parent=[0]*(g+1)

# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1,g+1):
#   parent[i]=i

# result=0
# for _ in range(p):
#   data=find_parent(parent,int(input())) # 현재 비행기의 탑승구의 루트 확인
#   if data==0: # 현재 루트가 0이라면, 종료
#     break
#   union_parent(parent,data,data-1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
#   result+=1

# print(result)