N,M,R=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]
forRestore=[row[:] for row in board]

dx={'E':0,'W':0,'S':1,'N':-1}
dy={'E':1,'W':-1,'S':0,'N':0}

def isIn(x,y):
    if x<0 or y<0 or x>=N or y>=M:
        return False
    return True

answer=0
for r in range(R):
    attackX,attackY,attackD=map(str,input().split())
    defenX,defenY=map(int,input().split())
    attackX,attackY=int(attackX)-1,int(attackY)-1
    defenX,defenY=defenX-1,defenY-1

    fallH=board[attackX][attackY]
    while isIn(attackX,attackY) and fallH>0:
        if board[attackX][attackY]!=0:
            fallH=max(board[attackX][attackY]-1,fallH-1)
            board[attackX][attackY]=0
            answer+=1
        else:
            fallH-=1
        attackX+=dx[attackD]
        attackY+=dy[attackD]

    board[defenX][defenY]=forRestore[defenX][defenY]
print(answer)
for i in range(N):
    for j in range(M):
        if board[i][j]>0:
            print('S',end=' ')
        else:
            print('F',end=' ')
    print()