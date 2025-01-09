import sys

input=sys.stdin.readline

N=int(input())

board=[list(map(int,input().split())) for _ in range(N)]

cnt=dict()
cnt['-1']=0
cnt['0']=0
cnt['1']=0

def divide_conquer(n,board,i,j):
    side=n//3
    numSet=set()
    for a in range(i,i+n):
        for b in range(j,j+n):
            numSet.add(board[a][b])
    if len(numSet)==1:
        cnt[str(list(numSet)[0])]+=1
        return
    else:
        divide_conquer(side,board,i,j)
        divide_conquer(side,board,i+side,j)
        divide_conquer(side,board,i+side*2,j)
        divide_conquer(side,board,i,j+side)
        divide_conquer(side,board,i,j+side*2)
        divide_conquer(side,board,i+side,j+side)
        divide_conquer(side,board,i+side*2,j+side)
        divide_conquer(side,board,i+side*2,j+side*2)
        divide_conquer(side,board,i+side,j+side*2)

divide_conquer(N,board,0,0)

print(cnt['-1'])
print(cnt['0'])
print(cnt['1'])