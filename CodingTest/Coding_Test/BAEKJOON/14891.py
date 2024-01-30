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


# BFS를 이용해서 풀이
from collections import deque

gears_state=[deque([0]*8) for _ in range(4+1)]
for i in range(1,5):
    state=list(input())
    for j in range(0,8):
        gears_state[i][j]=int(state[j])

INF=int(1e9)
k=int(input())

def turn_gear(num,clock_dir):
    if clock_dir==-1:
        gears_state[num].append(gears_state[num].popleft())
    elif clock_dir==1:
        gears_state[num].appendleft(gears_state[num].pop())

def start_gear(start,dir):
    q=deque([start])
    visited=[INF]*(5)
    visited[start]=dir
    while q:
        now=q.popleft()
        nl=now-1
        nr=now+1
        if nl>=1 and visited[nl]==INF:
            if gears_state[now][6]!=gears_state[nl][2]:
                visited[nl]=-visited[now]
            else:
                visited[nl]=0
            q.append(nl)
        if nr<=4 and visited[nr]==INF:
            if gears_state[now][2]!=gears_state[nr][6]:
                visited[nr]=-visited[now]
            else:
                visited[nr]=0
            q.append(nr)
    for i in range(1,5):
        turn_gear(i,visited[i])

def get_score(gears):
    score=0
    if gears[1][0]==1:
        score+=1
    if gears[2][0]==1:
        score+=2
    if gears[3][0]==1:
        score+=4
    if gears[4][0]==1:
        score+=8
    return score

for _ in range(k):
    num,dir=map(int,input().split())
    start_gear(num,dir)

score=get_score(gears_state)
print(score)
