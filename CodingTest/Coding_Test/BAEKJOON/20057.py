# 풀이시간 56분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 토네이도의 방향대로 진행하면서 모래를 퍼트리고 그 중 나가는 모래의 양을 체크하는 문제이다. 모래의 이동방향의 경우 왼쪽 방향으로 꺾이면서 진행하는데 이 때, 이미 방문한 곳으로는 방향이 진행되지 않고 앞으로 방향이 진행된다. 그렇게 0,0에 도달할 때까지 진행하는데 각 9개의 곳에 퍼센트지 만큼 뿌려진다. 이 때 퍼센티지 만큼 y칸을 기준으로 다른 곳에 쌓이고 모래밭 밖으로 나갈 경우에는 결과값에 더해진다. 퍼센티지 칸이 끝난 후 남은 모래는 alpha값에 쌓이거나 alpha 칸이 밖에 있을 경우에는 이 또한 결과값에 더해진다. 그렇게 계속해서 진행하면 된다.

n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[-1,0,1,0]

percent=[5,10,10,2,2,7,7,1,1]

visited=[[False]*n for _ in range(n)]

def next_dir(visited,dir,x,y):
    nd=(dir+1)%4
    nx=x+dx[nd]
    ny=y+dy[nd]
    if visited[nx][ny]:
        return dir
    return nd

x,y=n//2,n//2
visited[x][y]=True
dir=0
out_sand=0
while not visited[0][0]:
    # x에서 y로 이동
    x_pos=[x,y]
    y_pos=[x+dx[dir],y+dy[dir]]
    visited[y_pos[0]][y_pos[1]]=True

    percent_spread=[[0,0] for _ in range(9)]

    y_sand=a[y_pos[0]][y_pos[1]]
    send_sand=0

    # %로 퍼지는 모래
    percent_spread[0]=[y_pos[0]+2*dx[dir],y_pos[1]+2*dy[dir]]
    percent_spread[1]=[y_pos[0]+dx[dir]+dx[(dir+1)%4],y_pos[1]+dy[dir]+dy[(dir+1)%4]]
    percent_spread[2]=[y_pos[0]+dx[dir]+dx[(dir-1)%4],y_pos[1]+dy[dir]+dy[(dir-1)%4]]
    percent_spread[3]=[y_pos[0]+2*dx[(dir+1)%4],y_pos[1]+2*dy[(dir+1)%4]]
    percent_spread[4]=[y_pos[0]+2*dx[(dir-1)%4],y_pos[1]+2*dy[(dir-1)%4]]
    percent_spread[5]=[y_pos[0]+dx[(dir+1)%4],y_pos[1]+dy[(dir+1)%4]]
    percent_spread[6]=[y_pos[0]+dx[(dir-1)%4],y_pos[1]+dy[(dir-1)%4]]
    percent_spread[7]=[y_pos[0]-dx[dir]+dx[(dir+1)%4],y_pos[1]-dy[dir]+dy[(dir+1)%4]]
    percent_spread[8]=[y_pos[0]-dx[dir]+dx[(dir-1)%4],y_pos[1]-dy[dir]+dy[(dir-1)%4]]
    alpha=[y_pos[0]+dx[dir],y_pos[1]+dy[dir]]

    for i in range(9):
        tmp_x,tmp_y=percent_spread[i]
        sand=(y_sand*percent[i])//100
        if tmp_x<0 or tmp_y<0 or tmp_x>=n or tmp_y>=n:
            out_sand+=sand
        else:
            a[tmp_x][tmp_y]+=sand
        send_sand+=sand

    if alpha[0]<0 or alpha[1]<0 or alpha[0]>=n or alpha[1]>=n:
        out_sand+=y_sand-send_sand
    else:
        a[alpha[0]][alpha[1]]+=y_sand-send_sand
    a[y_pos[0]][y_pos[1]]=0

    # 다음 이동을 위한 좌표 갱신
    x,y=y_pos
    dir=next_dir(visited,dir,x,y)

print(out_sand)