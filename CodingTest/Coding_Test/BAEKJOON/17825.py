# 풀이시간 1시간 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 브루트 포스 알고리즘이자 시뮬레이션 문제이다. 주사위가 나오는 수가 정해지고 턴이 정해졌기 때문에 각 턴마다 어떤 주사위를 선택할지를 경우의수로 구하면 된다. 모든 경우의 수는 말이 4개 이므로 4^10이기 때문에 중복순열로 고르면 된다. 경우의 수는 약 100만이 나오기 때문에 해볼만 하다. 각 말의 현재 위치를 기준으로 케이스별로 말을 진행시키는데 이 때, 그래프, 즉 윷놀이 판에서 처음이고 파란색 선이 있을 경우에만 파란색 화살표로 이동시켜주고 나머지는 횟수대로 빨간색으로 이동시켜주면 된다. 중간에 도착지점에 도착하거나 최종적으로 도착지점에 도착하는 경우, 또 처음 시작점이 도착지점인 경우에는 중지시키면 만약 시작점이 도착지점인 경우는 최댓값이 될 수 없기 때문에 제외시켜주면 된다. 또한 이미 움직일 지점에 다른 말이 있을 경우에도 최댓값이 될 수 없기 때문에 제외시키면 되며 이 경우는 도착지점이 최종지점이 아닐 때, 다른 말의 위치를 확인해주면 된다.

from itertools import product

board_score=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,22,24,28,27,26,30,35,0]

# 윷놀이 판
graph=[[] for _ in range(33)]
for i in range(0,20):
    graph[i].append((i+1,1))
for i in range(21,24):
    graph[i].append((i+1,1))
graph[25].append((26,1))
for i in range(27,29):
    graph[i].append((i+1,1))
graph[30].append((31,1))
graph[5].append((21,2))
graph[10].append((25,2))
graph[15].append((27,2))
graph[26].append((24,1))
graph[29].append((24,1))
graph[24].append((30,1))
graph[31].append((20,1))
graph[20].append((32,1))

def go(num,go_cnt):
    pos=horse_pos[num]
    n_pos=pos
    for i in range(go_cnt):
        if n_pos==32:
            break
        nk=0
        if i==0 and len(graph[n_pos])>1:
            for next,color in graph[n_pos]:
                if color==2:
                    nk=next
        else:
            for next,color in graph[n_pos]:
                if color==1:
                    nk=next
        n_pos=nk
    if n_pos!=32 and n_pos in horse_pos:
        return False
    horse_pos[num]=n_pos
    return True


result=0
dice=list(map(int,input().split()))
for case in product(range(1,5),repeat=10):

    score=0
    horse_pos=[0,0,0,0,0]
    for i in range(10):
        now=case[i]
        go_cnt=dice[i]
        if horse_pos[now]==32:
            break
        if not go(now,go_cnt):
            break
        score+=board_score[horse_pos[now]]
    result=max(result,score)

print(result)