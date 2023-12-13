# 풀이시간 20분/30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 데이터의 수가 100,000 이기 때문에 시간복잡도가 O(NlongN) 이하 이므로 계수 정렬, 퀵 정렬 등을 고려해볼 수 있으나, 항상 우리는 최소의 두개의 수를 구해야 하기 때문에 우선순위 큐를 통한 정렬을 고려해볼 수 있다. 우선순위 큐의 시간복잡도는 O(logN)이기 때문에 시간복잡도 면에서는 가능한다.
# 최소의 두개의 수를 꺼낸 후 합쳐서 넣고 합은 그 수를 누적시키면 되는 문제이다.

import heapq

n=int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
arr=[]
for _ in range(n):
  heapq.heappush(arr,int(input()))

sum=0
# 힙(Heap)에 원소가 1개 남을 때까지
while len(arr)>1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  first=heapq.heappop(arr)
  second=heapq.heappop(arr)
  sum+=first+second
  # 카드 묶음을 합쳐서 다시 삽입
  heapq.heappush(arr,first+second)

print(sum)