n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

dp=dict()

def checked(nx1,ny1,nx2,ny2):
    global board
    if nx2<0 or ny2<0 or nx2>=n or ny2>=n:
        return False
    if abs(nx1-nx2)==1 and abs(ny1-ny2)==1:
        if nx2-1<0 or nx2-1>=n or ny2-1<0 or ny2-1>=n:
            return False
        if board[nx2-1][ny2]==1 or board[nx2][ny2-1]==1:
            return False
    if board[nx2][ny2]==1:
        return False
    return True

def dfs(x1,y1,x2,y2):
    if x2==n-1 and y2==n-1:
        dp[(x1,y1,x2,y2)]=1
        return dp[(x1,y1,x2,y2)]
    if (x1,y1,x2,y2) in dp:
        return dp[(x1,y1,x2,y2)]
    dp[(x1,y1,x2,y2)]=0
    if abs(x1-x2)==1 and abs(y1-y2)==1:
        for dx1,dy1,dx2,dy2 in [(1,1,1,1),(1,1,1,0),(1,1,0,1)]:
            nx1,ny1,nx2,ny2=x1+dx1,y1+dy1,x2+dx2,y2+dy2
            if not checked(nx1,ny1,nx2,ny2):
                continue
            dp[(x1,y1,x2,y2)]+=dfs(nx1,ny1,nx2,ny2)
    elif abs(y1-y2)==1:
        for dx1,dy1,dx2,dy2 in [(0,1,0,1),(0,1,1,1)]:
            nx1,ny1,nx2,ny2=x1+dx1,y1+dy1,x2+dx2,y2+dy2
            if not checked(nx1,ny1,nx2,ny2):
                continue
            dp[(x1,y1,x2,y2)]+=dfs(nx1,ny1,nx2,ny2)
    elif abs(x1-x2)==1:
        for dx1,dy1,dx2,dy2 in [(1,0,1,0),(1,0,1,1)]:
            nx1,ny1,nx2,ny2=x1+dx1,y1+dy1,x2+dx2,y2+dy2
            if not checked(nx1,ny1,nx2,ny2):
                continue
            dp[(x1,y1,x2,y2)]+=dfs(nx1,ny1,nx2,ny2)
    return dp[(x1,y1,x2,y2)]

answer=0
answer=dfs(0,0,0,1)
print(answer)
