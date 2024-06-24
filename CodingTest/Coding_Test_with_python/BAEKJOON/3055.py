# 풀이시간 35분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 물과 햄스터의 초마다 움직임을 끊어야하는 문제이다. 그렇기 때문에 BFS를 이용하여 각 이동할 수 있는 가지를 덱에 저장해 두고 각 초에는 저장되어있는 덱의 길이 만큼만 딱 돌려 주면 움직임을 초단위로 끊을 수 있다. 이 때, 햄스터의 경우에는 방문경로를 따로 해두어 돌아가지 않도록 하고 물은 맵에 직접적으로 표시해도 된다. 이런 경우에서 햄스터는 다음에 방문할 칸에 도착지가 있으면 정답을 return 하고 다음에 방문할 곳이 덱에 하나도 들어가지 않는다면, 물에 다 막히거나 이동할 수 없는 상태이기 때문에 KATUS를 리턴한다.

from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

board=[]
target=0
hedgehog=deque()
water=deque()
visited=[[False]*m for _ in range(n)]
for i in range(n):
  arr=list(input())
  for j in range(m):
    if arr[j]=='D':
      target=(i,j)
    elif arr[j]=='S':
      hedgehog.append((i,j))
      visited[i][j]=True
    elif arr[j]=='*':
      water.append((i,j))
  board.append(arr)

def play_game():
  time=0
  while True:
    for _ in range(len(water)):
      x,y=water.popleft()
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
          continue
        if board[nx][ny]=='D' or board[nx][ny]=='X':
          continue
        if board[nx][ny]=='*':
          continue
        water.append((nx,ny))
        board[nx][ny]='*'

    for _ in range(len(hedgehog)):
      x,y=hedgehog.popleft()
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
          continue
        if visited[nx][ny]:
          continue
        if board[nx][ny]=='X' or board[nx][ny]=='*':
          continue
        if board[nx][ny]=='D':
          return time+1
        hedgehog.append((nx,ny))
        visited[nx][ny]=True

    if len(hedgehog)==0:
      return "KAKTUS"
    time+=1

answer=play_game()
print(answer)
  