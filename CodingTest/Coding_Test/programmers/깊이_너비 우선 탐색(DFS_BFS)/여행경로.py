# 풀이시간 1시간
# 1회차 정답
# DPS에서 갔던 길을 다시 갈 수 있는 방법을 사용한 문제이다. 이때, 우리는 티켓의 사용으로 이용을 제한하기 때문에 굳이 visited를 사용하지 않고 티켓을 제거해가며 방문을 하면 된다. 여기서 코드를 돌려보면서 깨달은 점 두가지가 있다.
# 첫번째, 복구의 문제가 발생할 수 있기 때문에 최대한 복구를 시키지 않도록 다음상태를 만들어서 dfs를 사용하는 것이 좋다는 점
# 두번째, 마지막 답 지정에서 복사가 아니면 배열 같은 경우 복구 될 수 있기 때문에 깊은 복사를 사용하는 것이 좋다는 점이다.

import copy

def dfs(start,tickets,path):
    global result
    left_tickets=copy.deepcopy(tickets)
    if len(left_tickets)==0:
        new_path=copy.deepcopy(path)
        result.append(new_path)
        return
    for a,b in tickets:
        if a==start:
            next_path=path+[b]
            index=tickets.index([a,b])
            next_tickets=tickets[:index]+tickets[index+1:]
            dfs(b,next_tickets,next_path)


def solution(tickets):

    global result

    result=[]
    dfs("ICN",tickets,["ICN"])
    result.sort()

    return result[0]