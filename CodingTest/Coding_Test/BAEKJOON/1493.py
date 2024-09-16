length,width,height=map(int,input().split())

n=int(input())
cubes=[]

for i in range(n):
    type,cnt=map(int,input().split())
    cubes.append([type,cnt])

cubes.sort()

fail=False
answer=0
prevVolume=length*width*height
prevL=1

for i in range(n):
    L=2**cubes[i][0]

    nLength=length//(L/prevL)
    nWidth=width//(L/prevL)
    nHeight=height//(L/prevL)

    nVolume=(nLength*nWidth*nHeight)*(L**3)

    if cubes and (prevVolume-nVolume)//(prevL**3)>cubes[i-1][1]:
        lastVolume=prevVolume-nVolume
        index=i-1
        while lastVolume>0 and index>=0:
            nLen=cubes[index][0]
            target=((2**nLen)**3)*cubes[index][1]
            if target>=lastVolume:
                k=lastVolume//((2**nLen)**3)
                cubes[index][1]-=k
                answer+=k
                lastVolume=0
                break
            else:
                answer+=cubes[index][1]
                cubes[index][1]=0
                lastVolume-=target
                index-=1
        if lastVolume>0:
            fail=True
            break
    elif cubes:
        cubes[i-1][1]-=(prevVolume-nVolume)//(prevL**3)
        answer+=(prevVolume-nVolume)//(prevL**3)
    if i==n-1:
        if nLength*nWidth*nHeight>cubes[i][1]:
            lastVolume=(nLength*nWidth*nHeight-cubes[i][1])*(L**3)
            answer+=cubes[i][1]
            index=i-1
            while lastVolume>0 and index>=0:
                nLen=cubes[index][0]
                target=((2**nLen)**3)*cubes[index][1]
                if target>=lastVolume:
                    answer+=lastVolume//((2**nLen)**3)
                    lastVolume=0
                    break
                else:
                    answer+=cubes[index][1]
                    lastVolume-=target
                    index-=1
            if lastVolume>0:
                fail=True
            break
        else:
            answer+=nLength*nWidth*nHeight
            break
    prevVolume=(nLength*nWidth*nHeight)*(L**3)
    length,width,height=nLength,nWidth,nHeight
    prevL=L

if fail:
    print(-1)
else:
    print(int(answer))