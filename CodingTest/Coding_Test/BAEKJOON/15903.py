# - 두 개의 숫자를 꺼내서 그 합을 그 두개의 카드에 다시 넣었을 때, 그 결과값이 최소가 되야 하므로 계속해서 2개의 숫자는 가장 작은 값을 꺼내야 한다. 그렇기 때문에 지금 현상황에서 필요한 것을 꺼내는 그리디라고 볼 수 있으며 단순히 힙큐를 사용하면 두수를 쉽게 꺼내고 넣을 수 있다.
# - 풀이시간 : 5분

import heapq

n,m=map(int,input().split())
q=list(map(int,input().split()))
heapq.heapify(q)

for _ in range(m):
    a=heapq.heappop(q)
    b=heapq.heappop(q)
    heapq.heappush(q,a+b)
    heapq.heappush(q,a+b)

print(sum(q))