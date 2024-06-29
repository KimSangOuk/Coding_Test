import copy
from collections import deque

for tc in range(int(input())):
    n=int(input())
    board=[]
    dx=[0,0,-1,1,-1,-1,1,1]
    dy=[-1,1,0,0,-1,1,-1,1]
    for i in range(n):
        board.append(list(input()))

    bomb_checker=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]=='*':
                bomb_checker[i][j]=-1
                continue
            cnt=0
            for k in range(8):
                nx=i+dx[k]
                ny=j+dy[k]
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                if board[nx][ny]=='*':
                    cnt+=1
            bomb_checker[i][j]=cnt
    answer=0
    visited=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bomb_checker[i][j]==0 and not visited[i][j]:
                q=deque([])
                q.append((i,j))
                visited[i][j]=True
                answer+=1
                while q:
                    x,y=q.popleft()
                    if bomb_checker[x][y]>0:
                        continue
                    for k in range(8):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            continue
                        if visited[nx][ny]:
                            continue
                        if bomb_checker[nx][ny]==-1:
                            continue
                        if k>=4:
                            if not visited[x][ny] or not visited[nx][y]:
                                continue
                        visited[nx][ny]=True
                        q.append((nx,ny))
    for i in range(n):
        for j in range(n):
            if bomb_checker[i][j]>0 and not visited[i][j]:
                answer+=1

    print("#"+str(tc+1)+" "+str(answer))

