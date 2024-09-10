import math

def findPos(num,r):
    width=2**r
    sx,sy=0,0
    pattern=-1
    startAreaNum=1
    patternBoard={1:(0,0) ,2:(0,1),3:(1,1),4:(1,0)}
    while True:
        if width==1:
            break

        if num<startAreaNum+(width//2)*(width//2):
            pattern=1
        elif num<startAreaNum+(width//2)*(width//2)*2:
            pattern=2
        elif num<startAreaNum+(width//2)*(width//2)*3:
            pattern=3
        elif num<startAreaNum+(width//2)*(width//2)*4:
            pattern=4

        sx,sy=sx+patternBoard[pattern][0]*(width//2),sy+patternBoard[pattern][1]*(width//2)
        startAreaNum+=(width//2)*(width//2)*(pattern-1)


        if pattern==1:
            patternBoard[2],patternBoard[4]=patternBoard[4],patternBoard[2]
        if pattern==4:
            patternBoard[1],patternBoard[3]=patternBoard[3],patternBoard[1]

        width=width//2
    return sx,sy

for _ in range(int(input())):
    n,h,o=map(int,input().split())
    x1,y1=findPos(h,n)
    x2,y2=findPos(o,n)
    k=(abs(x1-x2)*10)**2+(abs(y1-y2)*10)**2
    print(round(math.sqrt(k)))