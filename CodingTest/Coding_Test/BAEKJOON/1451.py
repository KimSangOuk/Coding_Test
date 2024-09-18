n,m=map(int,input().split())
board=[list(map(int,list(input()))) for _ in range(n)]

prefixSum=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        leftUp=0 if i-1<0 or j-1<0 else prefixSum[i-1][j-1]
        left=0 if j-1<0 else prefixSum[i][j-1]
        up=0 if i-1<0 else prefixSum[i-1][j]
        prefixSum[i][j]=board[i][j]+up+left-leftUp

answer=0
for i in range(n):
    for j in range(m):
        firstX,firstY=i,j
        firstSize=prefixSum[firstX][firstY]
        if firstX==n-1 and firstY!=m-1:
            secondY=m-1
            for secondX in range(n-1):
                secondSize=prefixSum[secondX][secondY]-prefixSum[secondX][firstY]
                thirdSize=prefixSum[n-1][m-1]-prefixSum[firstX][firstY]-prefixSum[secondX][secondY]+prefixSum[secondX][firstY]
                answer=max(answer,firstSize*secondSize*thirdSize)
            secondX=n-1
            for secondY in range(m-1):
                secondSize=prefixSum[secondX][secondY]-prefixSum[secondX][firstY]
                thirdSize=prefixSum[n-1][m-1]-prefixSum[secondX][secondY]
                answer=max(answer,firstSize*secondSize*thirdSize)
        elif firstY==m-1 and firstX!=n-1:
            secondX=n-1
            for secondY in range(m-1):
                secondSize=prefixSum[secondX][secondY]-prefixSum[firstX][secondY]
                thirdSize=prefixSum[n-1][m-1]-prefixSum[firstX][firstY]-prefixSum[secondX][secondY]+prefixSum[firstX][secondY]
                answer=max(answer,firstSize*secondSize*thirdSize)
            secondY=m-1
            for secondX in range(n-1):
                secondSize=prefixSum[secondX][secondY]-prefixSum[firstX][secondY]
                thirdSize=prefixSum[n-1][m-1]-prefixSum[secondX][secondY]
                answer=max(answer,firstSize*secondSize*thirdSize)
        else:
            secondX=n-1
            secondY=m-1
            thirdX=firstX
            thirdY=m-1
            secondSize=prefixSum[secondX][secondY]-prefixSum[thirdX][thirdY]
            thirdSize=prefixSum[thirdX][thirdY]-prefixSum[firstX][firstY]
            answer=max(answer,firstSize*secondSize*thirdSize)
            thirdX=n-1
            thirdY=m-1
            secondX=n-1
            secondY=firstY
            thirdSize=prefixSum[thirdX][thirdY]-prefixSum[secondX][secondY]
            secondSize=prefixSum[secondX][secondY]-prefixSum[firstX][firstY]
            answer=max(answer,firstSize*secondSize*thirdSize)
print(answer)