# 풀이시간 20분 시간제한 6초 메모리제한 256MB
# 1회차 정답
# 각 4가지 경우를 다음의 경우로 현재의 방문에서 부터 문자 키를 더해가면 된다. BFS로 방문 안한 경우에만 탐색하는 방식으로 나아가면 된다.

from collections import deque

for tc in range(int(input())):
  a,b=map(int,input().split())
  visited=[-1]*10000

  q=deque()
  q.append(a)
  visited[a]=""

  while q:
    n=q.popleft()
    d=(2*n)%10000
    s=(n-1)%10000
    to_str=str(n)
    to_str=(4-len(to_str))*"0"+to_str
    l=int(to_str[1:]+to_str[0])
    r=int(to_str[-1]+to_str[:-1])
    if visited[d]==-1:
      visited[d]=visited[n]+"D"
      q.append(d)
    if visited[s]==-1:
      visited[s]=visited[n]+"S"
      q.append(s)
    if visited[l]==-1:
      visited[l]=visited[n]+"L"
      q.append(l)
    if visited[r]==-1:
      visited[r]=visited[n]+"R"
      q.append(r)
  print(visited[b])