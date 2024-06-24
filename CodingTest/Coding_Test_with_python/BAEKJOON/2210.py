# 풀이시간 20분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 5*5 보드에서 깊이가 6자리가 될때까지 깊이 탐색을 모든 칸에서 모든 방향으로 수행하면 된다. DFS이자 브루트포스 알고리즘이라고 할 수 있다.

answer=set([])

board=[]
for i in range(5):
  board.append(list(map(int,input().split())))

def dfs(now,s,deep):
  global answer
  if now[0]<0 or now[0]>=5 or now[1]<0 or now[1]>=5:
    return
  if deep==6:
    s+=str(board[now[0]][now[1]])
    answer.add(s)
  else:
    s+=str(board[now[0]][now[1]])
    dfs((now[0]+1,now[1]),s,deep+1)
    dfs((now[0]-1,now[1]),s,deep+1)
    dfs((now[0],now[1]+1),s,deep+1)
    dfs((now[0],now[1]-1),s,deep+1)

for i in range(5):
  for j in range(5):
    dfs((i,j),"",1)

print(len(list(answer)))