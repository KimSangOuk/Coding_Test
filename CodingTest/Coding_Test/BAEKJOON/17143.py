dx=[-1,1,0,0]
dy=[0,0,1,-1]

fisherYPos=0
r,c,m=map(int,input().split())
board=[[[] for _ in range(c+1)] for _ in range(r+1)]
for _ in range(m):
    x,y,s,d,z=map(int,input().split())
    board[x][y].append([x,y,s,d,z])

def fishing(board,fisherYPos):
    deep=0
    while deep<r:
        deep+=1
        if len(board[deep][fisherYPos])>0:
            score=board[deep][fisherYPos][0][4]
            board[deep][fisherYPos]=[]
            return score
    return 0

def sharkMoving(board):
    newBoard=[[[] for _ in range(c+1)] for _ in range(r+1)]
    for i in range(1,r+1):
        for j in range(1,c+1):
            if len(board[i][j])>0:
                x,y,s,d,z=board[i][j][0]
                d-=1

                if d < 2:  # 상하 이동
                    s %= (r - 1) * 2
                else:  # 좌우 이동
                    s %= (c - 1) * 2

                for _ in range(s):
                    if d == 0 and x == 1:  # 위쪽 벽 도달
                        d = 1  # 아래로 방향 전환
                    elif d == 1 and x == r:  # 아래쪽 벽 도달
                        d = 0  # 위로 방향 전환
                    elif d == 2 and y == c:  # 오른쪽 벽 도달
                        d = 3  # 왼쪽으로 방향 전환
                    elif d == 3 and y == 1:  # 왼쪽 벽 도달
                        d = 2  # 오른쪽으로 방향 전환

                    x += dx[d]
                    y += dy[d]
                if len(newBoard[x][y])>0:
                    if newBoard[x][y][0][4]<z:
                        newBoard[x][y][0]=[x,y,s,d+1,z]
                    else:
                        continue
                else:
                    newBoard[x][y].append([x,y,s,d+1,z])
    return newBoard
score=0
while fisherYPos<c:
    fisherYPos+=1
    score+=fishing(board,fisherYPos)
    board=sharkMoving(board)

print(score)