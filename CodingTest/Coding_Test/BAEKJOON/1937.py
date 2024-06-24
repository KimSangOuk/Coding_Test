# 풀이시간 20분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 주어진 보드에서 경로중 가장 긴 경로가 나오는 경우를 탐색하는 것이기 때문에, DFS나 BFS 등의 그래프 탐색으로 풀 수 있다고 할 수 있다. 시간복잡도도 O(N)이기에 가능하다. 이 때, 모든 지점에서 탐색을 해버리면 N^2이 되버려서 불가능하므로 겪은 지점은 다시 안들리게 하는것이 최선이라는 것을 알 수 있는데, 그렇게 하기 위해서는 다이나믹 프로그래밍으로 기록해둘 수 있는지 보아야한다. 다이나믹 프로그래밍은 전까지의 해로 지금의 해를 구하는데 쓰는 것이기 때문에 깊이 탐색으로 들어갔다 나오면서 기록한다면, 주위에 되는 깊이 중 가장 큰 값 중 +1을 하면 현재의 좌표까지의 최대 거리를 dp에 저장하며 구할 수 있으며 이미 방문을 했다면 값만 받아오면 되기 때문에 총 O(N)회만 연산하면 된다.

import sys
sys.setrecursionlimit((10**5)*3)

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n=int(input())
board=[]

for _ in range(n):
  board.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)]

def dfs(x,y):
  max_value=0
  if dp[x][y]!=0:
    return dp[x][y]

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or nx>=n or ny<0 or ny>=n:
      continue
    if board[nx][ny]<board[x][y]:
      max_value=max(max_value,dfs(nx,ny))

  dp[x][y]=max_value+1
  return dp[x][y]
  
    
answer=0
for i in range(n):
  for j in range(n):
    if dp[i][j]==0:
      answer=max(answer,dfs(i,j))

print(answer)
