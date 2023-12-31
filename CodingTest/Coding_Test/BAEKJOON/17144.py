# 풀이시간 1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 상황을 코드로 나타내는 시뮬레이션 유형이다. 이 때, 먼지가 퍼지는 과정부터 설명하자면 각 지점에서 퍼지는 영향을 따로 저장해야 서로 겹치는 상황을 막을 수 있어 차후에 더해주는 것이 좋다.
# 그 후 바람의 순환을 한 리스트에 담아서 풀어주면 되는 문제이다. 솔직히 더 코드를 줄이고 단순화를 함수를 통해서 시킬 수 있거나 밑에 문단 4개를 반으로 줄일 수 있었으나 자기 직전 컨디션 이슈와 렉 이슈로 여기까지만 풀도록 하겠다.

from collections import deque

r,c,t=map(int,input().split())

board=[]
air_machine=[]

for i in range(r):
  arr=list(map(int,input().split()))
  for j in range(c):
    if arr[j]==-1:
      air_machine.append(i)
  board.append(arr)

dx=[0,1,0,-1]
dy=[-1,0,1,0]

for _ in range(t):

  get_board=[[0]*c for _ in range(r)]
  
  for i in range(r):
    for j in range(c):
      if board[i][j]>0:
        y,x=i,j
        count=0
        for k in range(4):
          nx=x+dx[k]
          ny=y+dy[k]
          if ny<0 or ny>=r or nx<0 or nx>=c or board[ny][nx]==-1:
            continue
          count+=1
          get_board[ny][nx]+=board[i][j]//5
        board[i][j]=board[i][j]-board[i][j]//5*count
  for i in range(r):
    for j in range(c):
      board[i][j]+=get_board[i][j]

  up_air=[]
  up_air_tail=deque([])
  for i in range(air_machine[0],-1,-1):
    if air_machine[0]==i:
      up_air+=board[i][1:]
    elif i==0:
      tmp=board[i][::-1]+list(up_air_tail)
      up_air=deque(up_air+tmp)
    else:
      up_air_tail.appendleft(board[i][0])
      up_air.append(board[i][-1])
  up_air.appendleft(0)
  up_air.pop()
  # print(up_air)

  down_air=[]
  down_air_tail=deque([])
  for i in range(air_machine[1],r):
    if air_machine[1]==i:
      down_air+=board[i][1:]
    elif i==r-1:
      tmp=board[i][::-1]+list(down_air_tail)
      down_air=deque(down_air+tmp)
    else:
      down_air_tail.appendleft(board[i][0])
      down_air.append(board[i][-1])
  down_air.appendleft(0)
  down_air.pop()
  # print(down_air)
  
  for i in range(air_machine[0],-1,-1):
    if air_machine[0]==i:
      for j in range(1,c):
        board[i][j]=up_air[j-1]
      up_air=[up_air[i] for i in range(c-1,len(up_air)) ]
    elif i==0:
      board[i]=up_air[::-1]
    else:
      board[i][0]=up_air[-1]
      board[i][-1]=up_air[0]
      up_air=up_air[1:-1]

  for i in range(air_machine[1],r):
    if air_machine[1]==i:
      for j in range(1,c):
        board[i][j]=down_air[j-1]
      down_air=[down_air[i] for i in range(c-1,len(down_air)) ]
    elif i==r-1:
      board[i]=down_air[::-1]
    else:
      board[i][0]=down_air[-1]
      board[i][-1]=down_air[0]
      down_air=down_air[1:-1]

answer=0
for i in range(r):
  answer+=sum(board[i])
  
print(answer+2)