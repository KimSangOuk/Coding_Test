    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    def simulation(sx,sy,sd):
        global answer
        started=False
        x,y,d=sx,sy,sd
        cnt=0
        while True:
            if started and x==sx and y==sy:
                break
            if board[x][y]==-1:
                break
            if not started:
                started=True
            if 1<=board[x][y]<=4:
                if board[x][y]==1:
                    if d==3:
                        d=0
                    elif d==2:
                        d=1
                elif board[x][y]==2:
                    if d==0:
                        d=1
                    elif d==3:
                        d=2
                elif board[x][y]==3:
                    if d==1:
                        d=2
                    elif d==0:
                        d=3
                elif board[x][y]==4:
                    if d==2:
                        d=3
                    elif d==1:
                        d=0
                cnt+=1
            nx=x+dx[d]
            ny=y+dy[d]
            if (nx<0 or ny<0 or nx>=n or ny>=n) or (board[nx][ny]==5) or (board[nx][ny]==1 and (d==1 or d==0)) or (board[nx][ny]==2 and (d==1 or d==2)) or (board[nx][ny]==3 and (d==2 or d==3)) or (board[nx][ny]==4 and (d==3 or d==0)):
                cnt+=1
                d=(d+2)%4
                nx,ny=x,y

            x,y=nx,ny
            if 6<=board[x][y]<=10:
                for k in range(2):
                    if (x,y)!=hole[board[x][y]][k]:
                        x,y=hole[board[x][y]][k]
                        break
            # print(x,y)
        answer=max(answer,cnt)

    for tc in range(1,int(input())+1):
        n=int(input())
        hole=dict()
        answer=0
        board=[list(map(int,input().split())) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if 6<=board[i][j]<=10:
                    if board[i][j] not in hole:
                        hole[board[i][j]]=[]
                    hole[board[i][j]].append((i,j))
        answer=0
        for x in range(n):
            for y in range(n):
                if board[x][y]==0:
                    for d in range(4):
                        simulation(x,y,d)
        print("#"+str(tc)+" "+str(answer))