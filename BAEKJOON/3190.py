# 이것이 취업을 위한 코딩테스트다 part03 '11. 뱀'과 동일

import heapq
from collections import deque

dx=[0,1,0,-1]
dy=[-1,0,1,0]

def turn_right(now_dir):
  now_dir+=1
  if now_dir>3:
    now_dir=0
  return now_dir

def turn_left(now_dir):
  now_dir-=1
  if now_dir<0:
    now_dir=3
  return now_dir

# 맵의 크기
n=int(input())

# 맵을 만드는데 주위에 벽을 세워서 쉽게 만듬
board=[[3]*(n+2) for _ in range(n+2)]
for i in range(1,n+1):
  for j in range(1,n+1):
    board[i][j]=0

# 사과의 개수
k=int(input())
apple=[]
for _ in range(k):
  apple_y,apple_x=map(int,input().split())
  #apple.append((apple_y,apple_x))
  board[apple_y][apple_x]=1

# 방향 전환 개수
l=int(input())
q=[]
for _ in range(l):
  dir_s,dir_=input().split()
  heapq.heappush(q,(int(dir_s),dir_))

second=0
now_dir=1
head_x,head_y=1,1
board[head_y][head_x]=2
snake=deque()
snake.append((head_y,head_x))

while True:
  # 시간 경과
  second+=1

  # 머리가 앞으로 나아갈 방향
  nx=head_x+dx[now_dir]
  ny=head_y+dy[now_dir]

  # 머리가 놓여질 곳에 벽이나 자기자신 있으면 종료
  if board[ny][nx]!=0 and board[ny][nx]!=1:
    break
  # 사과가 있으면 몸을 늘리고 꼬리를 그대로
  elif board[ny][nx]==1:
    head_x=nx
    head_y=ny
    board[head_y][head_x]=2
    snake.appendleft((head_y,head_x))
  # 사과가 있고 전진가능한 칸이면 꼬리 칸 비워줌
  elif board[ny][nx]==0:
    prev_tail_y,prev_tail_x=snake.pop()
    board[prev_tail_y][prev_tail_x]=0
    head_x=nx
    head_y=ny
    board[head_y][head_x]=2
    snake.appendleft((head_y,head_x))

  # 시간이 끝난 후 방향 전환이 있으면 전환
  if len(q)!=0 and q[0][0]==second:
    turn_dir=heapq.heappop(q)[1]
    if turn_dir=="D":
      now_dir=turn_right(now_dir)
    else:
      now_dir=turn_left(now_dir)

print(second)