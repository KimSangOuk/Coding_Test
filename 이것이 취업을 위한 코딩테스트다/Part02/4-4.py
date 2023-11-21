# 풀이시간 40분 초과해서 다시 재풀이
# 초과 이유 : 방향 및 x,y 축, 현재 좌표 등에 대해서 생각할 부분이 꼬이다 보니 코드를 수정하게 됨.
# 또한 시뮬레이션 되는 상황을 돌려보지 않고 진행하다 보니 조건부분에서 꼬이게 됨.
# ex) 원래 방향으로 다시 돌아오는 경우 중에서 4번을 돌고 실패해서 돌아오는 경우를 생각해야 되는데 이부분을 한 번에 생각하지 못함.

n,m=map(int,input().split())
a,b,d=map(int,input().split())
board=[]
dx=[0,-1,0,1]
dy=[-1,0,1,0]

# 여기서도 python 한정의 문제풀이인점을 이용해서 전역변수를 활용하면 현재 실시간으로 바뀌는 방향으로 이용할 수 있음 -> 코드의 길이를 줄일 수 있음
def find_next_dir(d):
  if d==3:
    return 0
  else:
    return d+1

for _ in range(n):
  board.append(list(map(int,input().split())))
# 굳이 여기서 맵을 합칠 필요가 없이. 현재 맵과 이동표시 맵을 구분해도 됨.
# 이걸 통해 복잡하게 생각할 부분을 더욱 단순화 가능하게 만듬

result=1
board[a][b]=2
full_rotate=False

while True:
  next_dir=find_next_dir(d)
  # 그리고 여기서 한 템포에 모든걸 끊을 필요 없이 회전 수 만큼 받은 넘어갈 수도 있음.
  # 여기서도 템포를 나눌 수 있게 됨녀서 더욱 단순화 가능하게 만듬
  for i in range(4):
    ny=a+dy[next_dir]
    nx=b+dx[next_dir]
    # 주변에 벽이 있는지 없는지를 조건에서 확인해서 영역처리를 할 필요가 있는지 없는지를 잘 확인해야 됨. 만약 코드를 단순화 시키고 싶을 때는 벽을 추가해서 단순화 시킨다음 해도 됨.
    if nx<0 or ny<0 or nx>=m or ny>=n or board[ny][nx]!=0:
      next_dir=find_next_dir(next_dir)
      if next_dir==d:
        full_rotate=True
      continue
    elif board[ny][nx]==0:
      # 가보고
      a=ny
      b=nx
      d=next_dir
      print(d,"로 감",a,b)
      result+=1
      board[ny][nx]=2
      break
  if full_rotate==True:
    ny=a-dy[d]
    nx=b-dx[d]
    if nx<0 or ny<0 or nx>=m or ny>=n or board[ny][nx]==1:
      break
    else:
      a=ny
      b=nx
      print("뒤로 감",a,b)
  full_rotate=False

print(result)

# # 답안 예시
# # N, M을 공백으로 구분하여 입력받기
# n, m=map(int,input().split())

# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d=[[0]*m for _ in range(n)]
# # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
# x,y,direction=map(int,input().split())
# d[x][y]=1 # 현재 좌표 방문 처리

# # 전체 맵 정보를 입력받기
# array=[]
# for i in range(n):
#   array.append(list(map(int,input().split())))

# # 북, 동, 남, 서 방향 정의
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]

# # 왼쪽으로 회전
# def turn_left():
#   global direction
#   direction -=1
#   if direction == -1:
#     direction=3

# # 시뮬레이션 시작
# count=1
# turn_time=0
# while True:
#   # 왼쪽으로 회전
#   turn_left()
#   nx=x+dx[direction]
#   ny=y+dy[direction]
#   # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#   if d[nx][ny]==0 and array[nx][ny]==0:
#     d[nx][ny]=1
#     x=nx
#     y=ny
#     count+=1
#     turn_time=0
#     continue
#   # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#   else:
#     turn_time+=1
#   # 네 방향 모두 갈 수 없는 겨우
#   if turn_time==4:
#     nx=x-dx[direction]
#     ny=y-dy[direction]
#     # 뒤로 갈 수 있다면 이동하기
#     if array[nx][ny]==0:
#       x=nx
#       y=ny
#     # 뒤가 바다로 막혀있는 경우
#     else:
#       break
#     turn_time=0

# # 정답 출력
# print(count)