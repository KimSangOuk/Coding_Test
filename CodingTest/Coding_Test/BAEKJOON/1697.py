# 풀이시간 15분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 데이터의 수가 많아야 100,000개 이기 때문에 특정수에서부터 특정수를 찾아가는 탐색문제에다가 뻗어나갈 케이스가 나누어져있기 때문에 bfs로 찾아나가면 시간을 누적시키면서 답을 도출해 낼 수 있다. O(N)이기 때문에 가능하다.

from collections import deque

n,k=map(int,input().split())
visited=[-1]*100001

def bfs(n):
  q=deque([n])
  visited[n]=0
  time=0

  while q:
    v=q.popleft()
    case=[]
    case.append(v-1)
    case.append(v+1)
    case.append(v*2)
    for i in range(3):
      if 0<=case[i]<=100000 and visited[case[i]]==-1:
        q.append(case[i])
        visited[case[i]]=visited[v]+1

bfs(n)
print(visited[k])