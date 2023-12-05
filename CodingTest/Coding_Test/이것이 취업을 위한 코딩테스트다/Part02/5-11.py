# bfs로 푼것 까지 좋았으나 한번 더 리스트를 사용하지 않고 탐색의 형태가 아닌 나아가는 형태로 기록할 수 있다는 점을 배울 수 있어서 다시 풀기로 결정함.
# 즉, 풀이방식이 달라서 다시 품.
# 현재 칸과 전의 칸의 기록을 불러와 기록하는 방식으로 앞으로 나아가면 거리를 쉽게 구할 수 있다는 점을 배움.
# 현재 나아가는 한칸들을 묶어두지 않더라도 숫자로만 간단히 기록할 수 있다는 점을 배움.
# 그러나, 한 묶음으로 묶는 아이디어도 어딘가 쓸모 있는 구현 방식이라고 생각이 됨.
# 처음에 짠 알고리즘에서 이 기록 방식만 다른 점만 유의하면 답안지대로 구현할 수 있음.
from collections import deque

n,m=map(int,input().split())

board=[]
for _ in range(n):
  board.append(list(map(int,input())))

visited=[[False]*m for _ in range(n)]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(start,visited,board):
  start=(0,0)
  queue=deque([[start]])
  visited[0][0]=True
  count=1
  while queue:
    arr=list(queue.popleft())
    count+=1
    new_arr=[]
    for y,x in arr:
      for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if nx==m-1 and ny==n-1:
          return count
        if nx>=0 and nx<m and ny>=0 and ny<n and board[ny][nx]==1 and visited[ny][nx]==False:
          visited[ny][nx]=True
          new_arr.append((ny,nx))
    queue.append(new_arr)

print(bfs((0,0),visited,board))

# 답안 예시
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue=deque()
  queue.append((x,y))
  # 큐가 빌 때까지 반복
  while queue:
    x,y=queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny]==0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))