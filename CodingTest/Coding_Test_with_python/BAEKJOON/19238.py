# 풀이시간 1시간 20분 시간제한 1초 메모리제한 512MB
# 1회차 정답 - But 시간 초과
# 시뮬레이션 문제이자 최단거리를 측정하기 위한 BFS 문제라고 할 수 있다.
# 먼저 도착지의 위치는 겹칠 수 있기 때문에 도착지의 위치와 택시의 위치는 따로 받고 손님의 출발 위치는 맵에 기록해 둔다. 이는 손님을 찾을 때에는 여러가지 중 하나를 찾지만 목적지는 하나 이기 때문이기도 하다. 먼저 손님을 찾는데 손님의 위치는 전부 다르기 때문에 BFS를 사용하여 모든 손님의 거리와 위치 번호를 찾아놓는데 택시의 시작 위치에 손님이 있을 수도 있으므로 큐에서 꺼내는 즉시의 상태에서 검사하여야 한다. 그렇게 찾았을 때, 만약 찾아진 손님이 없다면 두가지 경우로 나누어진다. 만약 모든 손님을 이미 처리해서 없는 경우는 끝내서 연료를 출력하면 되고, 만약 벽으로 막혀 도달하지 못할 수도 있기 때문에 손님이 남아있는데 찾지 못한 경우는 -1을 출력한다. 손님을 찾고 연료의 양이 충분한지 한번 확인 하고, 또한 손님을 지도 상에서 지워주면 된다. 택시는 손님 위치로 이동한다. 그리고 나서 손님의 목적지까지의 거리를 찾는다. 이때는 단순히 거리만 찾으면 되고 도달이 불가능한 곳일 경우에는 마찬가지로 -1을 출력한다. 택시의 연료와 위치 정보를 찾은 곳으로 업데이트하면 된다.
# 시간 초과를 걸리면서 깨달은게 조건에 모든 경우를 주지 않을 수 있다는 점을 깨달았다. 즉, 숨겨진 조건을 찾아야 하는데, 첫번째 택시의 위치같은 경우, 시작할 때, 빈칸이라는 점만 주고 나머진 주지 않았기 때문에 겹칠 수 있다는 점을 알고 있어야 한다. 두 번째의 경우, 출발지는 서로 다르고, 각 손님의 출발지의 목적지는 서로 다르다라고 하였기 때문에 출발지는 다르고 목적지는 같을 수 있으며, 목적지가 곧 출발지가 될 수 있다는 사실을 캐치해야 한다. 이렇게 모든 케이스를 전부 주지 않는 경우가 있을 수 있기 때문에 경우의 수를 전부 생각해야 한다.

from collections import deque
import copy

dx=[0,0,-1,1]
dy=[-1,1,0,0]

n,m,fuel_amount=map(int,input().split())
customer_cnt=m

board=[] # 지도
for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(n):
        if arr[j]==1:
            arr[j]='-'
    board.append(arr)

taxi_x,taxi_y=map(int,input().split())
taxi_x,taxi_y=taxi_x-1,taxi_y-1

target_pos=dict()

for i in range(1,m+1):
    start_x,start_y,end_x,end_y=map(int,input().split())
    board[start_x-1][start_y-1]=i
    target_pos[i]=[end_x-1,end_y-1]

def find_nearest_customer(now_x,now_y):
    q=deque()
    visited=[[-1]*n for _ in range(n)]
    q.append((now_x,now_y))
    visited[now_x][now_y]=0
    customer=[]
    while q:
        now=q.popleft()
        if board[now[0]][now[1]]>0:
            customer.append((visited[now[0]][now[1]],now[0],now[1],board[now[0]][now[1]]))
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if board[nx][ny]=='-':
                continue
            if visited[nx][ny]>=0:
                continue
            q.append((nx,ny))
            visited[nx][ny]=visited[now[0]][now[1]]+1

    if len(customer)==0:
        return False
    customer.sort()
    return customer[0]

def find_customer_target(now_x,now_y,target_num):
    q=deque()
    visited=[[-1]*n for _ in range(n)]
    q.append((now_x,now_y))
    visited[now_x][now_y]=0
    while q:
        now=q.popleft()
        if now[0]==target_pos[target_num][0] and now[1]==target_pos[target_num][1]:
            return [visited[now[0]][now[1]],now[0],now[1]]
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if board[nx][ny]=='-':
                continue
            if visited[nx][ny]>=0:
                continue
            q.append((nx,ny))
            visited[nx][ny]=visited[now[0]][now[1]]+1
    return False

find=True
while True:
    # 가장 가까운 승객 찾기
    nearest_customer=find_nearest_customer(taxi_x,taxi_y)
    if not nearest_customer: # 승객이 더 이상 없으면 끝
        if customer_cnt==0:
            break
        else:
            find=False
            break
    dist,customer_x,customer_y,customer_num=nearest_customer

    # 택시가 이동
    if fuel_amount<=dist:
        find=False
        break
    fuel_amount-=dist
    board[customer_x][customer_y]=0
    taxi_x,taxi_y=customer_x,customer_y

    target_info=find_customer_target(taxi_x,taxi_y,customer_num)
    if not target_info:
        find=False
        break
    dist,target_x,target_y=target_info
    if dist>fuel_amount:
        find=False
        break
    fuel_amount-=dist
    fuel_amount+=dist*2
    taxi_x,taxi_y=target_x,target_y

    customer_cnt-=1

if not find:
    print(-1)
else:
    print(fuel_amount)