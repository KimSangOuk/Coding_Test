from collections import deque
import copy

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def fallDown(arr):
    new_arr=[]
    for i in range(h):
        if arr[i]!=0:
            new_arr.append(arr[i])
    return [0]*(h-len(new_arr))+new_arr

def clearBlock(now_board,pos):
    board=copy.deepcopy(now_board)
    q=deque()
    q.append((pos[0],pos[1],board[pos[0]][pos[1]]))
    while q:
        x,y,t=q.popleft()
        for i in range(t):
            for k in range(4):
                nx=x+dx[k]*i
                ny=y+dy[k]*i
                if nx<0 or ny<0 or nx>=h or ny>=w:
                    continue
                q.append((nx,ny,board[nx][ny]))
                board[nx][ny]=0
    new_board=[[0]*w for _ in range(h)]
    for j in range(w):
        arr=[]
        for i in range(h):
            arr.append(board[i][j])
        arr=fallDown(arr)
        for i in range(h):
            new_board[i][j]=arr[i]
    return new_board

def getAnswer(board):
    cnt=0
    for i in range(h):
        for j in range(w):
            if board[i][j]>0:
                cnt+=1
    return cnt

def play(board,deep,n):
    global answer
    if getAnswer(board)==0:
        answer=0
        return
    if deep==n:
        answer=min(getAnswer(board),answer)
        return
    for i in range(w):
        for j in range(h):
            if board[j][i]>0:
                new_board=clearBlock(board,(j,i))
                play(new_board,deep+1,n)
                break

for tc in range(1,int(input())+1):
    n,w,h=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(h)]
    answer=1000
    play(board,0,n)
    print("#"+str(tc)+" "+str(answer))
