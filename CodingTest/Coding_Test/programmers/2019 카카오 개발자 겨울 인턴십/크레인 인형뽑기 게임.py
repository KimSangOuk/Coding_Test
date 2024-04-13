# 풀이시간 17분
# 1회차 정답
# 게임 보드에서 크레인이 작동될 때, 뽑히는 인형을 바구니에 쌓아서 같으면 없어지는 문제이기 때문에 바구니의 경우는 스택처럼 가장 앞에 있는 원소만 확인하면서 같은지 확인하면 된다. 같지 않을 경우에는 스택에 쌓으면 된다. 인형을 뽑는 함수는 따로 만들어서 위에서부터 인형이 존재할 경우, 그 인형을 지우고 반납하고 없을 경우에는 False를 반납하여 인형이 존재하지 않는 뽑기 행위를 나타냈다.

from collections import deque

def pick_doll(board,pos):
    for i in range(len(board)):
        if board[i][pos-1]!=0:
            doll=board[i][pos-1]
            board[i][pos-1]=0
            return doll
    return False

def solution(board, moves):
    answer = 0

    basket=deque()
    for i in moves:
        pass
        now=pick_doll(board,i)
        if not now:
            continue
        if len(basket)!=0 and now==basket[0]:
            answer+=2
            basket.popleft()
        else:
            basket.appendleft(now)

    return answer