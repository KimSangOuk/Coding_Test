from collections import deque

def canConnect(x1,y1,x2,y2):
    type1=board[x1][y1]
    type2=board[x2][y2]
    if type1==1:
        if x1<x2:
            if type2==1 or type2==2 or type2==4 or type2==7:
                return True
        if x1>x2:
            if type2==1 or type2==2 or type2==5 or type2==6:
                return True
        if y1>y2:
            if type2==1 or type2==3 or type2==4 or type2==5:
                return True
        if y2>y1:
            if type2==1 or type2==3 or type2==6 or type2==7:
                return True
    if type1==2:
        if x1<x2:
            if type2==1 or type2==2 or type2==4 or type2==7:
                return True
        if x2<x1:
            if type2==1 or type2==2 or type2==5 or type2==6:
                return True
    if type1==3:
        if y1>y2:
            if type2==1 or type2==3 or type2==4 or type2==5:
                return True
        if y2>y1:
            if type2==1 or type2==3 or type2==6 or type2==7:
                return True
    if type1==4:
        if x1>x2:
            if type2==1 or type2==2 or type2==5 or type2==6:
                return True
        if y2>y1:
            if type2==1 or type2==3 or type2==6 or type2==7:
                return True
    if type1==5:
        if x1<x2:
            if type2==1 or type2==2 or type2==4 or type2==7:
                return True
        if y2>y1:
            if type2==1 or type2==3 or type2==6 or type2==7:
                return True
    if type1==6:
        if x1<x2:
            if type2==1 or type2==2 or type2==4 or type2==7:
                return True
        if y1>y2:
            if type2==1 or type2==3 or type2==4 or type2==5:
                return True
    if type1==7:
        if x1>x2:
            if type2==1 or type2==2 or type2==5 or type2==6:
                return True
        if y1>y2:
            if type2==1 or type2==3 or type2==4 or type2==5:
                return True
    return False

for tc in range(1,int(input())+1):
    N,M,R,C,L=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(N)]
    visited=[[-1]*M for _ in range(N)]

    q=deque()
    visited[R][C]=0
    q.append((R,C))
    while q:
        x,y=q.popleft()
        if board[x][y]==1:
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
        elif board[x][y]==2:
            for dx,dy in [(-1,0),(1,0)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
        elif board[x][y]==3:
            for dx,dy in [(0,-1),(0,1)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
        elif board[x][y]==4:
            for dx,dy in [(-1,0),(0,1)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
        elif board[x][y]==5:
            for dx,dy in [(1,0),(0,1)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
        elif board[x][y]==6:
            for dx,dy in [(1,0),(0,-1)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
        elif board[x][y]==7:
            for dx,dy in [(-1,0),(0,-1)]:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if not (1<=board[nx][ny]<=7):
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if not canConnect(x,y,nx,ny):
                    continue
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    answer=0
    for i in range(N):
        for j in range(M):
            if visited[i][j]!=-1 and visited[i][j]<L:
                answer+=1
    print("#"+str(tc)+" "+str(answer))