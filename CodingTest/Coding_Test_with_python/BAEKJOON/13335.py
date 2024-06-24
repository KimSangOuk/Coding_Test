# 풀이시간 30분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 버스의 이동과 투입을 큐로 나타내어서 초에 따른 상황에 따라 표현하면 되는 문제이다. 상황을 나타내는 시뮬레이션 문제라고 할 수 있다.
# 다리가 비어있을 경우 무조건 적으로 트럭을 투입시킨다.
# 다리가 비어있지 않을 경우에, 바로 나갈 트럭을 제외한 나머지 다리위의 트럭의 무게와 새로 들어올 트럭의 무게의 합이 최대 하중보다 높다면 트럭은 대기하고 마지막 트럭은 나가기만 한다.
# 또 최대 하중보다 낮다면 새롭게 트럭을 투입하고 마지막 트럭은 나간다.
# 마지막으로 모든 트럭이 원래 있던 트럭 순으로 나온다면 마무리 한다.

from collections import deque
import copy

n,w,l=map(int,input().split())
trucks=deque(list(map(int,input().split())))
answer=copy.deepcopy(trucks)
bridge=deque([0]*w)
out=deque([0]*n)

s=0
while True:
  s+=1
  if sum(bridge)==0:
    bridge.append(trucks.popleft())
    bridge.popleft()
    trucks.append(0)
  elif sum(list(bridge)[1:])+trucks[0]>l:
    k=bridge.popleft()
    if k>0:
      out.append(k)
      out.popleft()
    bridge.append(0)
  elif sum(list(bridge)[1:])+trucks[0]<=l:
    k=bridge.popleft()
    if k>0:
      out.append(k)
      out.popleft()
    bridge.append(trucks.popleft())
    trucks.append(0)

  check=True
  for i in range(n):
    if out[i]!=answer[i]:
      check=False
      break
  if check:
    break

print(s)