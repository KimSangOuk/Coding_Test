import sys
sys.setrecursionlimit(10**5)

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

dp=[[-1]*m for _ in range(n)]

def dfs(x,y):
    if (x,y)==(n-1,m-1):
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if board[nx][ny]>=board[x][y]:
            continue
        dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))