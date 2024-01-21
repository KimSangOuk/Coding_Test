# 3회차 풀이



















# 풀이시간 초과 시간제한 2초 메모리제한 192MB
# 2회차 오답 - 풀이시간 초과 및 풀이방법에 접근 못함
# 최단 거리를 찾기 위해서는 BFS로 거리를 따져가며 접근하며 데이터의 크기가 백만이기 때문에 O(N)인 BFS 입장에서는 한번밖에 사용하지 못한다는 점을 인지하고 있었다. 그렇다면 BFS 함수를 만져 그 안에서 해결을 봐야하는데, 조건들을 건드리거나 데이터를 추가적으로 기록해서 하는 방법이 있다고 염두해 두고 시작했다. 처음에 접근은 0인 순간으로 접근하고 나서 1을 사용할 때로 덮어씌우려고 했으나 중간에 갈아타는 부분이 불가능하다는 것을 알고 방법을 바꾸었다. 두번째 접근으로는 visited를 나눠서 답안지와 같이 접근하는데 성공했으나 이 방법 또한 갈아타는 부분에서 문제가 발생했다. 벽을 사용한 지점 부터는 벽을 사용할 수 없는데 이 것은 기록이 가능했으나, 그렇게 된다면 벽을 사용한 visited에서는 다른 지점까지의 거리는 새롭게 기록되기 때문에 그 전까지의 지점들의 최단거리가 틀린다고 생각해서 그렇게 진행하지 못했다. 하지만 결과적으로 목적지에 빠르게 도착하는 거리값만 구하면 되기 때문에 중간에 갈아타는 부분도 상관없다는 것을 알았다. 결국 내가 틀린 이유는 두 visited에서 정답과 같은 거리가 나와야된다고 생각했기 때문이다. 그리고 별개로 진행되어야 된다고 생각했기 때문에 답에 접근하지 못했다. 왜 별개로 진행되어야 된다고 생각했는가? 벽을 부수는 루틴과 안부수는 루틴이 서로 안겹치게 접근되어 답을 구한다고 생각했다. 중간에 상태가 달라지는 것을 처음 경험해보기도 했고, visited는 하나의 답을 구할 때까지 연속되어야된다고 생각했지 다른 visited로 넘어가는 경우는 생각해보지 못했다. 그렇게 두개의 상태를 표현할것이라고 접근을 못했다. 즉, 결론은 visited를 구할때, 하나의 상태를 구한다고 생각했지 다른 상태로 전환하거나 할때 바뀐다고는 생각하지 못한 고정관념이었다. 유연하게 차원을 하나 더 두거나 해서 다른 visited에 넘어갈 수도 있다고 생각해야 한다. 또한, 최단거리에서는 도달하는 즉시, 그 최단거리만을 답으로 정하기 때문에, 특정 상태에 맞지 않은 상태에서의 최단거리는 무시해도 된다는 사실을 배웠다. 즉, 0과 1인 상태가 있을 때, 0인 상태에서 먼저 특정 지점에 도달한다면 1에서 도달한 것은 후에 오기 때문에 답을 취급안할 수 있다는 말이다.
# 짧게 정리하면 첫번째, visited는 반드시 진행이 독자적으로 진행될 필요 없이 상태가 바뀐다면 개입하거나 다른 상태를 기록하는 visited로 나아갈 수 있다. 두번째는 BFS에서 최단거리를 구할 때는 상태가 다르더라도 특정 지점에 먼저 도착한 것만을 답으로 삼을 수 있다는 것을 인지하고 있어야 겠다.

# import heapq
from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

board=[]
for _ in range(n):
  board.append(list(map(int,input())))

visited=[[-1]*m for _ in range(n)]
visited2=[[-1]*m for _ in range(n)]
dist=[[0]*m for _ in range(n)]

def bfs(pos):
  q=deque([])
  q.append(wall,pos)
  dist[pos[0]][pos[1]]=1
  visited[pos[0]][pos[1]]=0
  while q:
    wall,pos=q.popleft()
    x,y=pos
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if visited[nx][ny]==-1 and board[nx][ny]==0:
        visited[nx][ny]=0
        q.append((wall,pos))
      if visited2[nx][ny]==-1 and board[nx][ny]==1:
        visited2[nx][ny]=1
        
      # if visited[nx][ny]!=-1:
      #   continue
      # if board[nx][ny]==1:
      #   continue
      # visited[nx][ny]=0
      # dist[nx][ny]=dist[x][y]+1
      # q.append((nx,ny))

start=(0,0)
bfs(start)
# bfs2(start)

# for i in range(n):
#   print(dist[i])

if dist[n-1][m-1]==0:
  print(-1)
else:
  print(dist[n-1][m-1])


# 풀이시간 3시간 경과
# 1회차 오답 - 풀이에 접근 못함, 실패
# ...

# from collections import deque

# dx=[0,0,1,-1]
# dy=[1,-1,0,0]

# n,m=map(int,input().split())

# board=[[] for _ in range(n)]
# for i in range(n):
#   arr=list(input())
#   for j in range(m):
#     board[i].append(int(arr[j]))

# visited=[[0]*m for _ in range(n)]
# wall_break=[[0]*m for _ in range(n)]

# def bfs(board,start,visited):
#   q=deque([])
#   y,x=start
#   q.append((y,x))
#   visited[y][x]=1
#   while q:
#     y,x=q.popleft()
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       if nx<0 or nx>=m or ny<0 or ny>=n:
#         continue
#       if visited[ny][nx]>0:
#         if wall_break[y][x]==0:
#           wall_break[ny][nx]=0
#         continue
#       if board[ny][nx]==0:
#         wall_break[ny][nx]=wall_break[y][x]
#       else:
#         if wall_break[y][x]==1:
#           continue
#         else:
#           wall_break[ny][nx]=1
#       q.append((ny,nx))
#       visited[ny][nx]=visited[y][x]+1

# start=(0,0)
# bfs(board,start,visited)

# for i in range(n):
#   print(visited[i])

# if visited[n-1][m-1]==0:
#   print(-1)
# else:
#   print(visited[n-1][m-1])

# 답안지
from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))