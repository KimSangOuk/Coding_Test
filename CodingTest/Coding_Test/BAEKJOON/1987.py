# 풀이시간 15분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 단순히 문제에서 특정 깊이까지 알파벳의 사용유무를 체크하면서 탐색해 나아가면 되는 문제이다. 데이터의 양은 400밖에 되지 않기 때문에 DFS를 충분히 사용할 수 있으며 깊이는 따로 체크하면서 들어가면 된다.

r,c=map(int,input().split())

alpha=[False]*26

board=[]
for _ in range(r):
  board.append(list(input()))

answer=0

def dfs(x,y,deep):
  global answer
  if x<0 or x>=c or y<0 or y>=r or alpha[ord(board[y][x])-ord('A')]:
    answer=max(answer,deep)
    return
  elif not alpha[ord(board[y][x])-ord('A')]:
    alpha[ord(board[y][x])-ord('A')]=True
    dfs(x,y-1,deep+1)
    dfs(x,y+1,deep+1)
    dfs(x-1,y,deep+1)
    dfs(x+1,y,deep+1)
    alpha[ord(board[y][x])-ord('A')]=False

dfs(0,0,0)
print(answer)