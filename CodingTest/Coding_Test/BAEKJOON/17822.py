# 풀이시간 1시간 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 시뮬레이션 문제이자 BFS/DFS 탐색 문제이다. 처음 원판이 주어지고 원판을 주어진 조건에 따라 먼저 회전 시킨다. 이경우에는 덱을 이용해서 방향과 횟수에 따라 회전시켜주며 배수가 되는 원판만 회전시켜주면 된다. 그런 후 인접한 수들을 구해야하는데, 원판의 경우 서로 이어지기 때문에 하나의 2차원 배열이라고 생각하고 인접한 수는 인접한 행이거나 인접한 열인데, 회전시 열은 끝과 시작이 이어지는 점만 유의해주면 된다. 2차원 배열중에서 그렇게 인접한 좌표를 전부 찾아주면 되고 이 경우에 따라 또 있을 때, 없을 때의 경우가 나누어지기 때문에 먼저 배열에 전부 담아서 그 배열이 존재하는지를 확인하면 된다. 있을 경우에는 그 좌표들을 전부 0으로 처리해서 없애주고 없을 경우에는 0이 아닌 좌표들의 모든 수와 모든 합을 구해서 평균을 구해주고 이 때, 전부 0일 수 있는데 이 때는 그냥 넘어가주면 된다. 평균을 구해서 0이 아닌 수들 중, 평균 값에 따라 +-1을 해주면 된다.

from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m,t=map(int,input().split())

plate=[]
for _ in range(n):
    plate.append(deque(list(map(int,input().split()))))

def turn(arr,d,k):
    for _ in range(k):
        if d==0:
            arr.appendleft(arr.pop())
        else:
            arr.append(arr.popleft())

def bfs(visited,x,y):
    global near
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    num=plate[x][y]
    new=[]
    while q:
        now=q.popleft()
        new.append((now[0],now[1]))
        for i in range(4):
            nx=now[0]+dx[i]
            ny=(now[1]+dy[i])%m
            if nx<0 or nx>=n:
                continue
            if visited[nx][ny]:
                continue
            if plate[nx][ny]==0:
                continue
            if num==plate[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
    if len(new)>1:
        near+=new


for tc in range(t):
    x,d,k=map(int,input().split())
    for i in range(1,n+1):
        if i%x==0:
            turn(plate[i-1],d,k)
    near=[]
    visited=[[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and plate[i][j]!=0:
                bfs(visited,i,j)
    if len(near)>0:
        for x,y in near:
            plate[x][y]=0
    else:
        sum_value=0
        count=0
        for i in range(n):
            for j in range(m):
                if plate[i][j]>0:
                    count+=1
                    sum_value+=plate[i][j]
        if count==0:
            continue
        avg=sum_value/count
        for i in range(n):
            for j in range(m):
                if plate[i][j]>avg and plate[i][j]>0:
                    plate[i][j]-=1
                elif plate[i][j]<avg and plate[i][j]>0:
                    plate[i][j]+=1

result=0
for i in range(n):
    result+=sum(plate[i])
print(result)