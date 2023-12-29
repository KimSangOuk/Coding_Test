# 풀이 시간 - 1시간 15분/40분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이시간 초과
# 아이디어 자체는 쉽고 맵의 크기도 그렇게 크지 않아 시뮬레이션 아이디어라는게 그냥 보였다. 다만 구현하는데 시간이 좀 걸렸는데 다 구현 후, 두가지 문제가 발생했는데 방향 전환이 이상하게 된다는 점. 꼬리가 따라오지 않는다는 점이었다. 꼬리가 따라오지 않는 점은 해결하는데 시간이 소요되기 했지만 그렇게 오래 걸리지 않았지만 방향 전환을 찾는데 애먹었다. 전체 코드가 길다보니 알고리즘 쪽이 틀렸다고 생각이 되서 만지다가 방향전환부분에서 숫자하나를 잘못적은게 시간을 엄청나게 잡아먹었다.

# 2회차 풀이
# 풀이 시간 40분/40분 시간제한 1초 메모리제한 128MB
# 2회차 정답
# 금방 풀어버린 문제, 피지컬이 많이 늘긴한 것 같다고 느낀 문제이다.
# 여기서 -1%4가 안되길래 방향 설정에서 저렇게 풀었는데, 여기서 a - (b * float(a/b))라고 한다. 외우고 있는게 좋을 것 같은 방식이다.

from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())
board=[[1]*(n+2) for _ in range(n+2)]
for i in range(1,1+n):
  for j in range(1,1+n):
    board[i][j]=0
    
k=int(input())
for _ in range(k):
  a,b=map(int,input().split())
  board[a][b]=2

t=int(input())
rotate=deque()
for _ in range(t):
  a,b=map(str,input().split())
  rotate.append((int(a),b))

def dir_rotate(direction,want):
  if want=="L":
    direction-=1
    if direction<0:
      direction=3
  else:
    direction=(direction+1)%4
  return direction
  
time=0
q=deque()
q.append((1,1))
dir=0
head_x,head_y=1,1
while True:
  time+=1
  nx=head_x+dx[dir]
  ny=head_y+dy[dir]

  if board[ny][nx]==1 or (ny,nx) in q:
    break

  head_x,head_y=nx,ny
  q.append((head_y,head_x))
  if board[ny][nx]!=2:
    q.popleft()
  else:
    board[ny][nx]=0

  if len(rotate)!=0 and time==rotate[0][0]:
    dir=dir_rotate(dir,rotate[0][1])
    rotate.popleft()

print(time)

# # 1회차 풀이
# # 전체적으로 해설집이랑 비슷한 부분이 거의 대부분이고 벽을 세우거나 하는부분은 더 쉬웠기 때문에 괜찮았다. 하지만 방향을 회전하는데에서 더 짧게 구현할 수 있는 방법을 배웠다.
# import heapq
# from collections import deque

# dx=[0,1,0,-1]
# dy=[-1,0,1,0]

# # 이 두 함수를 한줄씩 처리해서 굳이 두개 함수를 나누지 않고도 나머지 값을 이용해서 쉽게 표현하는 방법을 배웠는데 숫자의 범위를 한정할 경우, 나머지를 이용하는 방법을 생각해보는 것도 좋을 것 같다.
# def turn_right(now_dir):
#   now_dir+=1
#   if now_dir>3:
#     now_dir=0
#   return now_dir

# def turn_left(now_dir):
#   now_dir-=1
#   if now_dir<0:
#     now_dir=3
#   return now_dir

# # 맵의 크기
# n=int(input())

# # 맵을 만드는데 주위에 벽을 세워서 쉽게 만듬
# board=[[3]*(n+2) for _ in range(n+2)]
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     board[i][j]=0

# # 사과의 개수
# k=int(input())
# apple=[]
# for _ in range(k):
#   apple_y,apple_x=map(int,input().split())
#   #apple.append((apple_y,apple_x))
#   board[apple_y][apple_x]=1

# # 방향 전환 개수
# l=int(input())
# q=[]
# for _ in range(l):
#   dir_s,dir_=input().split()
#   heapq.heappush(q,(int(dir_s),dir_))

# second=0
# now_dir=1
# head_x,head_y=1,1
# board[head_y][head_x]=2
# snake=deque()
# snake.append((head_y,head_x))

# while True:
#   # 시간 경과
#   second+=1

#   # 머리가 앞으로 나아갈 방향
#   nx=head_x+dx[now_dir]
#   ny=head_y+dy[now_dir]

#   # 머리가 놓여질 곳에 벽이나 자기자신 있으면 종료
#   if board[ny][nx]!=0 and board[ny][nx]!=1:
#     break
#   # 사과가 있으면 몸을 늘리고 꼬리를 그대로
#   elif board[ny][nx]==1:
#     head_x=nx
#     head_y=ny
#     board[head_y][head_x]=2
#     snake.appendleft((head_y,head_x))
#   # 사과가 있고 전진가능한 칸이면 꼬리 칸 비워줌
#   elif board[ny][nx]==0:
#     prev_tail_y,prev_tail_x=snake.pop()
#     board[prev_tail_y][prev_tail_x]=0
#     head_x=nx
#     head_y=ny
#     board[head_y][head_x]=2
#     snake.appendleft((head_y,head_x))

#   # 시간이 끝난 후 방향 전환이 있으면 전환
#   if len(q)!=0 and q[0][0]==second:
#     turn_dir=heapq.heappop(q)[1]
#     if turn_dir=="D":
#       now_dir=turn_right(now_dir)
#     else:
#       now_dir=turn_left(now_dir)

# print(second)

# # 답안지
# n = int(input())
# k = int(input())
# data=[[0]*(n+1) for _ in range(n+1)] # 맵 정보
# info = [] # 방향 회전 정보

# # 맵 정보(사과 있는 곳은 1로 표시)
# for _ in range(k):
#   a,b=map(int,input().split())
#   data[a][b]=1

# # 방향 회전 정보 입력
# l = int(input())
# for _ in range(l):
#   x,c=input().split()
#   info.append(int(x),c)

# # 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
# dx=[0,1,0,-1]
# dy=[1,0,-1,0]

# def turn(direction,c):
#   if c=="L":
#     direction=(direction-1)%4
#   else:
#     direction=(direction+1)%4
#   return direction

# def simulate():
#   x,y=1,1 # 뱀의 머리 위치
#   data[x][y]=2 # 뱀이 존재하는 위치는 2로 표시
#   direction=0 # 처음에는 동쪽을 보고 있음
#   time=0 # 시작한 뒤에 지난 '초' 시간
#   index=0 # 다음에 회전할 정보
#   q=[(x,y)]
#   while True:
#     nx=x+dx[direction]
#     ny=y+dy[direction]
#     # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
#     if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny]!=2:
#       # 사과가 없다면 이동 후에 꼬리 제거
#       if data[nx][ny]==0:
#         data[nx][ny]=2
#         q.append((nx,ny))
#         px,py=q.pop(0)
#         data[px][py]=0
#       # 사과가 있다면 이동 후에 꼬리 그대로 두기
#       if data[nx][ny]==1:
#         data[nx][ny]=2
#         q.append((nx,ny))
#     # 벽이나 뱀의 몸통과 부딪혔다면
#     else:
#       time+=1
#       break
#     x,y=nx,ny
#     time+=1
#     if index<1 and time==info[index][0]: # 회전할 시간인 경우 회전
#       direction = turn(direction,info[index][1])
#       index+=1
#   return time

# print(simulate())