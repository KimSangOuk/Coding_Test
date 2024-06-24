# 풀이시간 43분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 모든 방향을 완전탐색으로 찾은 후 각 방향별 게임 진행을 코드로 구현하면 된다. 게임 진행 시에는, 방향에 따라 한쪽 방향으로 몰면서 수를 방향 우선으로 더해주면 되는 문제이다.
# 거의 한번에 풀어냈다.

from collections import deque

n=int(input())

board=[]
for i in range(n):
  board.append(list(map(int,input().split())))

answer=0

def combine(array,d):
  line=[]
  if d==-1:
    for i in range(0,n):
      if array[i]!=0:
        line.append(array[i])
  else:
    for i in range(n-1,-1,-1):
      if array[i]!=0:
        line.append(array[i])
  re_line=[]
  if len(array)!=0:
    q=deque(line)
    while True:
      if len(q)==0:
        break
      if len(q)==1:
        re_line.append(q.popleft())
      else:
        if q[0]==q[1]:
          re_line.append(q.popleft()+q.popleft())
        else:
          re_line.append(q.popleft())
  re_line=re_line+[0]*(n-len(re_line))
  return re_line if d==-1 else re_line[::-1]

def push_side(board,d):
  
  if d==0 or d==2:
    for j in range(n):
      line=[]
      for i in range(n):
        line.append(board[i][j])
      k=-1 if d==0 else 1
      line=combine(line,k)
      for i in range(n):
        board[i][j]=line[i]
  else:
    for i in range(n):
      line=[]
      for j in range(n):
        line.append(board[i][j])
      k=-1 if d==1 else 1
      line=combine(line,k)
      for j in range(n):
        board[i][j]=line[j]

def play_game(directions):
  global answer
  game_setting=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      game_setting[i][j]=board[i][j]
  
  for dir in directions:
    push_side(game_setting,dir)

  for i in range(n):
    answer=max(answer,max(game_setting[i]))
  

def dfs(d,dir):
  if d==5:
    play_game(dir)
  else:
    for i in range(4):
      dir.append(i)
      dfs(d+1,dir)
      dir.pop()

count=0
dfs(0,[])
print(answer)