# 풀이시간 15분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 강의의 시작과 끝 시간이 주어지기 때문에 강의가 시작하는 순으로 강의가 정렬되어 쓰인다는 것을 알 수 있다. 하지만 그 다음에는 가장 빨리 끝나는 강의가 필요하다. 그값을 위해서는 힙큐에 첫번쨰 원소를 이용해서 구할 수 있다. 새로운 강의가 시작할 때, 그 강의의 시작 전에 끝나는 강의들을 끝내어 강의실을 비우고 새로운 강의를 시작하면 되는데 이 때, 힙큐에 넣었을 때라면, 힙큐의 길이가 가장 긴 순간을 구하면 된다.

import heapq

n=int(input())
arr=[]
for _ in range(n):
  start,end=map(int,input().split())
  arr.append((start,end))

arr.sort()
q=[]
answer=0
for k in arr:
  heapq.heappush(q,(k[1],k[0]))
  while q and q[0][0]<=k[0]:
    heapq.heappop(q)
  answer=max(answer,len(q))

print(answer)
    