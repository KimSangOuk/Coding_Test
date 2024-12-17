import sys
from collections import deque

input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

for tc in range(int(input())):
    h,w=map(int,input().split())
    board=[]
    board.append(['.']*(w+2))
    q=deque()
    visited=[[False]*(w+2) for _ in range(h+2)]
    doorDict=dict()
    for i in range(h):
        arr=list(input().strip())
        for j in range(w):
            if arr[j].isalpha() and arr[j].isupper():
                if arr[j] not in doorDict:
                    doorDict[arr[j]]=[]
                doorDict[arr[j]].append((i+1,j+1))
        board.append(['.']+arr+['.'])
    board.append(['.']*(w+2))
    keySet=set(list(input()))
    for key in keySet:
        if key.upper() in doorDict:
            for x,y in doorDict[key.upper()]:
                board[x][y]='.'

    q.append((0,0))
    visited[0][0]=True
    answer=0
    mid=set()

    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=h+2 or ny>=w+2:
                continue
            if board[nx][ny]=='*':
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny].isalpha():
                if board[nx][ny].islower():
                    if board[nx][ny].upper() in doorDict:
                        for x,y in doorDict[board[nx][ny].upper()]:
                            board[x][y]='.'
                            if (x,y) in mid:
                                q.append((x,y))
                                mid.remove((x,y))
                                visited[x][y]=True
                    q.append((nx,ny))
                    visited[nx][ny]=True
                else:
                    mid.add((nx,ny))
            else:
                q.append((nx,ny))
                visited[nx][ny]=True
                if board[nx][ny]=='$':
                    board[nx][ny]='.'
                    answer+=1
    print(answer)