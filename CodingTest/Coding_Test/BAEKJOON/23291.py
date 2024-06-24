# 풀이시간 2시간 시간제한 2초 메모리제한 1024MB
# 1회차 정답 - But, 풀이시간 오래 걸림
# 구현, 시뮬레이션 문제의 고난이도 유형이다. 어항을 2차원 배열로 꽉채워 표현할까, 아니면 줄이 추가 될때마다 따로 따질까 하다가 회전 같은 면에서 더 쉽기도 하고, 회전 하고 엊을 때, 마지막 줄 이외의 줄만 따져주면 되는 식이라서 그냥 후자의 방법을 선택하였다.
# 1. 처음에는 물고기의 수를 가장 작은 인덱스들을 찾아서 그 중에서 +1을 해주면 된다. 2. 맨 왼쪽에 있는 어항을 빼서 쌓고 3. 이제 반복문을 시행하여 총 높이가 맨 밑에 줄의 길이에서 위에 쌓인 높이의 인덱스를 뺀, 즉 남은 블록의 길이보다 길어지면 중단한다. 시계방향으로 돌리는 경우는 그저 왼쪽 밑에서부터 한줄로 만드는 방식과 동일하게 읽으면서 맨 윗줄부터 추가하면 된다. 4. 물고기의 수를 조절한다. 이 때 동시에 일어나고 범위에 유의하도록 한다. 또한 방문했던 곳은 다시 방문하지 않도록 한다. 나는 집합을 사용해서 중복을 확인했지만 오른쪽과 아래 방향으로만 따져도 될거라는 생각이 들었다. 5. 일렬로 만든다. 맨 밑에 왼쪽부터 위쪽으로 읽으면 된다. 6. 다시 공중 부앙 시키고 180도 회전을 하는데 이 때는 끊어지는 길이가 두번 다 정해져있기 때문에 배열에서 분리하고 뒤집는 작업을 반복해주면 된다. 6. 똑같은 조절과 한줄 만들기를 해주고 7. 탈출 조건을 확인해서 탈출 해주면 된다.

from collections import deque

n,k=map(int,input().split())

dx=[0,0,-1,1]
dy=[-1,1,0,0]

fish_tanks=[]
fish_tanks.append(list(map(int,input().split())))


def get_max_min_differ():
    max_fishes=max(fish_tanks[0])
    min_fishes=min(fish_tanks[0])
    return max_fishes-min_fishes

def over_two_stack_turn_and_stack(fish_tanks):
    while True:
        new_fish_tanks=[]
        height=len(fish_tanks)
        point=len(fish_tanks[0])
        if height>len(fish_tanks[height-1])-point:
            break

        for j in range(len(fish_tanks[height-1])):
            if j<point:
                new_arr=[]
                for i in range(height-1,-1,-1):
                    new_arr.append(fish_tanks[i][j])
                new_fish_tanks.append(new_arr)
            else:
                break
        new_fish_tanks.append(fish_tanks[height-1][point:])
        fish_tanks=new_fish_tanks

    return fish_tanks

def make_one_line(fish_tanks):
    new_fish_tanks=[]
    one_line_arr=[]
    height=len(fish_tanks)
    point=len(fish_tanks[0])
    for j in range(len(fish_tanks[height-1])):
        if j<point:
            for i in range(height-1,-1,-1):
                one_line_arr.append(fish_tanks[i][j])
        else:
            one_line_arr.append(fish_tanks[height-1][j])

    new_fish_tanks.append(one_line_arr)
    return new_fish_tanks

def plus_one_fish_in_least_bowl(fish_tanks):
    new_fish_tanks=[]
    one_line_arr=fish_tanks[0]
    min_value=10001
    min_value_index_arr=[]
    for i in range(len(one_line_arr)):
        if min_value>one_line_arr[i]:
            min_value_index_arr=[]
            min_value_index_arr.append(i)
            min_value=one_line_arr[i]
        elif min_value==one_line_arr[i]:
            min_value_index_arr.append(i)
    for i in min_value_index_arr:
        one_line_arr[i]+=1
    new_fish_tanks.append(one_line_arr)
    return new_fish_tanks

def stack_left_block(fish_tanks):
    new_fish_tanks=[]
    one_line_arr=fish_tanks[0]
    q=deque(one_line_arr)
    new_fish_tanks.append([q.popleft()])
    new_fish_tanks.append(list(q))
    return new_fish_tanks

def control_fish_number(fish_tanks):
    height=len(fish_tanks)
    point=len(fish_tanks[0])
    w=len(fish_tanks[height-1])
    visited=set()
    up_and_down=[[0]*w for _ in range(height)]
    for i in range(height):
        if i!=height-1:
            for j in range(point):
                now=(i,j)
                for t in range(4):
                    nx=now[0]+dx[t]
                    ny=now[1]+dy[t]
                    if nx<0 or ny<0 or nx>=height or ny>=w:
                        continue
                    if 0<=nx<height-1 and ny>=point:
                        continue
                    tmp=[now,(nx,ny)]
                    tmp.sort()
                    tmp=tuple(tmp)
                    if tmp in visited:
                        continue
                    visited.add(tmp)
                    d=abs(fish_tanks[now[0]][now[1]]-fish_tanks[nx][ny])//5
                    if d>0:
                        if fish_tanks[now[0]][now[1]]>fish_tanks[nx][ny]:
                            up_and_down[now[0]][now[1]]-=d
                            up_and_down[nx][ny]+=d
                        elif fish_tanks[now[0]][now[1]]<fish_tanks[nx][ny]:
                            up_and_down[now[0]][now[1]]+=d
                            up_and_down[nx][ny]-=d
        else:
            for j in range(w):
                now=(i,j)
                for t in range(4):
                    nx=now[0]+dx[t]
                    ny=now[1]+dy[t]
                    if nx<0 or ny<0 or nx>=height or ny>=w:
                        continue
                    if 0<=nx<height-1 and ny>=point:
                        continue
                    tmp=[now,(nx,ny)]
                    tmp.sort()
                    tmp=tuple(tmp)
                    if tmp in visited:
                        continue
                    visited.add(tmp)
                    d=abs(fish_tanks[now[0]][now[1]]-fish_tanks[nx][ny])//5
                    if d>0:
                        if fish_tanks[now[0]][now[1]]>fish_tanks[nx][ny]:
                            up_and_down[now[0]][now[1]]-=d
                            up_and_down[nx][ny]+=d
                        elif fish_tanks[now[0]][now[1]]<fish_tanks[nx][ny]:
                            up_and_down[now[0]][now[1]]+=d
                            up_and_down[nx][ny]-=d

    for i in range(height):
        if i!=height-1:
            for j in range(point):
                fish_tanks[i][j]+=up_and_down[i][j]
        else:
            for j in range(w):
                fish_tanks[i][j]+=up_and_down[i][j]
    return fish_tanks

def n_div_two_turn_and_stack(fish_tanks):
    one_line_arr=fish_tanks[0]
    new_fish_tanks=[]
    new_fish_tanks.append(one_line_arr[:n//2][::-1])
    new_fish_tanks.append(one_line_arr[n//2:])
    second_new_fish_tanks=[]
    second_new_fish_tanks.append(new_fish_tanks[1][:n//4][::-1])
    second_new_fish_tanks.append(new_fish_tanks[0][:n//4][::-1])
    second_new_fish_tanks.append(new_fish_tanks[0][n//4:])
    second_new_fish_tanks.append(new_fish_tanks[1][n//4:])
    return second_new_fish_tanks

cnt=0

while True:
    cnt+=1
    # 1. 물고기 수 가장 작은 어항(다수 가능)에서 물고기 한마리 제거
    fish_tanks=plus_one_fish_in_least_bowl(fish_tanks)

    # 2. 가장 왼쪽 어항을 위로 쌓기
    fish_tanks=stack_left_block(fish_tanks)

    # 3. 두개 이상 쌓여있는 어항, 공중부앙 해서 90도 시계방향 회전 후 위에다가 쌓기
    fish_tanks=over_two_stack_turn_and_stack(fish_tanks)

    # 4. 물고기의 수 조절
    fish_tanks=control_fish_number(fish_tanks)

    # 5. 다시 일렬로 만듬
    fish_tanks=make_one_line(fish_tanks)

    # 6. N//2개 공중부앙 시켜서 180도 회전 후 쌓기 2회
    fish_tanks=n_div_two_turn_and_stack(fish_tanks)

    # 7. 다시 일렬로 만듬
    fish_tanks=control_fish_number(fish_tanks)
    fish_tanks=make_one_line(fish_tanks)
    # print(fish_tanks)

    # 8. 가장 많은 어항의 물고기와 적은 어항의 물고기의 수의 차가 K이하가 되면 종료
    if k>=get_max_min_differ():
        break

print(cnt)