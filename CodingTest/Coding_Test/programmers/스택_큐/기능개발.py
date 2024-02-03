# 풀이시간 20분
# 1회차 정답
# 진행도 만큼 하루에 진행시키고 앞에서부터 진행도가 100이 넘어가는 개수만큼 스택에서 제거하면서 그 숫자를 세면 되는 문제이다.

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses=deque(progresses)
    speeds=deque(speeds)
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]

        count=0
        while progresses:
            if progresses[0]>=100:
                progresses.popleft()
                speeds.popleft()
                count+=1
            else:
                break
        if count>0:
            answer.append(count)

    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))