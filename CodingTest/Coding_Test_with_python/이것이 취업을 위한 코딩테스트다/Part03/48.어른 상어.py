# 풀이시간 1시간 20분/1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답 - 풀이시간 초과
# 구현, 시뮬레이션 유형의 고난이도 문제이다. 시간복잡도는 시간이 최대 1000에 상어의 움직임이 400칸 안에서 한정되기 때문에 많아야 1600이라 넘을 일은 거의 없을 거라 생각했다.
# 먼저 상어의 현 위치의 정보를 받고 처음 방향 정보를 받아서 현재 상어의 정보를 좌표와 방향으로 저장을 해두었다. 또한 우선순위 정보를 받는데, 자료의 형태가 복잡하기 때문에 딕셔너리로 만들어냈다. 그리고 마지막으로 냄새를 뿌린 상어와 그 남은 시간의 정보를 담을 배열이 필요하기 때문에 이 또한 2차원 배열에 딕셔너리를 넣어서 만들어주었다.
# 시간이 진행되면서 처음에 위치한 상어의 위치에 냄새를 뿌려준다. 이 때, 없는 상어는 제외시켜주어야 한다. 그 다음 먼저 빈칸 순으로 위치를 찾는데 이 때, 냄새가 있거나 경계 밖은 제외시키며 찾은 방향으로 진행하되, 만약 그곳에 먼저 온 상어가 있다면 현재의 상어를 소멸 시킨다. 방향을 이 때 못찾은 경우라면 현재 자신이 남긴 냄새 중, 우선순위 방향으로 이동한다. 그리고 전체 칸에서 냄새를 1씩 감소시키면 된다. 종료조건은 1보다 큰 상어가 남아있는지를 상어의 유무를 통해 확인해주면 된다. 

n,m,k=map(int,input().split())

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

start_direction=list(map(int,input().split()))

shark_info=dict()
for i in range(n):
    for j in range(n):
        if 1<=board[i][j]<=m:
            shark_info[board[i][j]]=[i,j,start_direction[board[i][j]-1]]

priority=dict()
for i in range(1,m+1):
    priority[i]=dict()

for i in range(1,m+1):
    for j in range(1,5):
        priority[i][j]=list(map(int,input().split()))


time=0
board_about_smell=[[{"from":-1, "last_k":-1} for _ in range(n)] for _ in range(n)]
while time<1000:
    for shark_num in range(1,m+1):
        if shark_info[shark_num]==[-1,-1,-1]:
            continue
        now_x,now_y,now_d=shark_info[shark_num]
        board_about_smell[now_x][now_y]["from"]=shark_num
        board_about_smell[now_x][now_y]["last_k"]=k

    for shark_num in range(1,m+1):
        now_x,now_y,now_d=shark_info[shark_num]
        if shark_info[shark_num]==[-1,-1,-1]:
            continue
        # 먼저 아무 냄새가 없는 칸의 방향 중 우선순위 고려
        find_no_smell_direction=False
        for d in priority[shark_num][now_d]:
            nx=now_x+dx[d]
            ny=now_y+dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if board_about_smell[nx][ny]["last_k"]>0:
                continue
            find_no_smell_direction=True
            # 찾았다면 이동
            # 만약 가는 칸에 다른 상어가 있으면 현재의 번호가 더 높기 때문에 죽음
            if board[nx][ny]!=0:
                shark_info[shark_num]=[-1,-1,-1]
            else: # 그냥 갈 수 있는 빈칸이라면 그냥 이동
                shark_info[shark_num]=[nx,ny,d] # 상어의 정보 업데이트
                board[nx][ny]=shark_num # 상어의 움직임 업데이트
            board[now_x][now_y]=0
            break
        # 만약 아무 냄새가 없는 칸이 없다면 자신의 냄새가 있는 칸 중 우선순위 고려
        if not find_no_smell_direction:
            for d in priority[shark_num][now_d]:
                nx=now_x+dx[d]
                ny=now_y+dy[d]
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                if board_about_smell[nx][ny]["from"]==shark_num:
                    # 찾았다면 이동
                    shark_info[shark_num]=[nx,ny,d]
                    board[nx][ny]=shark_num
                    board[now_x][now_y]=0
                    break
    # 상어가 있는 칸에는 새로 냄새를 뿌리고 아닌 칸에 k가 남아있다면 1씩 감소시킨다.
    for i in range(n):
        for j in range(n):
            if board[i][j]>0:
                board_about_smell[i][j]["from"]=board[i][j]
                board_about_smell[i][j]["last_k"]=k
            elif board_about_smell[i][j]["last_k"]>0:
                board_about_smell[i][j]["last_k"]-=1
    # 시간 증가
    time+=1
    last_one_on_board=True
    for i in range(n):
        for j in range(n):
            if board[i][j]>1:
                last_one_on_board=False
                break
    if last_one_on_board:
        break


another_shark_on_board=False
for i in range(n):
    for j in range(n):
        if board[i][j]>1:
            another_shark_on_board=True
            break

if another_shark_on_board:
    print(-1)
else:
    print(time)