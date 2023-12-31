# 풀이시간 60분/60분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 상황을 코드로 표현하며 풀어가는 시뮬레이션 문제이다. 이 때 주사위를 나타내는 것이 제일 중요한데 가로와 세로의 변화를 각각 두어서 표현하고 회전이 끝난 후, 각 아래 위만 변하는 점을 이용해서 복사를 해주었다.

from collections import deque

n,m,x,y,k=map(int,input().split())

board=[]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

x,y=y,x

for _ in range(n):
  board.append(list(map(int,input().split())))

k=list(map(int,input().split()))

dice=[deque([0,0,0,0]),deque([0,0,0,0])]

for d in k:
  nx=x+dx[d-1]
  ny=y+dy[d-1]
  if ny<0 or ny>=n or nx<0 or nx>=m:
    continue

  x,y=nx,ny
  if d>2:
    wl=1
  else:
    wl=0
  
  if d==1 or d==4:
    dice[wl].append(dice[wl].popleft())
  elif d==2 or d==3:
    dice[wl].appendleft(dice[wl].pop())
  
  if board[ny][nx]==0: 
    board[ny][nx]=dice[wl][0]
  else:
    dice[wl][0]=board[ny][nx]
    board[ny][nx]=0

  temp=int(not bool(wl))
  dice[temp][0],dice[temp][2]=dice[wl][0],dice[wl][2]
  
  print(dice[wl][2])