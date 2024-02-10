# 풀이시간 2시간/1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답 - But, 풀이시간
# 낚시꾼이 이동하면서 상어를 건지는걸 시뮬레이션 하는 문제이다. 이때, 핵심은 상어의 이동이다.
# 먼저 낚시꾼이 이동하고 자신의 아래있는 열을 탐색하여 맨 위에 있는 상어를 제거하면서 크기를 결과값에 더한다. 그리고 낚시꾼이 열+1에 도착하면 종료하면 된다. 이 때, 상어가 움직이는데 상어는 동시에 움직이며 같은 칸에 두 마리 상어가 있으면 작은 상어를 소멸시키므로 큰 상어부터 이동시키며 만약 작은 상어가 이미 큰 상어가 있는 칸에 도착하면 제거한다. 상어의 이동은 상어가 벽에 닿는 순간 방향을 바꾸기 때문에 먼저 벽에 닿을 때까지 이동하고 행이나 열의 길이의 -1만을 한 수를 남은 거리에서 나누었을 때 나머지만큼 더 이동하면 된다. 이 때, 만약 나눈 값이 짝수라면 방향이 반대이고 출발지점에 처음 부딪친 벽이 된다. 그리고 만약 나눈 값이 홀수라면 방향은 유지되고 처음 부딪친 벽의 반대 방향이 나머지 칸을 세는 기준점이 된다. 그렇게 상어의 위치와 방향을 업데이트 해주면 된다. 동시 진행이기 때문에 새롭게 만든 배열에 넣었다가 업데이트 해준다.

r,c,m=map(int,input().split())

dx=[0,-1,1,0,0]
dy=[0,0,0,1,-1]

result=0

board=[[0]*(c+1) for _ in range(r+1)]
shark_info=dict()
shark_size_list=[]
for _ in range(m):
    shark_r,shark_c,shark_s,shark_d,shark_z=map(int,input().split())
    board[shark_r][shark_c]=shark_z
    shark_info[shark_z]=[shark_r,shark_c,shark_s,shark_d]
    shark_size_list.append(shark_z)

shark_size_list.sort(reverse=True)

def fishing(angler_pos,board,shark_info):
    global result
    for i in range(1,r+1):
        if board[i][angler_pos]>0:
            result+=board[i][angler_pos]
            shark_info[board[i][angler_pos]]=-1
            board[i][angler_pos]=0
            break

def shark_move(board,shark_info):
    new_board=[[0]*(c+1) for _ in range(r+1)]
    for size in shark_size_list:
        if shark_info[size]==-1:
            continue
        # 상어 이동 시키기(nx,ny)
        shark_r,shark_c,shark_s,d=shark_info[size]
        to_wall=0
        nx,ny=shark_r,shark_s
        if d==1:
            to_wall=shark_r-1
        elif d==2:
            to_wall=r-shark_r
        elif d==3:
            to_wall=c-shark_c
        elif d==4:
            to_wall=shark_c-1
        if shark_s-to_wall<=0:
            nx,ny=shark_r+dx[d]*shark_s,shark_c+dy[d]*shark_s
        else:
            div_value=(shark_s-to_wall)//(c-1) if d==3 or d==4 else (shark_s-to_wall)//(r-1)
            last_value=(shark_s-to_wall)%(c-1) if d==3 or d==4 else (shark_s-to_wall)%(r-1)
            if d==4:
                if div_value%2==0:
                    nx,ny,d=shark_r,1+last_value,3
                else:
                    nx,ny=shark_r,c-last_value
            elif d==3:
                if div_value%2==0:
                    nx,ny,d=shark_r,c-last_value,4
                else:
                    nx,ny=shark_r,1+last_value
            elif d==2:
                if div_value%2==0:
                    nx,ny,d=r-last_value,shark_c,1
                else:
                    nx,ny=1+last_value,shark_c
            elif d==1:
                if div_value%2==0:
                    nx,ny,d=1+last_value,shark_c,2
                else:
                    nx,ny=r-last_value,shark_c

        # 만약 큰 상어가 이미 칸에 있으면 제거
        if new_board[nx][ny]>0:
            board[shark_info[size][0]][shark_info[size][1]]=0
            shark_info[size]=-1
            continue
        # 아니라면 상어 이동
        new_board[nx][ny]=size
        shark_info[size][0],shark_info[size][1],shark_info[size][3]=nx,ny,d

    # 상어 이동을 확정
    for i in range(1,r+1):
        for j in range(1,c+1):
            board[i][j]=new_board[i][j]

angler_pos=0

while True:
    angler_pos+=1
    if angler_pos>c:
        print(result)
        break
    fishing(angler_pos,board,shark_info)

    shark_move(board,shark_info)