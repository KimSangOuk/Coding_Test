import sys

input=sys.stdin.readline

N=int(input())

board=[list(map(int,input().split())) for _ in range(N)]

def divide_conquer(n,board,i,j):
    side=n//2
    if side==1:
        arr=[]
        arr.append(board[i][j])
        arr.append(board[i][j+1])
        arr.append(board[i+1][j])
        arr.append(board[i+1][j+1])
        arr.sort()
        return arr[-2]
    else:
        arr=[]
        arr.append(divide_conquer(side,board,i,j))
        arr.append(divide_conquer(side,board,i+side,j))
        arr.append(divide_conquer(side,board,i,j+side))
        arr.append(divide_conquer(side,board,i+side,j+side))
        arr.sort()
        return arr[-2]
print(divide_conquer(N,board,0,0))