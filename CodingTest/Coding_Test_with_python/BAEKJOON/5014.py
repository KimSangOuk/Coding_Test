# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 현재 층에서 다른 층까지 가는 경로를 탐색하면서 다이나믹 방식으로 BFS를 통해 누적해 나가면 되는 문제이다.

from collections import deque

f,s,g,u,d=map(int,input().split())

visited=[-1]*(f+1)

def bfs(start):
  q=deque()
  q.append(start)
  visited[start]=0
  while q:
    now=q.popleft()
    up_stair=now+u
    down_stair=now-d
    if up_stair<=f and visited[up_stair]==-1:
      visited[up_stair]=visited[now]+1
      q.append(up_stair)
    if down_stair>=1 and visited[down_stair]==-1:
      visited[down_stair]=visited[now]+1
      q.append(down_stair)

bfs(s)
if visited[g]==-1:
  print("use the stairs")
else:
  print(visited[g])