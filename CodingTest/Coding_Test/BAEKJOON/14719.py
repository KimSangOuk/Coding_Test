h,w=map(int,input().split())

block=list(map(int,input().split()))
board=[[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i>=h-block[j]:
            board[i][j]=1

# for i in range(h):
#     print(board[i])

answer=0
for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if board[i][j]==1:
            continue
        else:
            left_have_wall=False
            right_have_wall=False
            ny=j
            while not left_have_wall and 0<=ny<w:
                if board[i][ny]==1:
                    left_have_wall=True
                    break
                ny-=1
            ny=j
            while not right_have_wall and 0<=ny<w:
                if board[i][ny]==1:
                    right_have_wall=True
                    break
                ny+=1
            if left_have_wall and right_have_wall:
                # print(i,j)
                answer+=1
print(answer)