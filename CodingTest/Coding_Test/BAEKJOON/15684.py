# 풀이시간 1시간 시간제한 2초 메모리제한 512MB
# 2회차 정답
# 사다리를 타는 과정에서 시간초과가 발생하는거 같아서 그래프 탐색에서 단순 좌표 이동으로 해주었더니 맞은 문제.

from collections import deque

n,m,h=map(int,input().split())

board=[[0]*(n+1) for _ in range(h+2)]

for _ in range(m):
    a,b=map(int,input().split())
    board[a][b]=1

result=4

def check_i_to_i():
    for i in range(1,n+1):
        now_n=i
        for j in range(0,h+2):
            if board[j][now_n-1]==1:
                now_n-=1
            elif board[j][now_n]==1:
                now_n+=1
        if now_n!=i:
            return False

    return True

def dfs(count):
    global result
    if count==3:
        if check_i_to_i():
            result=min(result,count)
            return
    else:
        if check_i_to_i():
            if result>count:
                result=count
                return
        if count+1>=result:
            return
        for i in range(1,h+1):
            for j in range(1,n):
                if board[i][j]==0 and board[i][j-1]==0 and board[i][j+1]==0:
                    board[i][j]=1
                    count+=1
                    dfs(count)
                    count-=1
                    board[i][j]=0

dfs(0)
if result>3:
    print(-1)
else:
    print(result)

# 풀이시간 2시간/1시간 시간제한 2초 메모리제한 512MB
# 1회차 정답 - But, 풀이시간 너무 오래 걸림
# 처음에는 조합을 통해 완전탐색으로 풀면되겠거니 해서 빈공간을 찾은 후 사다리를 설치하는 경우를 답으로 제시했다. 이럴 경우에 약 1000만회의 조합의 경우의 수가 나오는데 여기다가 각 조합에서 사다리타기만 진행해도 6번이 곱해져서 6000만회로 시간초과가 나왔다. 그래서 시간을 줄이기 위해서는 추가되는 사다리를 늘려가면서 들어가는 DFS를 사용하면 겹치는 경우의 수가 줄어들 것이라고 생각했고 시간초과를 해결하기 위해 DFS를 사용해서 벽을 놓는 것만 변경했다. 하지만 진행도는 올라가도 올라가서 시간초과로 다시 막히길래 방법을 찾다가 현재의 답으로 구해놓은 count보다 진행하려는 count가 많을 때는 진행할 필요가 없다는 것을 알았다. 그래서 적용시켰더니 시간초과를 통과하였다.
# 왜 조합의 경우의 수를 사용해서 풀면서 DFS의 방법은 생각하지 못했는가? 경우의 수가 DFS로 벽을 놓으나 똑같다고 생각을 하였다. 단순히 벽을 놓는 방법의 차이라고만 생각했다. 하지만 두가지 경우에 시간복잡도가 줄어들었다. 즉, 벽을 놓는 가짓수의 갯수가 많기 때문에 놓아가는 순서에서는 중복되는 방법은 한가지로 해결된다. 예를 들어 같은 곳에 놓는 벽을 1개,2개,3개를 놓는방법이 조합에서는 3가지이지만 DFS에서는 1개,2개를 놓는방법이 3개 놓는방법안에 포함되어 경우의 수가 줄어든다. 또한 조건을 벽을 놓으면서 걸수 있기 때문에 효율성이 늘어난다. 벽을 놓고나서 그 조합이 가능한지를 일일이 확인하는 것은 시간이 확인하는 알고리즘에 따라 배로 들지만 놓으면서 확인하는 것은 조건문 하나 걸치는 정도로 해결할 수 있다. 조합의 갯수만 확인하고 세부 알고리즘의 시간복잡도는 확인하지 않았기에 처음에 조합으로 풀어서 시간을 낭비하는 경우를 사전 제거할 수 있다. 또한 특정 벽을 놓는 경우에 또한 갯수를 늘리거나 하는 경우에는 특히, 중간에 벽을 놓는 조건이 달리는 경우도 마찬가지다. 시간복잡도를 줄일 수 있다는 사실을 배웠다.

import sys

input=sys.stdin.readline

n,m,h=map(int,input().split())
board=[[0]*(n+1) for _ in range(h+1)]

for _ in range(m):
  a,b=map(int,input().split())
  board[a][b]=1

def start_end_self(board,start):
  end=start
  for i in range(1,h+1):
    if board[i][start]==1:
      start+=1
    elif board[i][start-1]==1:
      start-=1       
  if start!=end:
    return False
  else:
    return True

def set_play_ladder_game(count):
  global answer
  if count==3:
    pass_all=True
    for i in range(1,n+1):
      if not start_end_self(board,i):
        pass_all=False
        break
    if pass_all:
      answer=min(answer,count)
  else:
    pass_all=True
    for i in range(1,n+1):
      if not start_end_self(board,i):
        pass_all=False
        break
    if pass_all:
      answer=min(answer,count)
    for i in range(1,h+1):
      for j in range(1,n):
        # 현재 자리에 사다리가 없거나 옆에 사다리가 없으면 사다리를 놓는다.
        if board[i][j]!=1:
          if ((j-1>=1 and board[i][j-1]!=1) or j-1<1) and (j+1>n or (j+1<=n and board[i][j+1]!=1)):
            count+=1
            board[i][j]+=1
            # 현재의 답보다 count가 작을때만 수행한다.
            if count<answer:
              set_play_ladder_game(count)
            board[i][j]-=1
            count-=1

answer=4
set_play_ladder_game(0)
if answer>3:
  print(-1)
else:
  print(answer)