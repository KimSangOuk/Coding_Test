from collections import deque

m,n=map(int,input().split())

board=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n):
    for j in range(1,m):
        board[i][j]=-1

store=[]
k=int(input())
px,py=-1,-1
for i in range(k+1):
    dir,dist=map(int,input().split())
    x,y=-1,-1
    if dir==1:
        x=0
        y=dist
    if dir==2:
        x=n
        y=dist
    if dir==3:
        x=dist
        y=0
    if dir==4:
        x=dist
        y=m
    if i==k:
        px,py=x,y
        continue
    store.append((x,y))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(sx,sy,visited):
    q=deque()
    q.append((sx,sy))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n+1 or ny>=m+1:
                continue
            if board[nx][ny]==-1:
                continue
            if visited[nx][ny]!=0:
                continue
            if nx==sx and ny==sy:
                continue
            q.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1

visited=[[0]*(m+1) for _ in range(n+1)]
bfs(px,py,visited)
ans=0
for i,j in store:
    ans+=visited[i][j]

print(ans)
