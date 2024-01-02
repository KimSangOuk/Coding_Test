# 2회차 풀이





# 풀이시간 90분/50분 시간제한 1초 메모리제한 256MB
# 1회차 오답 - 풀이시간 초과
# 1. 처음에는 큐를 바이러스 종류별로 두어서 받은 다음 시간초마다 반복문으로 또 따로 돌려서 구하려고 했으나 시간초과가 나와서 다른 방법으로 바꾸었다.
# 2. 두 번째 접근법은 전체 1초에 퍼지는 종류와 좌표를 전부 담아 퍼지는것을 확인한 후 그 퍼진것들을 또 큐에 한 세트로 담아 푸는 지금의 방법이다.
# 문제는 방법은 금방 생각해내놓고 바꾸는 식으로 시간내에 해결하였으나 오류가 나는 것을 잡아내지 못하였다. 최초에 바이러스를 담을 때, 낮은 바이러스 순으로 정렬을 하고 넣었어야 했는데 이 점에서 문제가 발생하였다. 아이디어, 즉 알고리즘의 형태를 바꿀 때, 다른 곳에서 어떤 영향을 바뀐 부분이 받고 있고 어떻게다른부분은 바뀌어야 되는지 생각했어야 했는데 간과했다.

# 1회차 풀이
# 풀이를 바꾸려면 처음부터 바꿔야한다는 사실을 깨닫게 되었다.
# 그리고 bfs 방식에서 시간이나 거리를 특정 장소에 저장하는 것이 아닌 큐 원소 좌표 자체에 저장할 수 있다는 점을 배웠다. 요긴하게 쓰일 것 같다.
from collections import deque
import sys

n,k=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

queue=deque()
new_arr=[]

for i in range(n):
  for j in range(n):
    if graph[i][j]!=0:
      new_arr.append((graph[i][j],i,j))

new_arr.sort()
queue.append(new_arr)

s,x_a,y_a=map(int,sys.stdin.readline().split())

dx=[0,-1,0,1]
dy=[-1,0,1,0]

for ms in range(s):
  arr=queue.popleft()
  new_arr=[]
  for d,x,y in arr:
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:
        graph[nx][ny]=d
        new_arr.append((d,nx,ny))
  new_arr.sort()
  queue.append(new_arr)

print(graph[x_a-1][y_a-1])

# 답안 예시
from collections import deque

n,k=map(int,input().split())

graph=[] # 전체 보드 정보를 담는 리스트
data=[] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int,input().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j]!=0:
      # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
      data.append((graph[i][j],0,i,j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q=deque(data)

target_s,target_x,target_y=map(int,input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx=[0,-1,0,1]
dy=[-1,0,1,0]

# 너비 우선 탐색(BFS) 진행
while q:
  virus,s,x,y=q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if s==target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    # 해당 위치로 이동할 수 있는 경우, 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
    if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:
      graph[nx][ny]=virus
      q.append(virus,s+1,nx,ny)

print(graph[target_x-1][target_y-1])