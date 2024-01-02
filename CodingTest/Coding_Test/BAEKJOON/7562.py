# 풀이시간 15분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 체스판의 크기가 커봤자 90,000이기 때문에 탐색할 데이터의 수가 같다. 그렇기에 O(N)인 DFS나 BFS를 사용하면서 특정 지점부터 다른 특정 지점까지를 탐색할 수 있는데 이 때, 각 걸린 횟수를 측정하므로 BFS를 사용하는 편이 쉽다.

from collections import deque

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]

def bfs(board,start,end):
  q=deque([start])
  board[start[0]][start[1]]=0
  while q:
    vx,vy=q.popleft()
    for i in range(8):
      nx=vx+dx[i]
      ny=vy+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n or board[nx][ny]!=-1:
        continue
      board[nx][ny]=board[vx][vy]+1
      q.append((nx,ny))

for tc in range(int(input())):
  n=int(input())
  visited=[[-1]*n for _ in range(n)]

  start=tuple(map(int,input().split()))
  end=tuple(map(int,input().split()))
  
  bfs(visited,start,end)
  
  print(visited[end[0]][end[1]])