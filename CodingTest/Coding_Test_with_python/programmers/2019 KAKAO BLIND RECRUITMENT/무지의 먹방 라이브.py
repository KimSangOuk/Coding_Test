# 이것이 취업을 위한 코딩테스트다 part03 '06. 무지의 먹방 라이브'와 동일

import heapq

def solution(food_times, k):
  answer = 0

  q=[]
  reduce=0

  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))

  while q and k>=(q[0][0]-reduce)*len(q):
    k-=(q[0][0]-reduce)*len(q)
    reduce+=q[0][0]-reduce
    heapq.heappop(q)

  if q:
    q.sort(key=lambda x:x[1])
    answer=q[k%len(q)][1]
  else:
    answer=-1
  return answer

food_times=[3,1,2]
k=5
print(solution(food_times,k))