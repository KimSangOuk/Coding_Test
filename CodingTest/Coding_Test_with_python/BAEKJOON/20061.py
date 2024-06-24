# 풀이시간 1시간 20분/1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답 - 풀이시간 초과
# 굉장히 복잡했던 구현 및 시뮬레이션 문제이다. 우선 각 블록을 빨간색에서 생성한다고 생각하고 각 블록에 끝에 닿을 때까지 파란색과 녹색 영역으로 이동시켜야 한다. 이 때는 단순히 while문을 진행하며 방향으로 이동시키되, 벽에 닿거나 다른 블록에 닿을 때까지 이동시키면 된다. 이제 점수를 구하는 부분인데, 모든 영역을 검사하면서 4개가 꽉차면 점수를 얻고 그 4개를 얻은 부분을 0으로 만들어주면 된다. 점수를 구하고 나서 한번 차있는 블록들을 없어진 공간을 메우듯 내려주어야한다. 이떄는, 새로운 배열을 만들어서 바닥에서부터 없는 줄을 제외하고 새롭게 채워넣은 다음 그 새로운 배열을 원래의 보드에 세팅하는 식으로 풀었다. 마지막으로 0,1에 나와있는 줄을 검사하고 만약 있다면 끝부분에서 있는 수만큼 줄을 제거해준다. 내리는 작업은 반복 되기 때문에 한번 더 함수를 사용하였다.
# 내가 보기에는 코드가 너무 길다고 생각이 들고 이를 줄이기 위해서는 중복되는 작업을 없애주어야 한다. 그렇기 위해서는 생성시에 범위를 축소하여 블록을 0,1공간에 생성시키는 방법과 초록과 파랑을 통일해서 블록을 넣을 때 대칭시켜주는 방법이 있다. 그러면 x,y좌표의 움직임이 통일 되기 때문에 파랑과 초록을 구분할 필요없이 한 큐에 처리할 수 있다. 

board=[[0]*10 for _ in range(10)]

def gb_stack(board,t,x,y,color):
    if t==1:
        block=[[x,y],[x,y]]
    elif t==2:
        block=[[x,y],[x,y+1]]
    elif t==3:
        block=[[x,y],[x+1,y]]
    while True:
        if color=='b':
            n1_x_block,n1_y_block,n2_x_block,n2_y_block=block[0][0],block[0][1]+1,block[1][0],block[1][1]+1
        else:
            n1_x_block,n1_y_block,n2_x_block,n2_y_block=block[0][0]+1,block[0][1],block[1][0]+1,block[1][1]
        if color=='b' and (n1_y_block>=10 or n2_y_block>=10):
            break
        elif color=='g' and (n1_x_block>=10 or n2_x_block>=10):
            break
        if board[n1_x_block][n1_y_block]==1 or board[n2_x_block][n2_y_block]==1:
            break
        block[0][0],block[0][1],block[1][0],block[1][1]=n1_x_block,n1_y_block,n2_x_block,n2_y_block
    board[block[0][0]][block[0][1]],board[block[1][0]][block[1][1]]=1,1

def down_block(board,start_x,end_x,start_y,end_y,color):
    if color=='b':
        new_mini_board=[[0]*6 for _ in range(4)]
        now_pos=5
        for j in range(end_y,start_y-1,-1):
            count=0
            for i in range(start_x,end_x+1):
                if board[i][j]==0:
                    count+=1
            if count!=4:
                for i in range(start_x,end_x+1):
                    new_mini_board[i][now_pos]=board[i][j]
                now_pos-=1
        for i in range(start_x,end_x+1):
            for j in range(start_y,end_y+1):
                board[i][j]=new_mini_board[i-start_x][j-start_y]
    else:
        new_mini_board=[[0]*4 for _ in range(6)]
        now_pos=5
        for i in range(end_x,start_x-1,-1):
            count=0
            for j in range(start_y,end_y+1):
                if board[i][j]==0:
                    count+=1
            if count!=4:
                for j in range(start_y,end_y+1):
                    new_mini_board[now_pos][j]=board[i][j]
                now_pos-=1
        for i in range(start_x,end_x+1):
            for j in range(start_y,end_y+1):
                board[i][j]=new_mini_board[i-start_x][j-start_y]

def get_score(board,start_x,end_x,start_y,end_y,color):
    this_round_score=0
    if color=='b':
        for j in range(start_y,end_y+1):
            count=0
            for i in range(start_x,end_x+1):
                if board[i][j]==1:
                    count+=1
            if count==4:
                for i in range(start_x,end_x+1):
                    board[i][j]=0
                this_round_score+=1
    if color=='g':
        for i in range(start_x,end_x+1):
            count=0
            for j in range(start_y,end_y+1):
                if board[i][j]==1:
                    count+=1
            if count==4:
                for j in range(start_y,end_y+1):
                    board[i][j]=0
                this_round_score+=1

    return this_round_score

def check_01(board,start_x,end_x,start_y,end_y,color):
    if color=='b':
        count=0
        for j in range(start_y,start_y+2):
            zero_cnt=0
            for i in range(start_x,end_x+1):
                if board[i][j]==0:
                    zero_cnt+=1
            if zero_cnt!=4:
                count+=1
        for j in range(end_y+1-count,end_y+1):
            for i in range(start_x,end_x+1):
                board[i][j]=0
    elif color=='g':
        count=0
        for i in range(start_x,start_x+2):
            zero_cnt=0
            for j in range(start_y,end_y+1):
                if board[i][j]==0:
                    zero_cnt+=1
            if zero_cnt!=4:
                count+=1
        for i in range(end_x+1-count,end_x+1):
            for j in range(start_y,end_y+1):
                board[i][j]=0

score=0
for tc in range(int(input())):
    t,x,y=map(int,input().split())
    gb_stack(board,t,x,y,'g')
    gb_stack(board,t,x,y,'b')

    score+=get_score(board,0,3,4,9,'b')
    score+=get_score(board,4,9,0,3,'g')


    down_block(board,0,3,4,9,'b')
    down_block(board,4,9,0,3,'g')

    check_01(board,0,3,4,9,'b')
    check_01(board,4,9,0,3,'g')


    down_block(board,0,3,4,9,'b')
    down_block(board,4,9,0,3,'g')

print(score)
cnt=0

for i in range(0,10):
    for j in range(0,10):
         if board[i][j]==1:
             cnt+=1

print(cnt)
