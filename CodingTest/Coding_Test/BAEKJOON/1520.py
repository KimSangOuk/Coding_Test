# 2회차 풀이



































# 풀이시간 초과/60분 시간제한 2초 메모리제한 128MB
# 1회차 오답
# DPS로 탐색해 들어가서 경로를 일일이 찾는거까지는 알고 있었기도 했고, 시간이 많이 걸리니 시간복잡도를 줄이기 위해 중간 기록을 해야한다 생각해서 다이나믹 프로그래밍까지 써야한다는 점도 이해했다. 이때, 다이나믹 프로그래밍에서는 현재 위치에서 현재까지의 답이 나와야된다고 생각했기 때문에 접근을 계속 파고 들어가면서로 했다. 즉, 다이나믹 프로그래밍에서의 잘못된 지식과 방법 접근때문에 풀지 못했다. 왜 현재까지의 답이 나와야된다고 생각했는가? 목적지와 도착지가 있기 때문에 한방향으로만 생각했다. 들어갔다 나오면서 답을 구한다는 생각은 하지 못한게, DFS에서도 나올때 보통 return을 시키면서 접근해본 경험도 없기 때문에 불가능하다고 생각을 박아두고 접근했다.
# 결국, DFS에서의 역접근이 경험부족으로 불가능하다는 생각에, DP또한 그렇게 접근할 생각을 하지 못한 점이 패착이다.

# m,n=map(int,input().split())

# board=[]
# count=0
# visited=[[0]*n for _ in range(m)]

# for i in range(m):
#   board.append(list(map(int,input().split())))

# def dfs(start,prev_h):
#   global count
#   x,y=start
#   if x<0 or y<0 or x>=m or y>=n:
#     return
#   if board[x][y]>=prev_h:
#     return
#   if x==m-1 and y==n-1:
#     count+=1
#     return
#   dfs((x+1,y),board[x][y])
#   dfs((x-1,y),board[x][y])
#   dfs((x,y+1),board[x][y])
#   dfs((x,y-1),board[x][y])

# dfs((0,0),int(1e9))
# print(count)

# 답안지
# import sys
# sys.setrecursionlimit(10 ** 8)
# input = sys.stdin.readline

# def dfs(sx, sy):
#     # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
#     if sx == m-1 and sy == n-1:
#         return 1

#     # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
#     if dp[sx][sy] != -1:
#         return dp[sx][sy]

#     ways = 0
#     for i in range(4):
#         nx, ny = sx + dx[i], sy + dy[i]
#         if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] > graph[nx][ny]:
#             ways += dfs(nx, ny)

#     dp[sx][sy] = ways
#     return dp[sx][sy]


# m, n = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(m)]
# dp = [[-1] * n for _ in range(m)]
# dx, dy = [1,-1,0,0], [0,0,1,-1]

# print(dfs(0,0))