# 백준 '트럭'과 유사한 문제

from collections import deque

def solution(bridge_length, weight, truck_weights):

  out=deque()
  bridge=deque([0]*bridge_length)
  total_trucks=len(truck_weights)
  truck_weights=deque(truck_weights)
  total_bridge_weight=0
  
  
  time=0
  while True:
    if len(out)==total_trucks:
      break

    if total_bridge_weight==0:
      k=truck_weights.popleft()
      total_bridge_weight+=k
      bridge.append(k)
      bridge.popleft()
      truck_weights.append(0)
    elif total_bridge_weight-bridge[0]+truck_weights[0]<=weight:
      k=truck_weights.popleft()
      total_bridge_weight+=k
      bridge.append(k)
      truck_weights.append(0)
      last_block_bridge=bridge.popleft()
      total_bridge_weight-=last_block_bridge
      if last_block_bridge>0:
        out.append(last_block_bridge)
    elif total_bridge_weight-bridge[0]+truck_weights[0]>weight:
      bridge.append(0)
      last_block_bridge=bridge.popleft()
      total_bridge_weight-=last_block_bridge
      if last_block_bridge>0:
        out.append(last_block_bridge)

    time+=1

  return time

bridge_length=2
weight=10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights)) # 8

bridge_length=100
weight=100
truck_weights=[10]
print(solution(bridge_length, weight, truck_weights)) # 101

bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights)) # 110