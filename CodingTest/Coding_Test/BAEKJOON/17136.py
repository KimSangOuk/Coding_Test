import sys

input=sys.stdin.readline
board=[]

for i in range(10):
    board.append(list(map(int,input().split())))

visited=0
for i in range(10):
    for j in range(10):
        if board[i][j]==1:
            visited|=(1<<(i*10+j))

answer=26
paperCounter=[5,5,5,5,5]

def dfs(visited,paperCounter):
    global answer

    for c in paperCounter:
        if c<0:
            return
    if visited==0:
        answer=min(answer,25-sum(paperCounter))
        return
    for i in range(10):
        for j in range(10):
            if not visited&(1<<(10*i+j)):
                continue
            for tempSize in range(1,5+1):
                if i+tempSize>10 or j+tempSize>10:
                    break
                tmpVisited=visited
                notPaperInSize=False
                for a in range(i,i+tempSize):
                    for b in range(j,j+tempSize):
                        if not tmpVisited&(1<<(10*a+b)):
                            notPaperInSize=True
                            break
                        tmpVisited&=~(1<<(10*a+b))
                    if notPaperInSize:
                        break
                if notPaperInSize:
                    break
                paperCounter[tempSize-1]-=1
                dfs(tmpVisited,paperCounter)
                paperCounter[tempSize-1]+=1
            return

dfs(visited,paperCounter)
if answer==26:
    print(-1)
else:
    print(answer)
