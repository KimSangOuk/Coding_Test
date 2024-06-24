# 이것이 취업을 위한 코딩테스트다 part03 '26. 카드 정렬하기'와 동일

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