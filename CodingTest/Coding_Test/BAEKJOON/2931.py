from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

dirDict={}
dirDict['|']={0:0,2:2}
dirDict['-']={1:1,3:3}
dirDict['+']={0:0,2:2,1:1,3:3}
dirDict['1']={0:1,3:2}
dirDict['2']={3:0,2:1}
dirDict['3']={1:0,2:3}
dirDict['4']={1:2,0:3}

n,m=map(int,input().split())
board=[]
startPos=[]
endPos=[]
visitedSet=set()
for i in range(n):
    arr=list(input())
    for j in range(m):
        if arr[j]!='.':
            visitedSet.add((i,j))
        if arr[j]=='M':
            startPos=(i,j)
        elif arr[j]=='Z':
            endPos=(i,j)
    board.append(arr)

def findLostPos(board,start):
    q=deque()
    dir=-1
    for i in range(4):
        nx=start[0]+dx[i]
        ny=start[1]+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if board[nx][ny]!='.' and board[nx][ny]!='Z':
            dir=i
            q.append((nx,ny))
            break
    while q:
        now=q.popleft()
        goDirFromNow=dirDict[board[now[0]][now[1]]][dir]
        nx=now[0]+dx[goDirFromNow]
        ny=now[1]+dy[goDirFromNow]
        if board[nx][ny]=='.':
            return (nx,ny)
        else:
            dir=goDirFromNow
            q.append((nx,ny))

def testRoute(board,start):
    visited=set()
    visited.add(start)
    q=deque()
    dir=-1
    for i in range(4):
        nx=start[0]+dx[i]
        ny=start[1]+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if board[nx][ny]!='.' and board[nx][ny]!='Z':
            dir=i
            q.append((nx,ny))
            visited.add((nx,ny))
            break
    while q:
        now=q.popleft()
        if dir not in dirDict[board[now[0]][now[1]]]:
            return False
        goDirFromNow=dirDict[board[now[0]][now[1]]][dir]
        nx=now[0]+dx[goDirFromNow]
        ny=now[1]+dy[goDirFromNow]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            return False
        elif board[nx][ny]=='.':
            return False
        elif board[nx][ny]=='Z':
            visited.add((nx,ny))
            if visited==visitedSet:
                return True
            return False
        else:
            dir=goDirFromNow
            q.append((nx,ny))
            visited.add((nx,ny))
    return False

lostPos=findLostPos(board,startPos)
visitedSet.add(lostPos)
answer=-1
for key in ('|','-','1','2','3','4','+'):
    board[lostPos[0]][lostPos[1]]=key
    if testRoute(board,startPos):
        print(lostPos[0]+1,lostPos[1]+1,key)
        break
    board[lostPos[0]][lostPos[1]]='.'