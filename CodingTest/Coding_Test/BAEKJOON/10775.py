# 풀이시간 15분 시간제한 1초 메모리제한 256MB
# 1회차 정답
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