# bfs로 풀었으나 dfs로 예제 풀이가 나와서 공부할 겸 다시 풀어보기 DFS로
# 풀이시간이 bfs가 더 빠르다는 이야기를 듣기도 했고 더 이해하기 쉬워서 bfs로 접근함
# 총 가로, 세로가 길어야 1,000이였기 때문에 모든 칸의 경우의 수를 구해도 1,000,000이라 O(N)인 BFS나 DFS를 둘 다 사용가능하다고 판단함
# 2차원 배열에서 탐색할 때, 넣고 빼고를 해야한다 생각해서 BFS로 접근한 부분이 큼.
# 2차원 배열 자체가 2차원 리스트 형식이 되어서 DFS 탐색이 가능하다는 아이디어를 배움.
# 2차원 배열에서 탐색할 때, 단순 방문과 반복, 즉 재귀형태(스택 형태)가 유지된다는 점을 배움.

from collections import deque

n,m=map(int,input().split())
board=[]
for i in range(n):
  arr=input()
  board.append([])
  for j in range(m):
    board[i].append(int(arr[j]))
    # print(arr[j])

visited=[[False]*m for _ in range(n)]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

count=0

for i in range(n):
  for j in range(m):
    if board[i][j]==0 and visited[i][j]==False:
      count+=1
      visited[i][j]=True
      queue=deque([(i,j)])
      while queue:
        y,x=queue.popleft()
        for k in range(4):
          nx=x+dx[k]
          ny=y+dy[k]
          if ny>=0 and ny<n and nx>=0 and nx<m and board[ny][nx]==0 and visited[ny][nx]==False:
            visited[ny][nx]=True
            queue.append((ny,nx))

for i in range(n):
  print(board[i])
print()
for i in range(n):
  for j in range(m):
    print(int(visited[i][j]),end=" ")
  print()
print(count)

# 답안지 예시
# N, M을 공백으로 구분하여 입력받기
n,m=map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모드 노드들도 방문
def dfs(x,y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<=-1 or x>=n or y<=1 or y>=m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y]==0:
    # 해당 노드 방문 처리
    graph[x][y]=1
    # 상, 하, 좌, 우의 위치도 모두 재귀적 호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
  for j in range(m):
    # 현재 위체에서 DFS 수행
    if dfs(i,j)==True:
      result+=1

print(result) # 정답 출력