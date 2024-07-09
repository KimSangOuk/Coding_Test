from collections import deque

def solution(queue1, queue2):
    answer = 0

    isCanMake=False
    len_q1=len(queue1)
    len_q2=len(queue2)
    q1=deque(queue1)
    q2=deque(queue2)

    # 큐의 넣음과 뺌이 연속됨을 유지하므로 각 배열을 연결한 뒤 2배한 것에서 찾을 수 있다.
    total_q=(queue1+queue2)*2
    target_sum_value=sum(queue1+queue2)/2

    # 두개의 합이 홀수가 되어 둘로 나누어질 수 없을 경우
    if target_sum_value-int(target_sum_value)>0:
        return -1

    # 이미 각 배열의 합이 같을 경우
    if sum(queue1)==sum(queue2):
        return 0

    q1=deque(queue1)
    q1_sum=sum(queue1)
    q2=deque(queue2)
    q2_sum=sum(queue2)
    while True:
        if answer>650000:
            break
        if q1_sum>q2_sum:
            k=q1.popleft()
            q2.append(k)
            q1_sum-=k
            q2_sum+=k
            answer+=1
        elif q1_sum==q2_sum:
            return answer
        elif q1_sum<q2_sum:
            k=q2.popleft()
            q1.append(k)
            q2_sum-=k
            q1_sum+=k
            answer+=1


    # 두개의 배열로 나누었을 때, 합이 최종적으로 나누어질 수 없는 경우
    if not isCanMake:
        return -1

    return answer