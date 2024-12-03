import sys
input=sys.stdin.readline

n=int(input())
opers=[tuple(list(map(int,input().split()))) for _ in range(n)]

redBoard=[[0]*4 for _ in range(4)]
boards=[[[0]*4 for _ in range(6)] for _ in range(2)]

blocks=[[] for _ in range(2)]

answer=0

def rotate(block):
    new_block=[]
    for x,y in block:
        new_block.append((y,3-x))
    return new_block

def allStackBlock(board,blocks):
    newBlocks=[]
    for block in blocks:
        for x,y in block:
            board[x][y]=0
        while True:
            nBlock=[]
            notPossibleNext=False
            for x,y in block:
                nx,ny=x+1,y
                if nx>5 or board[nx][ny]!=0:
                    notPossibleNext=True
                    break
                nBlock.append((nx,ny))
            if notPossibleNext:
                break
            block=nBlock
        for x,y in block:
            board[x][y]=1
        newBlocks.append(block)
    return newBlocks

def stackBlock(board,blocks,block):
    for x,y in block:
        board[x][y]=0
    while True:
        nBlock=[]
        notPossibleNext=False
        for x,y in block:
            nx,ny=x+1,y
            if nx>5 or board[nx][ny]!=0:
                notPossibleNext=True
                break
            nBlock.append((nx,ny))
        if notPossibleNext:
            break
        block=nBlock
    for x,y in block:
        board[x][y]=1
    blocks.append(block)

def clearLine(board,blocks,lineSet):
    leftBlocks=[]
    for block in blocks:
        leftBlock=[]
        for x,y in block:
            if x not in lineSet:
                leftBlock.append((x,y))
            else:
                board[x][y]=0
        if len(leftBlock)>0:
            leftBlocks.append(leftBlock)
    return leftBlocks,board

def getDeleteLineSet(boards):
    global answer
    deleteLineSets=[set() for _ in range(2)]
    for k in range(2):
        for i in range(5,1,-1):
            full=True
            for j in range(4):
                if boards[k][i][j]!=1:
                    full=False
                    break
            if full:
                answer+=1
                deleteLineSets[k].add(i)
    if len(deleteLineSets[0])>0 or len(deleteLineSets[1])>0:
        return deleteLineSets
    for k in range(2):
        cnt=0
        for i in range(0,2):
            for j in range(4):
                if boards[k][i][j]==1:
                    cnt+=1
                    break
        if cnt>=1:
            deleteLineSets[k].add(5)
            if cnt>=2:
                deleteLineSets[k].add(4)
    return deleteLineSets

def createBlock(oper):
    t,x,y=oper
    blocks=[]
    block=[]
    if t==1:
        block.append((x,y))
    if t==2:
        block.append((x,y))
        block.append((x,y+1))
    if t==3:
        block.append((x,y))
        block.append((x+1,y))
    blocks.append(block)
    blocks.append(rotate(block))

    setBlocks=[]
    for block in blocks:
        newBlock=[]
        minX=min(block[0][0],block[1][0]) if len(block)==2 else block[0][0]
        for x,y in block:
            newBlock.append((x-minX,y))
        setBlocks.append(newBlock)

    return setBlocks

for oper in opers:
    newBlocks=createBlock(oper)

    # 블록 생성
    for thisBoard,thisNewBlock,thisBlocks in zip(boards,newBlocks,blocks):
        stackBlock(thisBoard,thisBlocks,thisNewBlock)

    deleteLineSets=getDeleteLineSet(boards)
    while len(deleteLineSets[0])>0 or len(deleteLineSets[1])>0:
        for idx in range(2):
            if len(deleteLineSets[idx])==0:
                continue
            blocks[idx],boards[idx]=clearLine(boards[idx],blocks[idx],deleteLineSets[idx])
            blocks[idx]=allStackBlock(boards[idx],blocks[idx])
        deleteLineSets=getDeleteLineSet(boards)

blockCnt=0
for k in range(2):
    for i in range(6):
        for j in range(4):
            if boards[k][i][j]==1:
                blockCnt+=1

print(answer)
print(blockCnt)

