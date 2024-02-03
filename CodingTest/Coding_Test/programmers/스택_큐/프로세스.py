# 풀이시간 25분
# 1회차 정답
# 처음에는 우선순위 큐인줄 알고 접근했으나 그럴 경우에는 각 수가 다시 돌아오는 경우를 찾을 수가 없어서 덱으로 풀었다. 덱으로 우선순위와 각 인덱스를 넣은 다음 전부 빌때까지 반복하면서 진행한다. 각 진행마다 하나씩 큐에서 빼고 그 큐에서 가장 높은 우선순위를 찾은 다음 우선순위 목록에서도 제거하고 만약 우리가 찾는 인덱스와 동일한 경우에는 종료하고 답을 반환한다. 만약 제일 높은 우선순위가 아닌 경우에는 다시 넣는다.

from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    while q:
        prior,num=q.popleft()
        max_prior=0
        for i in range(len(priorities)):
            max_prior=max(max_prior,priorities[i])
        if max_prior==prior:
            answer+=1
            priorities.remove(max_prior)
            if num==location:
                break
        elif max_prior!=prior:
            q.append((prior,num))
        # print(q)
    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))