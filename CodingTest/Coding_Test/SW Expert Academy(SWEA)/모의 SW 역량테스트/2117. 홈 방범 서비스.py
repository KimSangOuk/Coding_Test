from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

for tc in range(1,int(input())+1):
    answer=0
    N,M=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            q=deque()
            q.append((i,j,0))
            visited=[[-1]*N for _ in range(N)]
            visited[i][j]=0
            houseCnt=board[i][j]
            nowDist=0
            answer=max(answer,houseCnt)
            while q:
                x,y,dist=q.popleft()
                if dist>nowDist:
                    k=dist+1
                    # if i==3 and j==3:
                    #     print(houseCnt,k*k+(k-1)*(k-1))
                    if houseCnt*M-(k*k+(k-1)*(k-1))>=0:
                        answer=max(houseCnt,answer)
                    nowDist+=1
                for t in range(4):
                    nx=x+dx[t]
                    ny=y+dy[t]
                    if nx<0 or ny<0 or nx>=N or ny>=N:
                        continue
                    if visited[nx][ny]!=-1:
                        continue
                    q.append((nx,ny,dist+1))
                    visited[nx][ny]=visited[x][y]+1
                    houseCnt+=board[nx][ny]
    print("#"+str(tc)+" "+str(answer))