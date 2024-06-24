# 풀이시간 30분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 단순하게 다음턴에 구해지는 수들을 구해가며 탐색해가는 그래프 탐색문제이다. DFS나 BFS를 통해 풀 수 있다. 수의 크기가 최대 10억이지만 구해지는 수들만 처리하면 되므로 O(N)으로 가능하다.

from collections import deque

start,target=map(int,input().split())

num=[]

q=deque([])
q.append((start,1))
num.append(start)
answer=0
while q:
  x,count=q.popleft()
  if x==target:
    answer=count
    break
  one=x*2
  two=int(str(x)+'1')
  if one<=int(1e9) and one not in num:
    q.append((one,count+1))
    num.append(one)
  if two<=int(1e9) and two not in num:
    q.append((two,count+1))
    num.append(two)

if answer==0:
  print(-1)
else:
  print(answer)
  