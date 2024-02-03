# 풀이시간 3시간/1시간 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이시간 초과 / 풀이방법에 접근하지 못함
# 각 면이 돌아갈 때, 한 면을 방향에 따라 돌리고 나머지 사이드에 붙어있는 4면의 큐빅을 회전시키는 문제이다. 시뮬레이션 문제인데, 이게 상당히 시간이 오래걸렸다. 처음에는 어떻게든 규칙이 있지 않을까 싶어서 코드 길이를 줄이고자 각 큐빅을 받아서 회전시키는 식으로 했다가 회전하는 면에 따라 큐빅이 돌아갈 때, 들어가는 방향이 일정하지 않아서 오래걸리기도 하고 다시 풀이 방법을 보고 다시 풀었다.
# 일일이 넣는 방식을 사용해서 풀었는데, 풀이방법이 없을 경우 풀 수 있는 최고의 방법이라는 것을 깨달았다. 왜 이 방식으로 풀지 못했는가? 규칙이 없을 때는, 단순하게 넣는 시뮬레이션 유형을 생각했어야 했는데 회전방식에 따라서 규칙성이 있을 줄 알았다. 왜 이 방법을 생각해내지 못했는가? 오히려 규모가 작고 단순하면 모든 경우의 수를 일일이 입력하는 방식이 있다고도 생각했어야 했는데 계속해서 규칙성을 쫓는 습관이 있었다. 그리고 이렇게까지 단순화시켜서 일일이 입력하는 문제는 거의 처음이었다. 
# 결국, 반복성을 계속해서 찾으려는 습관이 있는데 이를 미리 머리속으로 반복성이 가능하고 규칙성이 가능한지를 시뮬레이션 해보고 안될 시에는 데이터의 크기등을 보고 직접할 생각을 해야겠다고 생각이 들었다.

import sys
input=sys.stdin.readline

# 명칭에 따라 면 리턴
def select_side(side_name):
    if side_name=='U':
        return up_side
    if side_name=='D':
        return down_side
    if side_name=='F':
        return front_side
    if side_name=='B':
        return back_side
    if side_name=='L':
        return left_side
    if side_name=='R':
        return right_side

# 보이는 면 회전 함수
def clockwise_now(side_name,clockwise):
    turn_side=select_side(side_name)
    new_side=[[0]*3 for _ in range(3)]

    if clockwise=='+':
        for i in range(3):
            for j in range(3):
                new_side[j][2-i]=turn_side[i][j]
    if clockwise=='-':
        for i in range(3):
            for j in range(3):
                new_side[2-j][i]=turn_side[i][j]
    return new_side


def turn_sides(side_name):
    if side_name=='U':
        tmp1,tmp2,tmp3=front_side[0][0],front_side[0][1],front_side[0][2]
        front_side[0][0],front_side[0][1],front_side[0][2]=right_side[0][0],right_side[0][1],right_side[0][2]
        right_side[0][0],right_side[0][1],right_side[0][2]=back_side[0][0],back_side[0][1],back_side[0][2]
        back_side[0][0],back_side[0][1],back_side[0][2]=left_side[0][0],left_side[0][1],left_side[0][2]
        left_side[0][0],left_side[0][1],left_side[0][2]=tmp1,tmp2,tmp3
    if side_name=='D':
        tmp1,tmp2,tmp3=front_side[2][0],front_side[2][1],front_side[2][2]
        front_side[2][0],front_side[2][1],front_side[2][2]=left_side[2][0],left_side[2][1],left_side[2][2]
        left_side[2][0],left_side[2][1],left_side[2][2]=back_side[2][0],back_side[2][1],back_side[2][2]
        back_side[2][0],back_side[2][1],back_side[2][2]=right_side[2][0],right_side[2][1],right_side[2][2]
        right_side[2][0],right_side[2][1],right_side[2][2]=tmp1,tmp2,tmp3
    if side_name=='F':
        tmp1,tmp2,tmp3=right_side[0][0],right_side[1][0],right_side[2][0]
        right_side[0][0],right_side[1][0],right_side[2][0]=up_side[2][0],up_side[2][1],up_side[2][2]
        up_side[2][0],up_side[2][1],up_side[2][2]=left_side[2][2],left_side[1][2],left_side[0][2]
        left_side[2][2],left_side[1][2],left_side[0][2]=down_side[2][0],down_side[2][1],down_side[2][2]
        down_side[2][0],down_side[2][1],down_side[2][2]=tmp1,tmp2,tmp3
    if side_name=='B':
        tmp1,tmp2,tmp3=left_side[0][0],left_side[1][0],left_side[2][0]
        left_side[0][0],left_side[1][0],left_side[2][0]=up_side[0][2],up_side[0][1],up_side[0][0]
        up_side[0][2],up_side[0][1],up_side[0][0]=right_side[2][2],right_side[1][2],right_side[0][2]
        right_side[2][2],right_side[1][2],right_side[0][2]=down_side[0][2],down_side[0][1],down_side[0][0]
        down_side[0][2],down_side[0][1],down_side[0][0]=tmp1,tmp2,tmp3
    if side_name=='R':
        tmp1,tmp2,tmp3=back_side[0][0],back_side[1][0],back_side[2][0]
        back_side[0][0],back_side[1][0],back_side[2][0]=up_side[2][2],up_side[1][2],up_side[0][2]
        up_side[2][2],up_side[1][2],up_side[0][2]=front_side[2][2],front_side[1][2],front_side[0][2]
        front_side[2][2],front_side[1][2],front_side[0][2]=down_side[0][0],down_side[1][0],down_side[2][0]
        down_side[0][0],down_side[1][0],down_side[2][0]=tmp1,tmp2,tmp3
    if side_name=='L':
        tmp1,tmp2,tmp3=front_side[0][0],front_side[1][0],front_side[2][0]
        front_side[0][0],front_side[1][0],front_side[2][0]=up_side[0][0],up_side[1][0],up_side[2][0]
        up_side[0][0],up_side[1][0],up_side[2][0]=back_side[2][2],back_side[1][2],back_side[0][2]
        back_side[2][2],back_side[1][2],back_side[0][2]=down_side[2][2],down_side[1][2],down_side[0][2]
        down_side[2][2],down_side[1][2],down_side[0][2]=tmp1,tmp2,tmp3



def play_cube(oper):
    side_name=oper[0]
    clockwise=oper[1]
    # 일단 보이는 면 회전(시계, 반시계)
    old=select_side(side_name)
    new=clockwise_now(side_name,clockwise)
    for i in range(3):
        for j in range(3):
            old[i][j]=new[i][j]
    if clockwise=='+':
        turn_sides(side_name)
    else:
        for i in range(3):
            turn_sides(side_name)


for tc in range(int(input())):
    up_side=[['w']*3 for _ in range(3)]
    down_side=[['y']*3 for _ in range(3)]
    front_side=[['r']*3 for _ in range(3)]
    back_side=[['o']*3 for _ in range(3)]
    left_side=[['g']*3 for _ in range(3)]
    right_side=[['b']*3 for _ in range(3)]
    n=int(input())
    opers=list(map(str,input().split()))
    for oper in opers:
        play_cube(oper)

    for i in range(3):
        for j in range(3):
            print(up_side[i][j],end='')
        print()