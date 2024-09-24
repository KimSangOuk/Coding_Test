from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

n,m=map(int,input().split())
originBoard=[list(map(int,input().split())) for _ in range(n)]

board=[[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        board[i][j]=originBoard[i-1][j-1]

outAir=set()

def outAirbfs(x,y):
    q=deque()
    q.append((x,y))
    visited=[[False]*(m+2) for _ in range(n+2)]
    visited[x][y]=True
    outAir=set()
    outAir.add((x,y))
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n+2 or ny>=m+2:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny]==1:
                continue
            outAir.add((nx,ny))
            visited[nx][ny]=True
            q.append((nx,ny))
    return outAir

def cheeseBfs(visited,x,y):
    q=deque([(x,y)])
    visited[x][y]=True
    cheese=set()
    cheese.add((x,y))
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n+2 or ny>=m+2:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny]==0:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
            cheese.add((nx,ny))
    return cheese      

t=0
while True:
    outAirSet=outAirbfs(0,0)
    if len(outAirSet)==(n+2)*(m+2):
        break

    visited=[[False]*(m+2) for _ in range(n+2)]
    cheese=set()
    for i in range(n+2):
        for j in range(m+2):
            if not visited[i][j] and board[i][j]==1:
                cheese|=cheeseBfs(visited,i,j)

    for piece in cheese:
        x,y=piece
        cnt=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx,ny) in outAirSet:
                cnt+=1
        if cnt>=2:
            board[x][y]=0
    t+=1

print(t)