# 풀이시간 40분/40분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 시간복잡도를 고려했을 때, 데이터의 총량이 2,500이고 인구 이동 횟수가 2,000 이하 이므로 O(N)인 BFS/DFS 탐색을 썼을 때, 주위에 한번 정도 반복문을 씌울 수 있다. 이러한 점에서 인구이동 횟수를 미정인 무한 반복문으로 두고 풀 수 있다는 점을 알 수 있다.
# 또한 조건에 따른 2차원 배열에서의 확장, 즉 탐색을 문제를 읽었을 때 확인할 수 있다.

from collections import deque

n,l,r=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

dy=[0,0,-1,1]
dx=[-1,1,0,0]

def bfs(graph,start,visited):
  q=deque([start])
  unity=[]
  unity.append(start)
  visited[start[0]][start[1]]=True
  while q:
    y,x=q.popleft()
    for i in range(4):
      ny=y+dy[i]
      nx=x+dx[i]
      if ny>=0 and ny<n and nx>=0 and nx<n and abs(graph[ny][nx]-graph[y][x])>=l and abs(graph[ny][nx]-graph[y][x])<=r and (ny,nx) not in unity and visited[ny][nx]==False:
        q.append((ny,nx))
        unity.append((ny,nx))
        visited[ny][nx]=True
  return unity

def same(prev,graph):
  for i in range(n):
    for j in range(n):
      if prev[i][j]!=graph[i][j]:
        return False
  return True

count=0
prev=[[0]*n for _ in range(n)]
while True:
  for i in range(n):
    for j in range(n):
      prev[i][j]=graph[i][j]

  visited=[[False]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if visited[i][j]==False:
        unity=bfs(graph,(i,j),visited)
        # print(unity)
        sum_people=0
        box_people=0
        for y,x in unity:
          sum_people+=graph[y][x]
        box_people=int(sum_people/len(unity))
        for y,x in unity:
          graph[y][x]=box_people

  count+=1
  # print(count)

  if same(prev,graph):
    count-=1
    break


print(count)

# # 답안 예시
# from collections import deque

# # 땅의 크기(N), L, R값을 입력받기
# n, l, r = map(int,input().split())

# # 전체 나라의 정보(N X N)를 입력받기
# graph=[]
# for _ in range(n):
#   graph.append(list(map(int,input().split())))

# dx=[-1,0,1,0]
# dy=[0,-1,0,1]

# result=0

# # 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
# def process(x,y,index):
#   # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
#   united=[]
#   united.append((x,y))
#   # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
#   q=deque()
#   q.append((x,y))
#   union[x][y]=index # 현재 연합의 번호 할당
#   summary = graph[x][y] # 현재 연합의 전체 인구의 수
#   count=1 # 현재 연합의 국가의 수
#   # 큐가 빌 때까지 반복(BFS)
#   while q:
#     x,y=q.popleft()
#     # 현재 위치에서 4가지 방향을 확인하여
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       # 바로 옆에 있는 나라를 확인하여
#       if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
#         # 옆에 있는 나라와 인구 차이가 L명 이상 R명 이하라면
#         if l<=abs(graph[nx][ny]-graph[x][y])<=r:
#           q.append((nx,ny))
#           # 연합에 추가
#           union[nx][ny]=index
#           summary+=graph[nx][ny]
#           count+=1
#           united.append((nx,ny))
#   # 연합 국가끼리 인구를 분배
#   for i,j in united:
#     graph[i][j]=summary//count
#     return count

# total_count=0

# # 더 이상 인구 이동을 할 수 없을 때까지 반복
# while True:
#   union=[[-1]*n for _ in range(n)]
#   index=0
#   for i in range(n):
#     for j in range(n):
#       if union[i][j]==-1: # 해당 나라가 아직 처리되지 않았다면
#         process(i,j,index)
#         index+=1
#   # 모든 인구 이동이 끝난 경우
#   if index==n*n:
#     break
#   total_count+=1

# # 인구 이동 횟수 출력
# print(total_count)