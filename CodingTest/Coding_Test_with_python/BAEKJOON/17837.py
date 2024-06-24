# 풀이시간 1시간 45분/1시간 시간제한 0.5초 메모리제한 512MB
# 1회차 정답 - 풀이시간 초과
# 각 체스말을 번호순으로 단계에 따라 이동시키는 문제이다. 우선 보드의 색으로 이동할 시 영향을 받기 때문에 따로 저장해두고 chess의 위치와 상태는 별개로 또 쌓인 것을 알아야하기 때문에 각 칸에 체스가 쌓여있는 것을 표현하기 위해 3차원 배열로 두었다. 그리고 각 체스말을 순서대로 진행시켰고 이동 방향의 색에 따라 구분하면서 또 범위를 벗어나는 경우는 파란색의 이동경우와 마찬가지로 취급하여 처리하였다. 색깔별로 진행하는 함수를 따로 두었는데, 흰색과 빨간색 같은 경우는 색에 따라 체스의 이동상태는 체스가 쌓여있는대로 좌표만 이동시키고 쌓여있는대로 그대로 다음칸에 옮겨두었다. 빨간색은 순서를 역순으로 넣었다. 또 파란색의 경우는 방향을 바꾸고 또 파란색이나 장외라면 방향만 수정하고 아니라면 재귀를 써서 이동시키는 식으로 두었다.
# 시간이 오래 걸린 이유는 다음과 같다. 첫번째로 지식의 문제이다. 빈 공간으로 배열을 2차원 이상으로 두기 위해서는 곱하기가 아니라 3차원 배열 식으로 두어야 각 2차원 배열에 배열을 하나씩 둘 수 있다.
# 두번째는 슬라이싱의 지식 문제이다. 슬라이싱을 할때, 두번째가 -1이 오면 안된다는 점을 처음 알았다. for문과 마찬가지로 마지막 좌표 전에 꺾으면 되는줄 알았는데 그게 아니었다. 한번 시작 좌표로 끊은 다음 [::-1]로 한번 더 뒤집어 주는 방법이 있다는 것을 배웠다.
# 세번째 이유는 턴이 진행되는 중에 4개 이상이 쌓이면 종료된다는 점을 간과했다는 것이다. 모든 턴이 마치고 나서 4개 이상일 때를 찾았는데 그렇기 보다는 턴이 진행중일 때, 즉, 하나의 이동이 끝나는 순간 최대 높이를 확인했어야 했다. 이 점을 찾는데 시간이 오래걸렸다. 즉, 다음에는 턴을 마치고서 인지 아니면 중간에 확인하는 것인지 문제를 읽을 때 염두해 두면서 읽어야겠다.

n,k=map(int,input().split())

dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]

board_color=[]
for _ in range(n):
    board_color.append(list(map(int,input().split())))

board_chess=[[[] for _ in range(n)] for _ in range(n)]

chess=dict()
for i in range(1,k+1):
    x,y,d=map(int,input().split())
    board_chess[x-1][y-1].append(i)
    chess[i]=[x-1,y-1,d]

def go(board_chess,num,x,y,d,color):
    if color==0:
        for k in board_chess[x][y][board_chess[x][y].index(num):]:
            chess[k][0]=x+dx[d]
            chess[k][1]=y+dy[d]
        board_chess[x+dx[d]][y+dy[d]]+=board_chess[x][y][board_chess[x][y].index(num):]
        board_chess[x][y]=board_chess[x][y][:board_chess[x][y].index(num)]
    elif color==1:
        for k in board_chess[x][y][board_chess[x][y].index(num):]:
            chess[k][0]=x+dx[d]
            chess[k][1]=y+dy[d]
        board_chess[x+dx[d]][y+dy[d]]+=board_chess[x][y][board_chess[x][y].index(num):][::-1]
        board_chess[x][y]=board_chess[x][y][:board_chess[x][y].index(num)]
    elif color==2:
        if d==2:
            d=1
        elif d==1:
            d=2
        elif d==3:
            d=4
        elif d==4:
            d=3
        nx=x+dx[d]
        ny=y+dy[d]
        if nx<0 or ny<0 or nx>=n or ny>=n or board_color[nx][ny]==2:
            chess[num][2]=d
        else:
            chess[num][2]=d
            go(board_chess,i,x,y,d,board_color[nx][ny])


max_count=1
turn=0
while max_count<4 and turn<=1000:
    turn+=1
    for i in range(1,k+1):
        x,y,d=chess[i]
        nx=x+dx[d]
        ny=y+dy[d]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            go(board_chess,i,x,y,d,2)
        else:
            go(board_chess,i,x,y,d,board_color[nx][ny])
        for i in range(n):
            for j in range(n):
                max_count=max(max_count,len(board_chess[i][j]))
if turn>=1000:
    print(-1)
else:
    print(turn)