# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 레이저 통신의 시작 빛 한 점에서부터 다른 빛까지의 최소 거리를 구하는 문제이니 DFS나 최단 거리 알고리즘인 데익스트라 알고리즘으로 구할 수 있다고 생각할 수 있다. 이 때, 데이터의 크기는 10000이고 시간복잡도는 ElogV로 구할 수 있거나 N으로 구할 수 있는데 E는 V^2보다 작기 때문에 두개 다 가능하다.데익스트라로 나는 풀었는데 이 때, 방향이 기존의 방향과 다를 경우에 가중치를 1해주면된다. 이 때, 기존의 0인 지점에 새롭게 방향이 바뀐 상태가 다른 값이 들어 오면서 기존의 들렸던 칸은 다시 못들리는 현상이 발생할 수 있는데 이러한 상태를 막아주기 위해서 상태별로 데이터를 저장하기 위해 방향별로 진행상태를 표현하기 위해서 2차원 배열에 3차원으로 방향을 더해주었다. 도착하는 빛이 들어오는 각 방향의 차원 중에서 최소 값을 구해주면 된다.

import heapq

dx=[0,0,1,-1]
dy=[-1,1,0,0]

w,h=map(int,input().split())

INF=int(1e9)

board=[]
array_c=[]
for i in range(h):
  array=list(input())
  for j in range(w):
    if array[j]=='C':
      array_c.append((i,j))
  board.append(array)

distance=[[[INF]*(w) for _ in range(h)] for _ in range(4)]

def dijkstra(start):
  q=[]
  for i in range(4):
    heapq.heappush(q,(0,i,start))
    distance[i][start[0]][start[1]]=0
  while q:
    dist,dir,now=heapq.heappop(q)
    if distance[dir][now[0]][now[1]]<dist:
      continue
    for i in range(4):
      nx=now[0]+dx[i]
      ny=now[1]+dy[i]
      if nx<0 or nx>=h or ny<0 or ny>=w:
        continue
      if board[nx][ny]=='*':
        continue
      cost=dist
      if dir!=i:
        cost+=1
      if distance[i][nx][ny]>cost:
        distance[i][nx][ny]=cost
        heapq.heappush(q,(cost,i,(nx,ny)))

dijkstra(array_c[0])

result=INF
for i in range(4):
  result=min(result,distance[i][array_c[1][0]][array_c[1][1]])
print(result)
      