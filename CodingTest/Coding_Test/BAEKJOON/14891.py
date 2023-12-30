# 풀이시간 30분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 주어진 상황을 시뮬레이션, 즉 코드로 풀어쓰는 문제이다. 해당 바퀴가 4개이므로 시간복잡도는 사실상 고려안해도 된다고 생각한다. 각 바퀴가 회전하기 전에 각 양쪽에 있는 바퀴들이 회전에 영향을 받아 회전을 하는지를 해놓고 한번씩만 영향을 받게해서 한 바퀴가 회전하는 경우를 코드로 표현하면 된다.

from collections import deque

gears=[[]]

for _ in range(4):
  gears.append(deque(list(map(int,input()))))

k=int(input())

cases=[]
for _ in range(k):
  number,dir=map(int,input().split())
  cases.append((number,dir))

for case in cases:
  reminder=deque([case])
  already=[False]*(5)
  while len(reminder)!=0:
    number,dir=reminder.popleft()
    nleft=number-1
    nright=number+1
    if nleft>0 and gears[nleft][2]!=gears[number][6] and not already[nleft]:
      reminder.append((nleft,-dir))
      
    if nright<=4 and gears[nright][6]!=gears[number][2] and not already[nright]:
      reminder.append((nright,-dir))

    already[number]=True
    if dir==1:
      k=gears[number].pop()
      gears[number].appendleft(k)
    else:
      k=gears[number].popleft()
      gears[number].append(k)
  # print(gears)
      
result=gears[1][0]*1+gears[2][0]*2+gears[3][0]*4+gears[4][0]*8
print(result)