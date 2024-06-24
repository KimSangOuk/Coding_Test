# 풀이시간 4시간/1시간 시간제한 2초 메모리제한 1024MB
# 1회차 정답 - But, 풀이시간 초과
# 시뮬레이션, 구현 문제의 상위 문제이다. 먼저 물고기를 칸마다 저장해둔다고 생각하고 각 물고기를 2차원 배열에 저장하돼 여러 마리가 있음을 생각해서 배열에 넣어둔다. 복제 마법시에는 이 물고기를 처음으로 복사 해둔다. 그런 다음, 물고기를 이동시킨는데 물고기는 8가지 방향을 순서대로 보면서 갈 수 있는 방향을 찾으면 그 방향으로 향한다. 이때, 물고기의 냄새가 있는 방향, 상어가 있는 방향은 가지 못한다. 모든 물고기의 이동이 끝나면 상어가 3칸 이동하는데, 이 경우는 DFS로 푸는 것으로 접근했다. 상어는 처음 지점을 생략하고 다른 지점부터 가는데, 갔던 칸을 다시 갈 수 있으며 이때 먹는 물고기의 수, 이동방향의 사전순으로 가는 길을 선택한다. 가는 길이 선택되면 상어는 그 방향으로 이동하며 물고기들을 없앤다. 이때, 물고기가 없어진 곳은 물고기의 냄새가 남는다. 그리고 물고기의 냄새가 전체적으로 -1 된다. 마지막으로 복사된 물고기가 붙여넣기 되면서 마무리 된다.
# 시간이 오래 걸린 것은 두가지 때문이다. 처음은 상어의 조건을 정확히 알아보지 못해서 틀렸다. 상어의 출발 조건이 정확하게 적혀있지 않았기 때문에 처음시작 점에서 먹고 나서 시작인줄 알고 시도 했다가 틀렸다. 그리고 재방문 여부또한 표시가 되어 있지 않았기에 방문한 곳은 다시 방문하지 않는 걸로 시도했다가 틀렸었다. 이렇게 조건이 명확하게 적혀있지 않은 경우에는 명시되지 않은 쪽으로 생각하는 것이 맞다는 것을 알게 되었다. 예를들면 재방문의 여부에 대한 말이 없기 때문에 그냥 다 방문해도 된다고 생각하는 것이다.
# 두번째는 상어의 시작지점에서 물고기를 먹어버린 거때문에 오래걸렸는데 코드가 길다보니 틀린 곳을 찾는데 한참 걸렸다. 

import copy

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

shark_dx=[-1,0,1,0]
shark_dy=[0,-1,0,1]

m,s=map(int,input().split())

fish_board=[[{"fishes":[]} for _ in range(5)] for _ in range(5)]
fish_smell_cnt_board=[[0]*5 for _ in range(5)]
for _ in range(m):
    fx,fy,d=map(int,input().split())
    fish_board[fx][fy]["fishes"].append((fx,fy,d-1))

shark_x,shark_y=map(int,input().split())
shark_pos=[shark_x,shark_y]

def fishes_move(fish_board,shark_pos,smell_cnt_board):
    new_fish_board=[[{"fishes":[]} for _ in range(5)] for _ in range(5)]
    for i in range(1,5):
        for j in range(1,5):
            for fx,fy,fd in fish_board[i][j]["fishes"]:
                nd=fd
                find=False
                for k in range(8):
                    nx=fx+dx[nd]
                    ny=fy+dy[nd]
                    nd=(nd-1)%8
                    if nx<1 or ny<1 or nx>=5 or ny>=5:
                        continue
                    if [nx,ny]==shark_pos:
                        continue
                    if smell_cnt_board[nx][ny]>0:
                        continue
                    new_fish_board[nx][ny]["fishes"].append((nx,ny,(nd+1)%8))
                    find=True
                    break
                if not find:
                    new_fish_board[fx][fy]["fishes"].append((fx,fy,fd))

    return new_fish_board

def from_str_to_10(dirs):
    new_str=""
    for i in dirs:
        if i=="상":
            new_str+="1"
        elif i=="좌":
            new_str+='2'
        elif i=="하":
            new_str+='3'
        elif i=="우":
            new_str+='4'
    return int(new_str)

def bfs(fish_board,visited,deep,cnt,path_dirs,x,y):
    global pathes
    if x<1 or y<1 or x>=5 or y>=5:
        return
    if deep==0:
        deep+=1
        bfs(fish_board,visited,deep,cnt,path_dirs+"상",x-1,y)
        bfs(fish_board,visited,deep,cnt,path_dirs+"하",x+1,y)
        bfs(fish_board,visited,deep,cnt,path_dirs+"좌",x,y-1)
        bfs(fish_board,visited,deep,cnt,path_dirs+"우",x,y+1)
    elif deep==3:
        k=from_str_to_10(path_dirs)
        if not visited[x][y]:
            cnt+=len(fish_board[x][y]["fishes"])
        pathes.append([cnt,k,path_dirs])
    else:
        deep+=1
        if not visited[x][y]:
            cnt+=len(fish_board[x][y]["fishes"])
        visited[x][y]=True
        bfs(fish_board,visited,deep,cnt,path_dirs+"상",x-1,y)
        bfs(fish_board,visited,deep,cnt,path_dirs+"하",x+1,y)
        bfs(fish_board,visited,deep,cnt,path_dirs+"좌",x,y-1)
        bfs(fish_board,visited,deep,cnt,path_dirs+"우",x,y+1)
        visited[x][y]=False

def find_method_shark(shark_pos,fish_board):
    # bfs로 3칸이 가능한 모든 경우 찾기
    global pathes
    path_directions=""
    deep=0
    pathes=[]
    fish_cnt=0
    now_x,now_y=shark_pos
    visited=[[False]*5 for _ in range(5)]
    bfs(fish_board,visited,deep,fish_cnt,path_directions,now_x,now_y)

    pathes.sort(key=lambda x:(-x[0],x[1]))
    return pathes[0]

def shark_move(fish_board,smell_cnt_board,shark_pos,method):
    arr_dir=[]
    for c in str(method):
        arr_dir.append(int(c))

    # 현재칸 물고기 제거
    sx,sy=shark_pos
    for d in arr_dir:
        nx=sx+shark_dx[d-1]
        ny=sy+shark_dy[d-1]
        if len(fish_board[nx][ny]["fishes"])>0:
            smell_cnt_board[nx][ny]=3
            fish_board[nx][ny]["fishes"]=[]
        sx,sy=nx,ny
    return [sx,sy]


for magic_cnt in range(s):
    # 1. 복제마법 시전(대기중)
    copy_magic_result=copy.deepcopy(fish_board)

    # 2. 모든 물고기 한 칸 이동
    fish_board=fishes_move(fish_board,shark_pos,fish_smell_cnt_board)

    # 3. 상어가 연속해서 3칸 이동
    # 제외되는 물고기가 가장 많은 방법 찾기
    method=find_method_shark(shark_pos,fish_board)
    # 물고기 제외시키고 물고기 냄새 남기기, 상어 위치 업데이트
    shark_pos=shark_move(fish_board,fish_smell_cnt_board,shark_pos,method[1])

    # 4.두번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라짐
    for i in range(1,5):
        for j in range(1,5):
            if fish_smell_cnt_board[i][j]>0:
                fish_smell_cnt_board[i][j]-=1

    # 5. 1에서 사용한 복제 마법 완료
    for i in range(1,5):
        for j in range(1,5):
            fish_board[i][j]["fishes"]+=copy_magic_result[i][j]["fishes"]

total_fish_cnt=0
for i in range(1,5):
    for j in range(1,5):
        total_fish_cnt+=len(fish_board[i][j]["fishes"])

print(total_fish_cnt)