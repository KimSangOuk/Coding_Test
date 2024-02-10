# 풀이시간 40분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 각 구간을 단계별로 크기를 나누어서 각 구간을 회전시킨 후 각 칸을 순회하며 주위의 얼음이 3개 미만으로 있으면 -1 녹이는 문제이다. 후에 답을 구할 때는 전체 칸의 얼음을 더하고 또 bfs로 제일 큰 얼음 덩어리의 크기를 구하면 된다. 시뮬레이션이자 완전탐색 문제라고도 할 수 있겠다.

from collections import deque

n,q=map(int,input().split())

dx=[0,0,-1,1]
dy=[1,-1,0,0]

a=[]
for _ in range(2**n):
    a.append(list(map(int,input().split())))

q=list(map(int,input().split()))

def turn_clock_90(board):
    length=len(board)
    tmp=[[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            tmp[j][length-i-1]=board[i][j]
    return tmp

for stage in q:
    step=2**stage
    for i in range(0,2**n,step):
        for j in range(0,2**n,step):
            new_board=[[0]*step for _ in range(step)]
            for l in range(step):
                for m in range(step):
                    new_board[l][m]=a[i+l][j+m]
            new_board=turn_clock_90(new_board)
            for l in range(step):
                for m in range(step):
                    a[i+l][j+m]=new_board[l][m]

    minus_board=[[False]*(2**n) for _ in range(2**n)]

    for i in range(2**n):
        for j in range(2**n):
            count=0
            for d in range(4):
                nx=i+dx[d]
                ny=j+dy[d]
                if nx<0 or ny<0 or nx>=2**n or ny>=2**n:
                    continue
                if a[nx][ny]>0:
                    count+=1
            if count<3:
                minus_board[i][j]=True
    for i in range(2**n):
        for j in range(2**n):
            if minus_board[i][j] and a[i][j]>0:
                a[i][j]-=1

def bfs(visited,start_x,start_y):
    global bigest_ice
    q=deque()
    q.append((start_x,start_y))
    visited[start_x][start_y]=True
    count=0
    while q:
        now_x,now_y=q.popleft()
        count+=1
        for i in range(4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if nx<0 or ny<0 or nx>=2**n or ny>=2**n:
                continue
            if visited[nx][ny]:
                continue
            if a[nx][ny]==0:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
    bigest_ice=max(bigest_ice,count)

sum_ice=0
bigest_ice=0
visited=[[False]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        sum_ice+=a[i][j]
        if not visited[i][j] and a[i][j]>0:
            bfs(visited,i,j)

print(sum_ice)
print(bigest_ice)