# 풀이시간 38분 시간제한 1초 메모리제한 1024MB
# 1회차 정답
# 방향을 다루는 시뮬레이션 유형이다. 처음 구름의 이동 명령을 받아서 구름을 각 명령 받은 방향으로 이동시킨다. 이때, 1열과 n열, 1행과 n행이 연결되어 있어 다시 처음으로 돌아오는 식이므로 나머지를 이용해서 좌표를 구해주면 된다. 그런 후 나머지 단계에서 구름의 위치가 사용되기 때문에 이동시킨 구름의 좌표를 저장해준다. 그런 후 대각선 방향에 있는 물이 있는 칸만큼 형재의 칸을 증가시키고 구름이 있는 칸을 제외하고 나머지 칸 중 물의 양이 2 이상인 칸을 찾아서 물을 감소시키면서 새로운 구름을 찾아주면 된다.

n,m=map(int,input().split())

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

a=[]
cloud=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for _ in range(n):
    a.append(list(map(int,input().split())))

for count_m in range(m):
    d,s=map(int,input().split())
    step2=[]
    for x,y in cloud:
        nx=(x+s*dx[d-1])%n
        ny=(y+s*dy[d-1])%n
        a[nx][ny]+=1
        step2.append((nx,ny))
    cloud=[]
    for x,y in step2:
        count=0
        for i in range(4):
            nx=x+dx[i*2+1]
            ny=y+dy[i*2+1]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if a[nx][ny]>0:
                count+=1
        a[x][y]+=count
    step2=set(step2)
    for i in range(n):
        for j in range(n):
            if a[i][j]>=2 and (i,j) not in step2:
                cloud.append((i,j))
                a[i][j]-=2

result=0
for i in range(n):
    for j in range(n):
        result+=a[i][j]
print(result)
