# 풀이시간 초과 시간제한 2초 메모리제한 512MB
# 1회차 오답 - 시간초과 및 풀이 방식에 접근하지 못함
# 틀린 이유는 여러가지가 있다.
# 1. 구슬의 움직임을 별개로 취급해서 구하려고 함. 방문또한 마찬가지 -> 구슬이 동시에 움직여서 겹칠 때의 아이디어를 내지 못함
# 2. 최단 거리를 통해 횟수로 구하려고 함.
# 3. visited를 한정적으로 숫자만 넣을 때로 생각함
# 먼저 최단횟수를 구하는 문제이기 때문에 최단거리로 접근했다. 최단 거리로 접근했을 때, 꺾인 횟수를 따지면 문제가 풀릴 거라고 생각했기 때문이다. 그래서 꺾인 횟수를 빨간 구슬을 구했으나 파란 구슬의 움직임에 대처할 수 없었다. 그래서 움직인 거리로 풀리는게 아닐까라는 생각으로 움직임도 더 해보았으나 불가능했다. 왜 구슬의 움직임이 함께 움직인다는 점을 생각하지 못해서 좌표를 같이 움직일 생각을 하지 못했는가? 두개 이상의 물체가 동시에 움직이는 탐색은 해본적이 없기도 하고 동시에 움직여도 한쪽에 몰리면 움직임이 따로가 된다고 생각했기 때문이다. 왜 한쪽에 몰릴 때에 방향에 따른 동시에 움직임을 생각하지 못했는가? 좌표가 갈리면 움직임을 동시로 하는 것이 의미없다고 생각했기도 하고 동시에 움직여서 앞에 구슬 때문에 움직이지 못하는 경우가 있을 시에 따지기가 어렵다고 생각했다. 즉, 한쪽에 몰아서 끝까지 움직이는 것까지는 생각했으나 구슬이 겹쳤을 경우에 먼저 움직인 구슬을 찾는 경우의 아이디어를 생각하지 못했고 visited에 횟수만 넣을 생각을 했기에 BFS로 기록이 될 거라고 생각을 하지를 못했다. 후자의 경우 BFS가 단지 거리나 방문만을 생각하고 좌표로써의 방문은 생각하지 못했기 때문에 BFS에 도달하지 못한 점이 크다. 물체가 따로 움직일 경우에도 좌표로써의 방문 기록이 가능하다는 것을 알게 되었다. 물론 같이 움직일 때, 물체의 크기가 다르면 기록이 가능하다는 점도 알고 있었지만 따로 움직이는 경우에 좌표를 두개를 두어서 같은 경우가 발생하지 않으면 이라는 경우는 처음 경험해 보기 때문에 생각하지 못했고 visited에 오로지 길이나 크기 방문 여부만을 넣으면 된다는 편견이 강하게 잡혀있다는 것을 부시게 되었다. 전자의 경우는 방향이 달라서 겹치지 않을 경우를 계속해서 생각했기에 겹쳤을 경우만 전의 한칸으로 이동거리가 더 움직인 구슬을 뒤로 뺀다는 생각을 하지 못했다. 애초에 겹치면 안된다고만 생각하고 있었기에 반대로 겹쳤을 때, 대처하는 방식을 하지 못했다고 볼 수 있다. 즉, 특정 경우가 안되면 그것을 제한할 생각만 하고 그 경우가 됬을 때, 대처하는 경우는 생각하지 못했다고 할 수 있다. 이게 말이 되는 것이 파란 구슬이 먼저 움직이거나 빨간 구슬이 먼저 움직인 경우만 생각해서 이게 먼저 움직였다고 할 조건을 구하는게 어렵다고 생각하고만 있었기 때문에 생각하지 못한 것이지 이미 이동한 상태에서 취소를 할 생각은 하지 못했다. 앞으로는 방법이 불가능하다면 방법을 시행하기 전에 제한을 거는 방법과 즉, 파란 구슬을 이동시켜놓고 빨간 구슬의 이동을 생각하거나 빨간 구슬의 이동을 생각해놓고 파란구슬의 이동을 생각하는 방법, 아니면 이미 이동시켜놓고 겹치면 이동거리가 긴 구슬을 이동방향으로 취소하는 방법을 구할 수 있다고 할 수 있겠다. 하지만 이 경우에도 DFS라는 아이디어를 냈어야 했고 DFS를 생각하기 위해서는 방향이 계속해서 바뀌기 때문에 기록을 어떻게 하지를 생각했어야 했고 결국, 구슬의 두 위치를 기록으로 두는 생각을 했어야 했다.
# 결과적으로 이 문제의 1회차 풀이에서 배운 것은 실행전 상황에서 해결하는 방법이 아닌 실행 후 대처하는 식의 해결 방법과 visited에는 방문 횟수와 특정 수가 아닌 특정 좌표나 위치가 들어갈 수 있다는 점이다. 특히 좌표가 여러개거나 동시발생이 아닐 경우에 더욱 들어갈 수 있다는 점을 인지하고 있어야 겠다.

from collections import deque
import sys
input = sys.stdin.readline # 빠른 입출력 위한 코드

n, m = map(int, input().split())
graph = []
for i in  range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R': # 빨간구슬 위치
            rx, ry = i, j
        elif graph[i][j] == 'B': # 파란구슬 위치
            bx, by = i, j

# 상 하 좌 우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = [] # 방문여부를 판단하기 위한 리스트
    visited.append((rx, ry, bx, by))
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10: # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            if graph[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 count출력
                print(count)
                return 
            for i in range(4): # 4방향 탐색
                nrx, nry = rx, ry
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break
                if graph[nbx][nby] == 'O': # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited: # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1) # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우
bfs(rx, ry, bx, by)

### 내 풀이

from collections import deque

n,m=map(int,input().split())

dx=[0,0,-1,1]
dy=[-1,1,0,0]

bluePos=[]
redPos=[]
board=[]
visited=set()
for i in range(n):
    arr=list(input())
    for j in range(m):
        if arr[j]=='B':
            bluePos=[i,j]
        if arr[j]=='R':
            redPos=[i,j]
    board.append(arr)

q=deque()
q.append((redPos[0],redPos[1],bluePos[0],bluePos[1],0))
visited.add((redPos[0],redPos[1],bluePos[0],bluePos[1]))
answer=-1
while q:
    rx,ry,bx,by,cnt=q.popleft()
    if cnt>=10:
        break
    for i in range(4):
        nrx,nry,nbx,nby=rx,ry,bx,by
        distR=0
        distB=0
        while board[nrx+dx[i]][nry+dy[i]]!='#' and board[nrx][nry]!='O':
            nrx=nrx+dx[i]
            nry=nry+dy[i]
            distR+=1
        while board[nbx+dx[i]][nby+dy[i]]!='#' and board[nbx][nby]!='O':
            nbx=nbx+dx[i]
            nby=nby+dy[i]
            distB+=1
        if board[nbx][nby]=='O':
            continue
        if (nrx,nry,nbx,nby) in visited:
            continue
        if board[nrx][nry]=='O':
            answer=cnt+1
            break
        if nrx==nbx and nry==nby:
            if distR>distB:
                nrx-=dx[i]
                nry-=dy[i]
            else:
                nbx-=dx[i]
                nby-=dy[i]
        visited.add((nrx,nry,nbx,nby))
        q.append((nrx,nry,nbx,nby,cnt+1))
    if answer!=-1:
        break
print(answer)
