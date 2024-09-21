from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(distTree,key,start,dust,board):
    x,y=start
    q=deque([(x,y)])
    visited=[[-1]*w for _ in range(h)]
    visited[x][y]=0
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if board[nx][ny]=='x':
                continue
            if visited[nx][ny]!=-1:
                continue
            q.append((nx,ny))
            visited[nx][ny]=visited[now[0]][now[1]]+1
    if key=='cleaner':
        distTree['cleaner']=dict()
        for dustKey in dust:
            distTree['cleaner'][dustKey]=visited[dust[dustKey][0]][dust[dustKey][1]]
    else:
        distTree[key]=dict()
        for dustKey in dust:
            if key!=dustKey:
                distTree[key][dustKey]=visited[dust[dustKey][0]][dust[dustKey][1]]

def updateDistTree(distTree,cleaner,dust,board):
    for k in dust.keys():
        bfs(distTree,k,dust[k],dust,board)
    bfs(distTree,'cleaner',cleaner,dust,board)

def dfs(fromDust,dust,deep,visited,distSum):
    global answer,distTree
    if deep==dustNum:
        answer=min(answer,distSum)
        return
    for i in dust.keys():
        if visited&(1<<i):
           continue
        dfs(i,dust,deep+1,visited|(1<<i),distSum+distTree[fromDust][i])

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    board=[]
    cleaner=tuple()
    dust=dict()
    dustNum=0
    for i in range(h):
        arr=list(input())
        for j in range(w):
            if arr[j]=='.' or arr[j]=='x':
                continue
            if arr[j]=='o':
                cleaner=(i,j)
            elif arr[j]=='*':
                dust[dustNum]=(i,j)
                dustNum+=1
        board.append(arr)
    distTree=dict()
    updateDistTree(distTree,cleaner,dust,board)
    canFoundAll=True
    for k in distTree['cleaner'].keys():
        if distTree['cleaner'][k]==-1:
            canFoundAll=False
            break
    if not canFoundAll:
        print(-1)
        continue
    answer=1e9
    visited=0
    for dk in distTree['cleaner'].keys():
        dfs(dk,dust,1,visited|(1<<dk),distTree['cleaner'][dk])
    print(answer)
