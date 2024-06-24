# 풀이시간 15분 시간제한 2초 메모리제한 512MB
# 2회차 정답
# 단순하게 문제를 코드로 그대로 구현해내는 시뮬레이션 유형이다. 시간복잡도는 제일 커도 2500*4이기 때문에 충분하다.

n,m=map(int,input().split())

y,x,d=map(int,input().split())

dx=[0,1,0,-1]
dy=[-1,0,1,0]

def rotate(d):
  return (d-1)%4

board=[]
for _ in range(n):
  board.append(list(map(int,input().split())))

clean=[[0]*m for _ in range(n)]
answer=0

while True:
  if clean[y][x]==0:
    clean[y][x]=1
    answer+=1

  turn=0
  
  for _ in range(4):
    d=rotate(d)
    turn+=1
    nx=x+dx[d]
    ny=y+dy[d]
    if board[ny][nx]==1 or clean[ny][nx]==1:
      continue
    x,y=nx,ny
    turn=0
    break
  if turn==4:
    nx=x-dx[d]
    ny=y-dy[d]
    if board[ny][nx]!=1:
      x,y=nx,ny
    else:
      break

print(answer)

# # 풀이시간 2시간 시간제한 2초 메모리제한 512MB
# # 1회차 시간초과 오답
# # 먼저 최대 맵의 크기가 50인 점을 통해 이동횟수를 반복문으로 돌린다하더라도 최대 2500회이기 때문에 시간복잡도 O(N^2)까지 쓸 수 있다는 점을 알게되었다. 게다가 2초이니 두배 정도가 나도 괜찮기 때문이다.
# # 시간이 상당히 오래 걸렸는데 문제를 제대로 읽지 못했다는 점이 가장 크다. 동서남북의 지정 숫자를 제대로 확인하지 못해서 오답판정 이유를 찾는데 엄청난 시간이 걸렸다. 헛발질하느라...

# # n 행 m 열
# n,m=map(int,input().split())
# # 청소기의 좌표와 방향
# r,c,d=map(int,input().split())
# # 벽과 빈칸의 지도
# board=[]
# for _ in range(n):
#   board.append(list(map(int,input().split())))

# trash_map=[[0]*m for _ in range(n)]

# def rotate(d):
#   d-=1
#   if d<0:
#     d=3
#   return d

# dx=[0,1,0,-1]
# dy=[-1,0,1,0]

# while True:
#   # 회전한 횟수
#   turn=0
#   # 현재칸이 청소가 되지 않았다면 청소한다.
#   if trash_map[r][c]==0:
#     trash_map[r][c]=1
#   # 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
#   for _ in range(4):
#     d=rotate(d)
#     nr=r+dy[d]
#     nc=c+dx[d]
#     if board[nr][nc]==1 or trash_map[nr][nc]==1:
#       turn+=1
#   # 바라보는 방향을 유지한 채로
#   if turn==4:
#     # 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#     if board[r-dy[d]][c-dx[d]]==0:
#       r=r-dy[d]
#       c=c-dx[d]
#       continue
#     # 만약 뒤가 벽이라 후진할 수 없다면 작동을 멈춘다.
#     else:
#       break
#   # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
#   else:
#     for _ in range(4):
#       # 90도 반시계 방향으로 회전
#       d=rotate(d)
#       # 앞에 있는 구역 확인
#       nr=r+dy[d]
#       nc=c+dx[d]
#       # 앞에 있는 구역이 빈칸이면서 청소가 안되있으면
#       if board[nr][nc]==0 and trash_map[nr][nc]==0:
#         r=nr
#         c=nc
#         break

# answer=0
# for i in range(n):
#   answer+=trash_map[i].count(1)

# # for i in range(n):
# #   print(trash_map[i])

# print(answer)